#!/usr/bin/env python3
"""Prepare this project's seed by copying a verified empty Live-created group.

This constrained maintenance tool is separate from the page compiler. Its input
must contain GroupTrack 30, created and saved in Live around tracks 23 and 24.
"""
import argparse
from collections import Counter
import copy
import gzip
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

from compiler import SpecError, clear_fresh, set_value, validate_references, write_new

GLOBAL_IDS = {'Pointee', 'AutomationTarget', 'ModulationTarget',
              'VolumeModulationTarget', 'TranspositionModulationTarget',
              'GrainSizeModulationTarget', 'FluxModulationTarget',
              'SampleOffsetModulationTarget'}
LOCAL_IDS = {'GroupTrackSlot', 'AutomationLane', 'TrackSendHolder'}


def global_ids(root):
    values = [int(e.get('Id')) for e in root.iter() if e.tag in GLOBAL_IDS and e.get('Id') is not None]
    duplicates = [value for value,count in Counter(values).items() if count > 1]
    if duplicates:
        raise SpecError(f'duplicate global object definitions: {duplicates}')
    return set(values)


def add_pattern_b(root):
    live = root.find('LiveSet')
    tracks = live.find('Tracks')
    group = tracks.find("GroupTrack[@Id='30']")
    if group is None:
        raise SpecError('expected Live-created Pattern A group 30')
    if any(t.get('Id') == '31' for t in tracks):
        raise SpecError('track 31 already exists')
    if group.find('DeviceChain/DeviceChain/Devices') is None or len(group.find('DeviceChain/DeviceChain/Devices')):
        raise SpecError('seed group must have an empty device chain')
    if any(len(e) for e in group.findall('.//Envelopes') + group.findall('.//Events')):
        raise SpecError('seed group must have no automation or recorded events')
    if group.findall('.//PointeeId') or group.findall('.//AutomationEnvelope'):
        raise SpecError('seed group has unexpected object references')
    for elem in group.iter():
        if 'Id' in elem.attrib and elem.tag not in GLOBAL_IDS | LOCAL_IDS | {'GroupTrack'}:
            raise SpecError(f'unsupported group object identity: {elem.tag}')
    before = global_ids(root)
    next_node = live.find('NextPointeeId')
    if next_node is None or int(next_node.get('Value')) <= max(before):
        raise SpecError('NextPointeeId must follow all existing global object definitions')
    next_id = int(next_node.get('Value'))
    cloned = copy.deepcopy(group)
    cloned.set('Id','31')
    for node in cloned.iter():
        if node.tag in GLOBAL_IDS:
            node.set('Id',str(next_id))
            next_id += 1
    next_node.set('Value',str(next_id))
    for path in ('Name/EffectiveName','Name/UserName'):
        set_value(cloned,path,'Pattern B')
    set_value(cloned,'Color','17')
    pattern_b = [tracks.find("AudioTrack[@Id='21']"), tracks.find("MidiTrack[@Id='22']")]
    if any(t is None for t in pattern_b):
        raise SpecError('expected Pattern B audio/MIDI tracks 21/22')
    if [t.get('Id') for t in list(tracks)[list(tracks).index(pattern_b[0]):][:2]] != ['21','22']:
        raise SpecError('Pattern B tracks must be adjacent in audio/MIDI order')
    for child in pattern_b:
        if child.find('TrackGroupId').get('Value') != '-1':
            raise SpecError('Pattern B child is already grouped')
        set_value(child,'TrackGroupId','31')
    tracks.insert(list(tracks).index(pattern_b[0]),cloned)
    after = global_ids(root)
    if not before < after or len(after - before) != len([e for e in group.iter() if e.tag in GLOBAL_IDS]):
        raise SpecError('global object allocation failed')
    validate_references(live)
    return root


def prepare(source):
    root = ET.fromstring(gzip.decompress(Path(source).read_bytes()))
    if not root.get('Creator','').startswith('Ableton Live 11.'):
        raise SpecError('seed must be saved by Live 11')
    add_pattern_b(root)
    live = root.find('LiveSet')
    clear_fresh(live)
    locators = live.find('Locators/Locators')
    locator = ET.SubElement(locators,'Locator',Id='0')
    for key,value in [('LomId','0'),('Time','0'),('Name','Opening'),('Annotation',''),('IsSongStart','false')]:
        ET.SubElement(locator,key,Value=value)
    global_ids(root)
    return ET.tostring(root,encoding='utf-8',xml_declaration=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('output',type=Path)
    args = parser.parse_args()
    try:
        result=prepare(args.source)
        write_new(args.output,result)
    except (SpecError,OSError,ET.ParseError) as exc:
        print(f'error: {exc}',file=sys.stderr)
        return 2
    print(f'Prepared {args.output}; validate by opening, saving and reopening in Live.')
    return 0


if __name__=='__main__':
    sys.exit(main())
