import copy
import unittest
import xml.etree.ElementTree as ET

from compiler import SpecError
from prepare_seed import add_pattern_b, global_ids


def seed():
    root=ET.Element('Ableton',Creator='Ableton Live 11.3.43')
    live=ET.SubElement(root,'LiveSet');ET.SubElement(live,'NextPointeeId',Value='1004')
    tracks=ET.SubElement(live,'Tracks')
    group=ET.SubElement(tracks,'GroupTrack',Id='30')
    name=ET.SubElement(group,'Name')
    for tag in ['EffectiveName','UserName']:ET.SubElement(name,tag,Value='Pattern A')
    ET.SubElement(group,'Color',Value='16');ET.SubElement(group,'TrackGroupId',Value='-1')
    slots=ET.SubElement(group,'Slots')
    ET.SubElement(slots,'GroupTrackSlot',Id='0');ET.SubElement(slots,'GroupTrackSlot',Id='1')
    chain=ET.SubElement(group,'DeviceChain')
    ET.SubElement(ET.SubElement(chain,'DeviceChain'),'Devices')
    mixer=ET.SubElement(chain,'Mixer')
    ET.SubElement(mixer,'Pointee',Id='1000')
    ET.SubElement(mixer,'AutomationTarget',Id='1001')
    ET.SubElement(mixer,'ModulationTarget',Id='1002')
    ET.SubElement(mixer,'VolumeModulationTarget',Id='1003')
    ET.SubElement(ET.SubElement(mixer,'Sends'),'TrackSendHolder',Id='0')
    for tid,tag,gid in [('23','AudioTrack','30'),('24','MidiTrack','30'),('21','AudioTrack','-1'),('22','MidiTrack','-1')]:
        t=ET.SubElement(tracks,tag,Id=tid);ET.SubElement(t,'TrackGroupId',Value=gid)
        ET.SubElement(ET.SubElement(ET.SubElement(t,'DeviceChain'),'AudioOutputRouting'),'Target',Value='AudioOut/Master')
    return root


class SeedTests(unittest.TestCase):
    def test_allocates_global_ids_keeps_local_scoped_ids_and_routes(self):
        root=seed();original=copy.deepcopy(root)
        add_pattern_b(root)
        live=root.find('LiveSet');tracks=live.find('Tracks')
        self.assertEqual([t.get('Id') for t in tracks],['30','23','24','31','21','22'])
        self.assertEqual(global_ids(root),set(range(1000,1008)))
        self.assertEqual(live.find('NextPointeeId').get('Value'),'1008')
        a=tracks.find("GroupTrack[@Id='30']");b=tracks.find("GroupTrack[@Id='31']")
        self.assertEqual([e.get('Id') for e in a.find('Slots')],['0','1'])
        self.assertEqual([e.get('Id') for e in b.find('Slots')],['0','1'])
        self.assertEqual(ET.tostring(a),ET.tostring(original.find('LiveSet/Tracks/GroupTrack')))
        for tid in ['21','22']:
            track=next(t for t in tracks if t.get('Id')==tid)
            self.assertEqual(track.find('TrackGroupId').get('Value'),'31')
            self.assertEqual(track.find('DeviceChain/AudioOutputRouting/Target').get('Value'),'AudioOut/Master')

    def test_refuses_devices_unknown_ids_bad_allocator_and_duplicate_globals(self):
        for variant in ['device','unknown','allocator','duplicate']:
            root=seed();group=root.find('LiveSet/Tracks/GroupTrack')
            if variant=='device':ET.SubElement(group.find('DeviceChain/DeviceChain/Devices'),'PluginDevice',Id='1')
            if variant=='unknown':ET.SubElement(group,'UnknownObject',Id='123')
            if variant=='allocator':root.find('LiveSet/NextPointeeId').set('Value','1000')
            if variant=='duplicate':ET.SubElement(group,'Pointee',Id='1000')
            with self.subTest(variant=variant):
                with self.assertRaises(SpecError):add_pattern_b(root)


if __name__=='__main__':unittest.main()
