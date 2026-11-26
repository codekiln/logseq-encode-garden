{
	"patcher": {
		"fileversion": 1,
		"appversion": {
			"major": 9,
			"minor": 0,
			"revision": 4,
			"architecture": "x64",
			"modernui": 1
		},
		"classnamespace": "box",
		"rect": [
			100.0,
			100.0,
			780.0,
			560.0
		],
		"openrect": [
			0.0,
			0.0,
			0.0,
			169.0
		],
		"bglocked": 0,
		"openinpresentation": 1,
		"default_fontsize": 10.0,
		"default_fontface": 0,
		"default_fontname": "Arial Bold",
		"gridonopen": 1,
		"gridsize": [
			8.0,
			8.0
		],
		"gridsnaponopen": 1,
		"objectsnaponopen": 1,
		"statusbarvisible": 2,
		"toolbarvisible": 1,
		"boxanimatetime": 500,
		"enablehscroll": 1,
		"enablevscroll": 1,
		"devicewidth": 150.0,
		"description": "Collects digits from Launchpad Custom Mode 3 and sends the MicroFreak a bank select and Program Change on Enter.",
		"digest": "",
		"tags": "",
		"style": "",
		"subpatcher_template": "",
		"boxes": [
			{
				"box": {
					"id": "obj-1",
					"maxclass": "newobj",
					"text": "midiin",
					"numinlets": 1,
					"numoutlets": 1,
					"outlettype": [
						"int"
					],
					"patching_rect": [
						30.0,
						20.0,
						40.0,
						22.0
					]
				}
			},
			{
				"box": {
					"id": "obj-2",
					"maxclass": "v8.codebox",
					"code": "// MF Number Pad: Launchpad Custom Mode 3 sends notes 60 to 69 for the digits 0 to 9,\n// 70 for Clear and 71 for Enter. Enter sends the MicroFreak CC 0 = (N - 1) // 128,\n// then Program Change (N - 1) % 128, for slot N from 1 to 512.\n// Every note-on, note-off and poly pressure is kept from the output. Other MIDI passes through.\ninlets = 1;\noutlets = 3; // 0: MIDI bytes to midiout, 1: typed number display, 2: last slot display\n\nvar FIRST_DIGIT = 60;\nvar CLEAR = 70;\nvar ENTER = 71;\nvar LAST_SLOT = 512;\n\nvar typed = \"\";\nvar status = 0;\nvar data = [];\nvar sysex = null;\n\nfunction dataLength(s) {\n\tif (s < 0xc0 || (s >= 0xe0 && s < 0xf0)) return 2;\n\tif (s < 0xe0) return 1;\n\tif (s === 0xf1 || s === 0xf3) return 1;\n\tif (s === 0xf2) return 2;\n\treturn 0;\n}\n\nfunction msg_int(b) {\n\tb = b & 0xff;\n\tif (b >= 0xf8) {\n\t\toutlet(0, b);\n\t\treturn;\n\t}\n\tif (sysex !== null) {\n\t\tif (b < 0x80) {\n\t\t\tsysex.push(b);\n\t\t\treturn;\n\t\t}\n\t\tif (b === 0xf7) {\n\t\t\tsysex.push(b);\n\t\t\toutlet(0, sysex);\n\t\t\tsysex = null;\n\t\t\treturn;\n\t\t}\n\t\toutlet(0, sysex);\n\t\tsysex = null;\n\t}\n\tif (b === 0xf0) {\n\t\tsysex = [b];\n\t\tstatus = 0;\n\t\tdata = [];\n\t\treturn;\n\t}\n\tif (b >= 0x80) {\n\t\tdata = [];\n\t\tif (dataLength(b) === 0) {\n\t\t\toutlet(0, b);\n\t\t\tstatus = 0;\n\t\t\treturn;\n\t\t}\n\t\tstatus = b;\n\t\treturn;\n\t}\n\tif (status === 0) {\n\t\toutlet(0, b);\n\t\treturn;\n\t}\n\tdata.push(b);\n\tif (data.length < dataLength(status)) return;\n\thandle(status, data);\n\tdata = [];\n\tif (status >= 0xf0) status = 0;\n}\n\nfunction handle(s, d) {\n\tvar type = s & 0xf0;\n\tif (type === 0x80 || type === 0x90 || type === 0xa0) {\n\t\tif (type === 0x90 && d[1] > 0) press(d[0]);\n\t\treturn;\n\t}\n\toutlet(0, [s].concat(d));\n}\n\nfunction press(note) {\n\tif (note >= FIRST_DIGIT && note < FIRST_DIGIT + 10) {\n\t\tif (typed.length < 3) typed += String(note - FIRST_DIGIT);\n\t\tshowTyped();\n\t} else if (note === CLEAR) {\n\t\ttyped = \"\";\n\t\tshowTyped();\n\t} else if (note === ENTER) {\n\t\tenter();\n\t}\n}\n\nfunction enter() {\n\tvar slot = typed === \"\" ? 0 : parseInt(typed, 10);\n\ttyped = \"\";\n\tshowTyped();\n\tif (slot < 1 || slot > LAST_SLOT) return;\n\toutlet(0, [0xb0, 0, Math.floor((slot - 1) / 128)]);\n\toutlet(0, [0xc0, (slot - 1) % 128]);\n\toutlet(2, \"set\", \"Sent: \" + slot);\n}\n\nfunction showTyped() {\n\toutlet(1, \"set\", \"Slot: \" + (typed === \"\" ? \"-\" : typed));\n}\n",
					"filename": "none",
					"fontface": 0,
					"fontname": "<Monospaced>",
					"fontsize": 10.0,
					"linenumbers": 0,
					"numinlets": 1,
					"numoutlets": 3,
					"outlettype": [
						"",
						"",
						""
					],
					"patching_rect": [
						30.0,
						60.0,
						560.0,
						420.0
					],
					"saved_object_attributes": {
						"parameter_enable": 0
					}
				}
			},
			{
				"box": {
					"id": "obj-3",
					"maxclass": "newobj",
					"text": "midiout",
					"numinlets": 1,
					"numoutlets": 0,
					"patching_rect": [
						30.0,
						500.0,
						47.0,
						22.0
					]
				}
			},
			{
				"box": {
					"id": "obj-4",
					"maxclass": "live.comment",
					"text": "MF Number Pad",
					"textjustification": 0,
					"numinlets": 1,
					"numoutlets": 0,
					"patching_rect": [
						620.0,
						20.0,
						120.0,
						18.0
					],
					"presentation": 1,
					"presentation_rect": [
						8.0,
						8.0,
						130.0,
						18.0
					]
				}
			},
			{
				"box": {
					"id": "obj-5",
					"maxclass": "live.comment",
					"text": "Slot: -",
					"textjustification": 0,
					"fontsize": 16.0,
					"numinlets": 1,
					"numoutlets": 0,
					"patching_rect": [
						300.0,
						500.0,
						130.0,
						26.0
					],
					"presentation": 1,
					"presentation_rect": [
						8.0,
						40.0,
						130.0,
						26.0
					]
				}
			},
			{
				"box": {
					"id": "obj-6",
					"maxclass": "live.comment",
					"text": "Sent: -",
					"textjustification": 0,
					"fontsize": 12.0,
					"numinlets": 1,
					"numoutlets": 0,
					"patching_rect": [
						450.0,
						500.0,
						130.0,
						20.0
					],
					"presentation": 1,
					"presentation_rect": [
						8.0,
						76.0,
						130.0,
						20.0
					]
				}
			}
		],
		"lines": [
			{
				"patchline": {
					"source": [
						"obj-1",
						0
					],
					"destination": [
						"obj-2",
						0
					]
				}
			},
			{
				"patchline": {
					"source": [
						"obj-2",
						0
					],
					"destination": [
						"obj-3",
						0
					]
				}
			},
			{
				"patchline": {
					"source": [
						"obj-2",
						1
					],
					"destination": [
						"obj-5",
						0
					]
				}
			},
			{
				"patchline": {
					"source": [
						"obj-2",
						2
					],
					"destination": [
						"obj-6",
						0
					]
				}
			}
		],
		"dependency_cache": [],
		"latency": 0,
		"project": {
			"version": 1,
			"creationdate": 3590052786,
			"modificationdate": 3590052786,
			"viewrect": [
				0.0,
				0.0,
				300.0,
				500.0
			],
			"autoorganize": 1,
			"hideprojectwindow": 1,
			"showdependencies": 1,
			"autolocalize": 0,
			"contents": {
				"patchers": {}
			},
			"layout": {},
			"searchpath": {},
			"detailsvisible": 0,
			"amxdtype": 1835887981,
			"readonly": 0,
			"devpathtype": 0,
			"devpath": ".",
			"sortmode": 0,
			"viewmode": 0
		},
		"autosave": 0
	}
}
