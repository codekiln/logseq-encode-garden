#!/usr/bin/env python3
"""Compile the documented Logseq Ableton Session subset using an existing Live 11 Set."""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field


class SpecError(ValueError):
    pass


@dataclass
class Block:
    label: str
    indent: int = -1
    props: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


def put(props, key, value, context):
    if key in props:
        raise SpecError(f"{context}: duplicate property {key}")
    props[key] = value


def parse_page(text):
    root = Block("page")
    stack = [root]
    in_code = False
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.expandtabs(4)
        stripped = line.strip()
        if stripped.lstrip('- ').startswith(('~~~', '```')):
            in_code = not in_code
            continue
        if in_code or not stripped:
            continue
        indent = len(line) - len(line.lstrip())
        bullet = re.match(r"^\s*-\s+(.*)$", line)
        prop = re.match(r"^\s*([a-z][a-z0-9-]*)::\s*(.*?)\s*$", line)
        if bullet:
            while stack[-1].indent >= indent:
                stack.pop()
            node = Block(bullet.group(1).strip(), indent)
            stack[-1].children.append(node)
            stack.append(node)
        elif prop:
            while len(stack) > 1 and stack[-1].indent >= indent:
                stack.pop()
            put(stack[-1].props, prop.group(1), prop.group(2), f"line {number}")
    return root


def heading(label):
    return label.lstrip('# ').strip()


def page_path(garden, page):
    if page.endswith('.md') or page.startswith('/'):
        path = Path(page).expanduser().resolve()
    else:
        if any(part in ('', '.', '..') for part in page.split('/')):
            raise SpecError("invalid logical page name")
        path = garden / 'pages' / (page.replace('/', '___') + '.md')
    if not path.is_file():
        raise SpecError(f"page not found: {path}")
    return path


def load_spec(garden, page, seen=None):
    seen = set() if seen is None else seen
    path = page_path(garden, page).resolve()
    if path in seen:
        raise SpecError(f"template inheritance cycle: {path}")
    seen.add(path)
    tree = parse_page(path.read_text())
    props, sections, sources = {}, {}, []
    parent = tree.props.get('ableton-template')
    if parent:
        match = re.fullmatch(r'\[\[([^\[\]]+)\]\]', parent)
        if not match:
            raise SpecError("ableton-template must contain one [[Page]] link")
        inherited = load_spec(garden, match.group(1), seen)
        props.update(inherited['props'])
        sections.update(inherited['sections'])
        sources.extend(inherited['sources'])
    sessions = []
    def visit(node):
        if heading(node.label) == 'Ableton Session':
            sessions.append(node)
        for child in node.children:
            visit(child)
    visit(tree)
    if len(sessions) > 1:
        raise SpecError(f"{path}: more than one Ableton Session block")
    if sessions:
        session = sessions[0]
        props.update(session.props)
        names = set()
        for child in session.children:
            name = heading(child.label)
            if name not in ('Tracks', 'Scenes', 'Locators', 'Controls'):
                raise SpecError(f"unsupported section: {name}")
            if name in names:
                raise SpecError(f"duplicate section: {name}")
            names.add(name)
            sections[name] = child.children
    if not sessions and not parent:
        raise SpecError(f"{path}: no Ableton Session or ableton-template")
    sources.append(str(path))
    return {'props': props, 'sections': sections, 'sources': sources}


def integer(value, minimum, maximum, context):
    try:
        result = int(value)
    except (TypeError, ValueError):
        raise SpecError(f"{context}: expected integer") from None
    if not minimum <= result <= maximum:
        raise SpecError(f"{context}: expected {minimum}..{maximum}")
    return result


def number(value, minimum, maximum, context):
    try:
        result = float(value)
    except (TypeError, ValueError):
        raise SpecError(f"{context}: expected number") from None
    if not math.isfinite(result) or not minimum <= result <= maximum:
        raise SpecError(f"{context}: expected finite number {minimum}..{maximum}")
    return result


def require_props(node, required, allowed):
    missing = set(required) - node.props.keys()
    unknown = node.props.keys() - set(allowed)
    if missing:
        raise SpecError(f"{node.label}: missing {', '.join(sorted(missing))}")
    if unknown:
        raise SpecError(f"{node.label}: unsupported properties {', '.join(sorted(unknown))}")
    if node.children:
        raise SpecError(f"{node.label}: nested item blocks are unsupported")


def validate(spec):
    p = spec['props']
    allowed = {'spec-version', 'live-version', 'base-template', 'tempo', 'time-signature', 'intention'}
    if p.keys() - allowed:
        raise SpecError(f"unsupported session properties: {', '.join(sorted(p.keys() - allowed))}")
    if p.get('spec-version') != '1' or p.get('live-version') != '11':
        raise SpecError("spec-version must be 1 and live-version must be 11")
    if 'tempo' in p:
        number(p['tempo'], 20, 999, 'tempo')
    if p.get('time-signature', '4/4') != '4/4':
        raise SpecError("this compiler currently supports time-signature 4/4")
    keys, ids = set(), set()
    for t in spec['sections'].get('Tracks', []):
        require_props(t, ('track-key', 'source-track-id', 'type'),
                      ('track-key', 'source-track-id', 'type', 'color', 'monitor', 'arm',
                       'audio-from', 'audio-to', 'midi-from', 'midi-to'))
        key = t.props['track-key']
        tid = integer(t.props['source-track-id'], 0, 2147483647, 'source-track-id')
        if not key or key in keys or tid in ids:
            raise SpecError(f"{t.label}: duplicate or empty track-key/source-track-id")
        keys.add(key); ids.add(tid)
        if t.props['type'] not in ('audio', 'midi', 'return', 'group'):
            raise SpecError(f"{t.label}: invalid track type")
        if t.props.get('monitor', 'auto') not in ('in', 'auto', 'off'):
            raise SpecError(f"{t.label}: monitor must be in, auto, or off")
        if t.props.get('arm', 'false') not in ('true', 'false'):
            raise SpecError(f"{t.label}: arm must be true or false")
        if 'color' in t.props:
            integer(t.props['color'], 0, 69, 'track color')
    keys = set()
    for s in spec['sections'].get('Scenes', []):
        require_props(s, ('scene-key',), ('scene-key', 'color'))
        if not s.props['scene-key'] or s.props['scene-key'] in keys:
            raise SpecError("duplicate or empty scene-key")
        keys.add(s.props['scene-key'])
        if 'color' in s.props:
            integer(s.props['color'], 0, 69, 'scene color')
    for loc in spec['sections'].get('Locators', []):
        require_props(loc, (), ('bar', 'beats'))
        if len(loc.props) != 1:
            raise SpecError(f"{loc.label}: declare either bar or beats")
        if 'bar' in loc.props:
            integer(loc.props['bar'], 1, 2147483647, 'locator bar')
        else:
            number(loc.props['beats'], 0, 1e12, 'locator beats')
    actions, messages = set(), set()
    for c in spec['sections'].get('Controls', []):
        require_props(c, ('action', 'cc', 'channel'), ('action', 'cc', 'channel'))
        action = c.props['action']
        if action not in ('record', 'set-locator', 'previous-locator', 'next-locator'):
            raise SpecError(f"unsupported control action: {action}")
        msg = (integer(c.props['channel'], 1, 16, 'control channel'),
               integer(c.props['cc'], 0, 127, 'control cc'))
        if action in actions or msg in messages:
            raise SpecError("duplicate control action or MIDI message")
        actions.add(action); messages.add(msg)


def set_value(parent, path, value):
    elem = parent.find(path) if parent is not None else None
    if elem is None:
        raise SpecError(f"base Set lacks required element {path}")
    elem.set('Value', str(value))


def clear_fresh(live):
    # Clear recorded content only. Devices may have their own Events/Envelopes;
    # those are part of the sound and must survive template specialization.
    tracks = list(live.find('Tracks'))
    tracks.extend(x for x in (live.find('MasterTrack'), live.find('PreHearTrack')) if x is not None)
    for track in tracks:
        for path in ('AutomationEnvelopes/Envelopes', 'TakeLanes/TakeLanes'):
            content = track.find(path)
            if content is not None:
                content[:] = []
        for tag in ('MainSequencer', 'FreezeSequencer'):
            seq = track.find('DeviceChain/' + tag)
            if seq is None:
                continue
            for events in seq.findall('.//ArrangerAutomation/Events'):
                events[:] = []
            for value in seq.findall('ClipSlotList/ClipSlot/ClipSlot/Value'):
                value[:] = []
            for key, value in [('LastSelectedTimeableIndex', '0'), ('Recorder/TakeCounter', '0')]:
                elem = seq.find(key)
                if elem is not None:
                    elem.set('Value', value)
        for key, value in [('SavedPlayingSlot','-1'), ('SavedPlayingOffset','0')]:
            elem = track.find(key)
            if elem is not None:
                elem.set('Value', value)
    locs = live.find('Locators/Locators')
    if locs is not None:
        locs[:] = []
    transport = live.find('Transport')
    if transport is not None:
        for key, value in [('CurrentTime', '0'), ('LoopOn', 'false'), ('LoopStart', '0'),
                           ('LoopLength', '16'), ('PunchIn', 'false'), ('PunchOut', 'false')]:
            if transport.find(key) is not None:
                set_value(transport, key, value)


def validate_references(live):
    tracks = live.find('Tracks')
    ids = {t.get('Id') for t in tracks}
    for track in tracks:
        gid = track.find('TrackGroupId')
        if gid is not None and gid.get('Value') not in ids | {'-1'}:
            raise SpecError(f"track {track.get('Id')} refers to missing group {gid.get('Value')}")
    for node in live.iter('Target'):
        match = re.search(r'(?:Audio|Midi)(?:In|Out)/Track\.(\d+)/', node.get('Value', ''))
        if match and match.group(1) not in ids:
            raise SpecError(f"routing refers to missing track {match.group(1)}")


def compile_set(spec, base, fresh=False):
    validate(spec)
    try:
        root = ET.fromstring(gzip.decompress(Path(base).read_bytes()))
    except (OSError, EOFError, ET.ParseError) as exc:
        raise SpecError(f"cannot read base Set: {exc}") from exc
    if not root.get('Creator', '').startswith('Ableton Live 11.'):
        raise SpecError("base Set must have been saved by Ableton Live 11")
    live = root.find('LiveSet')
    if live is None or live.find('Tracks') is None:
        raise SpecError("base Set has no LiveSet/Tracks")
    if fresh:
        clear_fresh(live)
    tracks = live.find('Tracks')
    selected = spec['sections'].get('Tracks')
    if selected is not None:
        by_id = {t.get('Id'): t for t in tracks}
        wanted = {t.props['source-track-id'] for t in selected}
        unknown = wanted - by_id.keys()
        if unknown:
            raise SpecError(f"source track IDs missing from base: {', '.join(sorted(unknown))}")
        removed = [t for t in tracks if t.get('Id') not in wanted and t.tag != 'ReturnTrack']
        if removed and not fresh:
            raise SpecError("Tracks omits base tracks; pruning requires --fresh")
        for t in removed:
            tracks.remove(t)
        for declaration in selected:
            p = declaration.props
            track = by_id[p['source-track-id']]
            expected = {'audio':'AudioTrack','midi':'MidiTrack','return':'ReturnTrack','group':'GroupTrack'}[p['type']]
            if track.tag != expected:
                raise SpecError(f"{declaration.label}: source track has type {track.tag}, expected {expected}")
            for name in ('EffectiveName', 'UserName'):
                set_value(track, f'Name/{name}', declaration.label)
            if 'color' in p:
                set_value(track, 'Color', p['color'])
            seq = track.find('DeviceChain/MainSequencer')
            if 'monitor' in p:
                set_value(seq, 'MonitoringEnum', {'in':0, 'auto':1, 'off':2}[p['monitor']])
            if 'arm' in p:
                set_value(seq, 'Recorder/IsArmed', p['arm'])
            for key, tag in [('audio-from','AudioInputRouting'),('audio-to','AudioOutputRouting'),
                             ('midi-from','MidiInputRouting'),('midi-to','MidiOutputRouting')]:
                if key in p:
                    prefix = {'audio-from':'AudioIn/', 'audio-to':'AudioOut/',
                              'midi-from':'MidiIn/', 'midi-to':'MidiOut/'}[key]
                    if not p[key].startswith(prefix):
                        raise SpecError(f"{key} must be a native {prefix} target")
                    set_value(track, f'DeviceChain/{tag}/Target', p[key])
                    # Live resolves these display strings from Target when opening.
                    routing = track.find(f'DeviceChain/{tag}')
                    target_match = re.search(r'/Track\.(\d+)/', p[key])
                    target_track = by_id.get(target_match.group(1)) if target_match else None
                    display = target_track.find('Name/EffectiveName').get('Value') if target_track is not None else p[key].split('/',1)[1]
                    set_value(routing, 'UpperDisplayString', display)
                    set_value(routing, 'LowerDisplayString', 'Track In' if target_match else '')
    # Names may change after a source track's routing was applied. Refresh all
    # retained internal routing labels after every rename is complete.
    retained = {t.get('Id'): t for t in tracks}
    for track in tracks:
        for tag in ('AudioInputRouting', 'AudioOutputRouting', 'MidiInputRouting', 'MidiOutputRouting'):
            routing = track.find('DeviceChain/' + tag)
            if routing is None:
                continue
            target = routing.find('Target')
            match = re.search(r'/Track\.(\d+)/', target.get('Value', '')) if target is not None else None
            if match and match.group(1) in retained:
                set_value(routing, 'UpperDisplayString', retained[match.group(1)].find('Name/EffectiveName').get('Value'))
    if 'intention' in spec['props']:
        set_value(live, 'Annotation', spec['props']['intention'])
    master = live.find('MasterTrack/DeviceChain/Mixer')
    if 'tempo' in spec['props']:
        set_value(master, 'Tempo/Manual', spec['props']['tempo'])
    if 'time-signature' in spec['props']:
        set_value(master, 'TimeSignature/Manual', '201')
    scenes = spec['sections'].get('Scenes')
    if scenes is not None:
        existing = list(live.find('Scenes'))
        if len(scenes) > len(existing):
            raise SpecError("scene declaration exceeds existing template scene slots")
        for scene, declaration in zip(existing, scenes):
            set_value(scene, 'Name', declaration.label)
            if 'color' in declaration.props:
                set_value(scene, 'Color', declaration.props['color'])
    locators = spec['sections'].get('Locators')
    if locators is not None:
        container = live.find('Locators/Locators')
        if container is None:
            raise SpecError("base Set lacks Locators/Locators")
        if len(container) and not fresh:
            raise SpecError("replacing existing locators requires --fresh")
        container[:] = []
        for index, loc in enumerate(locators):
            beat = (int(loc.props['bar']) - 1) * 4 if 'bar' in loc.props else float(loc.props['beats'])
            node = ET.SubElement(container, 'Locator', Id=str(index))
            for key, value in [('LomId','0'),('Time',format(beat,'.15g')),('Name',loc.label),
                               ('Annotation',''),('IsSongStart','false')]:
                ET.SubElement(node, key, Value=value)
    paths = {'record':'Transport/RecordKeyMidi', 'set-locator':'Locators/SetLocatorMapping',
             'previous-locator':'Locators/PreviousLocatorMapping', 'next-locator':'Locators/NextLocatorMapping'}
    for control in spec['sections'].get('Controls', []):
        mapping = live.find(paths[control.props['action']])
        if mapping is None:
            raise SpecError(f"base lacks mapping for {control.props['action']}")
        for key,value in [('IsNote','false'),('Channel',str(int(control.props['channel'])-1)),
                          ('NoteOrController',control.props['cc']),('LowerRangeNote','-1'),
                          ('UpperRangeNote','-1'),('ControllerMapMode','0')]:
            set_value(mapping,key,value)
    # Reject collisions with mappings inherited from the seed as well as
    # collisions among newly declared controls. Live would trigger both targets.
    for control in spec['sections'].get('Controls', []):
        mapping = live.find(paths[control.props['action']])
        message = (mapping.find('Channel').get('Value'), mapping.find('NoteOrController').get('Value'))
        for other in live.iter():
            if other is mapping:
                continue
            channel, cc, note = other.find('Channel'), other.find('NoteOrController'), other.find('IsNote')
            if channel is not None and cc is not None and note is not None:
                if note.get('Value') == 'false' and (channel.get('Value'), cc.get('Value')) == message:
                    raise SpecError(f"{control.label}: MIDI message conflicts with existing {other.tag} mapping")
    validate_references(live)
    if fresh and (live.findall('.//AudioClip') or live.findall('.//MidiClip')):
        raise SpecError("fresh output still contains clips")
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


def write_new(output, xml):
    output = Path(output)
    if output.suffix.lower() != '.als':
        raise SpecError("output must have .als extension")
    # Exclusive creation protects existing performances even if they appear after preview.
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output.open('xb') as raw:
            with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as stream:
                stream.write(xml)
    except FileExistsError:
        raise SpecError(f"output already exists: {output}; choose a new filename") from None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--garden', type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument('--page', required=True)
    parser.add_argument('--base-template', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--fresh', action='store_true', help='clear all clips, take lanes, automation and locators in the new copy')
    parser.add_argument('--apply', action='store_true', help='write the validated new Set; otherwise preview')
    args = parser.parse_args(argv)
    try:
        spec = load_spec(args.garden.resolve(), args.page)
        declared = spec['props'].get('base-template')
        base = args.base_template or (Path(declared).expanduser() if declared else None)
        if base is None:
            raise SpecError("declare base-template or pass --base-template")
        if not base.is_absolute():
            base = args.garden / base
        if args.output.exists():
            raise SpecError(f"output already exists: {args.output}; choose a new filename")
        xml = compile_set(spec, base, args.fresh)
        plan = {'sources':spec['sources'], 'base_template':str(base.resolve()),
                'base_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),
                'output':str(args.output.resolve()), 'fresh':args.fresh,
                'tracks':[b.label for b in spec['sections'].get('Tracks',[])],
                'scenes':[b.label for b in spec['sections'].get('Scenes',[])],
                'locators':[b.label for b in spec['sections'].get('Locators',[])],
                'intention':spec['props'].get('intention'), 'applied':args.apply}
        if args.apply:
            write_new(args.output,xml)
        print(json.dumps(plan,indent=2))
        return 0
    except (SpecError,OSError) as exc:
        print(f"error: {exc}",file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
