import copy
import gzip
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from compiler import (Block, SpecError, compile_set, load_spec, main,
                      parse_page, validate, write_new)


def fixture():
    root = ET.Element('Ableton', Creator='Ableton Live 11.3.43')
    live = ET.SubElement(root, 'LiveSet')
    tracks = ET.SubElement(live, 'Tracks')
    for tid, kind in [('23','AudioTrack'),('24','MidiTrack'),('14','AudioTrack'),('2','ReturnTrack')]:
        track = ET.SubElement(tracks,kind,Id=tid)
        name = ET.SubElement(track,'Name')
        for key in ['EffectiveName','UserName']:
            ET.SubElement(name,key,Value='Old')
        ET.SubElement(track,'Color',Value='1')
        ET.SubElement(track,'TrackGroupId',Value='-1')
        ET.SubElement(ET.SubElement(track,'AutomationEnvelopes'),'Envelopes')
        lanes = ET.SubElement(ET.SubElement(track,'TakeLanes'),'TakeLanes')
        take = ET.SubElement(lanes,'TakeLane',Id='1')
        events = ET.SubElement(ET.SubElement(take,'ClipAutomation'),'Events')
        ET.SubElement(events,'AudioClip',Id='0')
        dc = ET.SubElement(track,'DeviceChain')
        for key, value in [('AudioInputRouting','AudioIn/External/M2'),('AudioOutputRouting','AudioOut/Master'),
                           ('MidiInputRouting','MidiIn/External.All/-1'),('MidiOutputRouting','MidiOut/None')]:
            routing = ET.SubElement(dc,key)
            for tag,val in [('Target',value),('UpperDisplayString','Old'),('LowerDisplayString','')]:
                ET.SubElement(routing,tag,Value=val)
        seq = ET.SubElement(dc,'MainSequencer')
        ET.SubElement(seq,'MonitoringEnum',Value='1')
        ET.SubElement(ET.SubElement(seq,'Recorder'),'IsArmed',Value='false')
        arranger = ET.SubElement(ET.SubElement(seq,'ClipTimeable'),'ArrangerAutomation')
        ET.SubElement(ET.SubElement(arranger,'Events'),'MidiClip',Id='2')
        slot = ET.SubElement(ET.SubElement(seq,'ClipSlotList'),'ClipSlot',Id='0')
        ET.SubElement(ET.SubElement(ET.SubElement(slot,'ClipSlot'),'Value'),'MidiClip',Id='1')
        ET.SubElement(ET.SubElement(dc,'Devices'),'PluginDevice',Id='123',UniqueId='preserve-me')
    mixer = ET.SubElement(ET.SubElement(ET.SubElement(live,'MasterTrack'),'DeviceChain'),'Mixer')
    for key,value in [('Tempo','120'),('TimeSignature','201')]:
        ET.SubElement(ET.SubElement(mixer,key),'Manual',Value=value)
    scenes = ET.SubElement(live,'Scenes')
    for i in range(3):
        scene = ET.SubElement(scenes,'Scene',Id=str(i))
        ET.SubElement(scene,'Name',Value='')
        ET.SubElement(scene,'Color',Value='-1')
    transport = ET.SubElement(live,'Transport')
    for key,value in [('CurrentTime','256'),('LoopOn','true'),('LoopStart','8'),('LoopLength','64')]:
        ET.SubElement(transport,key,Value=value)
    locs = ET.SubElement(live,'Locators')
    ET.SubElement(ET.SubElement(locs,'Locators'),'Locator',Id='12')
    for parent,key in [(transport,'RecordKeyMidi'),(locs,'SetLocatorMapping'),(locs,'NextLocatorMapping'),(locs,'PreviousLocatorMapping')]:
        mapping = ET.SubElement(parent,key)
        for tag,value in [('PersistentKeyString','k'),('IsNote','false'),('Channel','-1'),('NoteOrController','-1'),('LowerRangeNote','-1'),('UpperRangeNote','-1'),('ControllerMapMode','0')]:
            ET.SubElement(mapping,tag,Value=value)
    return root


def spec():
    return {'props':{'spec-version':'1','live-version':'11','tempo':'96','time-signature':'4/4'},
            'sections':{}, 'sources':[]}


def track(tid='23',**extra):
    return Block('Pattern A Audio',props={'track-key':'a-audio','source-track-id':tid,'type':'audio',**extra})


class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.base = self.root/'base.als'
        self.base.write_bytes(gzip.compress(ET.tostring(fixture())))
        self.original = self.base.read_bytes()

    def tearDown(self):
        self.temp.cleanup()

    def compile(self,decl=None,fresh=False):
        result = ET.fromstring(compile_set(decl or spec(),self.base,fresh))
        self.assertEqual(self.base.read_bytes(),self.original)
        return result.find('LiveSet')

    def test_default_preserves_recordings_devices_and_locators(self):
        live = self.compile()
        self.assertEqual(len(live.findall('.//AudioClip')),4)
        self.assertEqual(len(live.findall('.//MidiClip')),8)
        self.assertEqual(len(live.findall('.//PluginDevice')),4)
        self.assertEqual(live.find('Locators/Locators/Locator').get('Id'),'12')

    def test_fresh_removes_every_content_location_preserves_devices(self):
        live = self.compile(fresh=True)
        self.assertFalse(live.findall('.//AudioClip')+live.findall('.//MidiClip'))
        self.assertEqual(len(live.findall('.//PluginDevice')),4)
        self.assertFalse(list(live.find('Locators/Locators')))
        self.assertEqual(live.find('Transport/CurrentTime').get('Value'),'0')
        self.assertEqual(live.find('Transport/LoopOn').get('Value'),'false')

    def test_prune_requires_fresh_and_preserves_returns(self):
        decl = spec(); decl['sections']['Tracks']=[track()]
        with self.assertRaisesRegex(SpecError,'pruning requires'):
            self.compile(decl)
        live = self.compile(decl,True)
        self.assertEqual([t.get('Id') for t in live.find('Tracks')],['23','2'])

    def test_routing_to_removed_track_is_rejected(self):
        decl = spec(); decl['sections']['Tracks']=[track(**{'audio-to':'AudioOut/Track.14/TrackIn'})]
        with self.assertRaisesRegex(SpecError,'missing track 14'):
            self.compile(decl,True)

    def test_fresh_preserves_device_events_and_envelopes(self):
        root=fixture()
        device=root.find('LiveSet/Tracks/AudioTrack/DeviceChain/Devices/PluginDevice')
        ET.SubElement(ET.SubElement(device,'Events'),'InternalSequence',Value='keep')
        ET.SubElement(ET.SubElement(device,'Envelopes'),'InternalEnvelope',Value='keep')
        self.base.write_bytes(gzip.compress(ET.tostring(root)))
        live=ET.fromstring(compile_set(spec(),self.base,True)).find('LiveSet')
        self.assertEqual(live.find('.//PluginDevice/Events/InternalSequence').get('Value'),'keep')
        self.assertEqual(live.find('.//PluginDevice/Envelopes/InternalEnvelope').get('Value'),'keep')

    def test_existing_group_preserved_and_missing_group_rejected(self):
        root=fixture();tracks=root.find('LiveSet/Tracks')
        group=copy.deepcopy(tracks[0]);group.tag='GroupTrack';group.set('Id','50');tracks.insert(0,group)
        tracks.find("AudioTrack[@Id='23']/TrackGroupId").set('Value','50')
        self.base.write_bytes(gzip.compress(ET.tostring(root)))
        decl=spec();decl['sections']['Tracks']=[Block('Pattern A',props={'track-key':'group-a','source-track-id':'50','type':'group'}),track()]
        live=ET.fromstring(compile_set(decl,self.base,True)).find('LiveSet')
        self.assertEqual(live.find('Tracks/GroupTrack/Name/UserName').get('Value'),'Pattern A')
        self.assertEqual(live.find('Tracks/AudioTrack/TrackGroupId').get('Value'),'50')
        decl['sections']['Tracks']=[track()]
        with self.assertRaisesRegex(SpecError,'missing group 50'):compile_set(decl,self.base,True)

    def test_new_control_cannot_conflict_with_inherited_mapping(self):
        root=fixture();mapping=root.find('LiveSet/Transport/RecordKeyMidi')
        mapping.find('Channel').set('Value','15');mapping.find('NoteOrController').set('Value','119')
        self.base.write_bytes(gzip.compress(ET.tostring(root)))
        decl=spec();decl['sections']['Controls']=[Block('Set',props={'action':'set-locator','cc':'119','channel':'16'})]
        with self.assertRaisesRegex(SpecError,'conflicts with existing RecordKeyMidi'):
            compile_set(decl,self.base)

    def test_intention_sets_annotation_and_omission_preserves_it(self):
        root=fixture();ET.SubElement(root.find('LiveSet'),'Annotation',Value='Existing intention')
        self.base.write_bytes(gzip.compress(ET.tostring(root)))
        result=ET.fromstring(compile_set(spec(),self.base))
        self.assertEqual(result.find('LiveSet/Annotation').get('Value'),'Existing intention')
        decl=spec();decl['props']['intention']='Explore Pattern A against Pattern B & reflect.'
        result=ET.fromstring(compile_set(decl,self.base))
        self.assertEqual(result.find('LiveSet/Annotation').get('Value'),decl['props']['intention'])

    def test_wrong_type_and_missing_source_id_rejected(self):
        for node in [track('999'),track('24')]:
            decl=spec();decl['sections']['Tracks']=[node]
            with self.assertRaises(SpecError):self.compile(decl,True)

    def test_tempo_names_arm_and_native_midi_channel(self):
        decl=spec();decl['sections']={'Tracks':[track(arm='true',monitor='off',color='12')],
            'Controls':[Block('Set',props={'action':'set-locator','cc':'118','channel':'16'})]}
        live=self.compile(decl,True)
        self.assertEqual(live.find('MasterTrack/DeviceChain/Mixer/Tempo/Manual').get('Value'),'96')
        self.assertEqual(live.find('Tracks/AudioTrack/Name/EffectiveName').get('Value'),'Pattern A Audio')
        self.assertEqual(live.find('Tracks/AudioTrack/DeviceChain/MainSequencer/Recorder/IsArmed').get('Value'),'true')
        self.assertEqual(live.find('Locators/SetLocatorMapping/Channel').get('Value'),'15')
        self.assertEqual(live.find('Locators/SetLocatorMapping/PersistentKeyString').get('Value'),'k')

    def test_locator_bar_conversion_and_scene_names(self):
        decl=spec();decl['sections']={'Locators':[Block('Intro',props={'bar':'1'}),Block('Explore',props={'bar':'17'})],
                                     'Scenes':[Block('Opening',props={'scene-key':'opening'})]}
        live=self.compile(decl,True)
        self.assertEqual([e.find('Time').get('Value') for e in live.find('Locators/Locators')],['0','64'])
        self.assertEqual(live.find('Scenes/Scene/Name').get('Value'),'Opening')
        with self.assertRaisesRegex(SpecError,'replacing existing locators'):
            self.compile(decl)

    def test_malformed_fields_duplicate_controls_and_nonfinite_numbers(self):
        for props in [{'tempo':'NaN'}, {'time-signature':'7/8'}, {'spec-version':'2'}, {'typo':'yes'}]:
            decl=spec();decl['props'].update(props)
            with self.assertRaises(SpecError):validate(decl)
        decl=spec();c=Block('Record',props={'action':'record','cc':'119','channel':'16'})
        decl['sections']['Controls']=[c,copy.deepcopy(c)]
        with self.assertRaisesRegex(SpecError,'duplicate control'):validate(decl)
        decl=spec();decl['sections']['Tracks']=[track(arm='yes')]
        with self.assertRaises(SpecError):validate(decl)
        with self.assertRaisesRegex(SpecError,'duplicate property'):
            parse_page('- Ableton Session\n  tempo:: 96\n  tempo:: 120')

    def test_version_rejected(self):
        r=fixture();r.set('Creator','Ableton Live 12.1')
        self.base.write_bytes(gzip.compress(ET.tostring(r)))
        with self.assertRaisesRegex(SpecError,'Live 11'):
            compile_set(spec(),self.base)

    def test_inheritance_merges_properties_and_replaces_whole_sections(self):
        pages=self.root/'pages';pages.mkdir()
        (pages/'Template.md').write_text('- Ableton Session\n  spec-version:: 1\n  live-version:: 11\n  tempo:: 120\n  - Scenes\n    - Old\n      scene-key:: old\n  - Controls\n    - Record\n      action:: record\n      cc:: 119\n      channel:: 16\n')
        (pages/'Episode.md').write_text('ableton-template:: [[Template]]\n- # Today\n\t- Ableton Session\n\t  tempo:: 96\n\t\t- Scenes\n\t\t\t- New\n\t\t\t  scene-key:: new\n')
        decl=load_spec(self.root,'Episode');validate(decl)
        self.assertEqual(decl['props']['tempo'],'96')
        self.assertEqual([b.label for b in decl['sections']['Scenes']],['New'])
        self.assertEqual(len(decl['sections']['Controls']),1)

    def test_inheritance_cycle_and_missing_page_rejected(self):
        pages=self.root/'pages';pages.mkdir()
        (pages/'Loop.md').write_text('ableton-template:: [[Loop]]\n')
        with self.assertRaisesRegex(SpecError,'cycle'):load_spec(self.root,'Loop')
        with self.assertRaisesRegex(SpecError,'not found'):load_spec(self.root,'Absent')

    def test_output_exclusive_and_dry_run(self):
        output=self.root/'new.als'
        xml=compile_set(spec(),self.base)
        write_new(output,xml)
        first=output.read_bytes()
        with self.assertRaisesRegex(SpecError,'already exists'):write_new(output,xml)
        self.assertEqual(output.read_bytes(),first)
        self.assertEqual(gzip.decompress(first),xml)
        pages=self.root/'pages';pages.mkdir()
        (pages/'Demo.md').write_text('- Ableton Session\n  spec-version:: 1\n  live-version:: 11\n')
        preview=self.root/'preview.als'
        self.assertEqual(main(['--garden',str(self.root),'--page','Demo','--base-template',str(self.base),'--output',str(preview)]),0)
        self.assertFalse(preview.exists())


if __name__=='__main__':
    unittest.main()
