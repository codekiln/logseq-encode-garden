alias:: [[JSON5]]

- # [JSON5 – JSON for Humans | JSON5](https://json5.org/)
	- ## About
	  id:: 67c822b0-3271-41da-a14f-4f023a1f4556
		- extension to [[json]] that **aims to be easier to write and maintain by hand (e.g. for config files)**. ([[Code/Comments]] allowed)
		- superset of [[json]]; valid JSON files will always be valid JSON5 files
			- a subset of [[ES5]]; valid JSON5 files will always be valid ES5
			- expands its syntax to include some productions from [ECMAScript 5.1](https://www.ecma-international.org/ecma-262/5.1/) (ES5).
	- ## #Example
		- ```json5
		  {
		    // comments
		    unquoted: 'and you can quote me on that',
		    singleQuotes: 'I can use "double quotes" here',
		    lineBreaks: "Look, Mom! \
		  No \\n's!",
		    hexadecimal: 0xdecaf,
		    leadingDecimalPoint: .8675309, andTrailing: 8675309.,
		    positiveSign: +1,
		    trailingComma: 'in objects', andIn: ['arrays',],
		    "backwardsCompatible": "with JSON",
		  }
		  ```
	- started in [[2012]], and as of [[2022]], gets [>65M downloads/week](https://www.npmjs.com/package/json5), ranks in the [top 0.1%](https://gist.github.com/anvaka/8e8fa57c7ee1350e3491) of the most depended-upon packages on npm, and has been adopted by major projects like [Chromium](https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/platform/runtime_enabled_features.json5;drc=5de823b36e68fd99009a29281b17bc3a1d6b329c), [Next.js](https://github.com/vercel/next.js/blob/b88f20c90bf4659b8ad5cb2a27956005eac2c7e8/packages/next/lib/find-config.ts#L43-L46), [Babel](https://babeljs.io/docs/en/config-files#supported-file-extensions), [Retool](https://community.retool.com/t/i-am-attempting-to-append-several-text-fields-to-a-google-sheet-but-receiving-a-json5-invalid-character-error/7626), [WebStorm](https://www.jetbrains.com/help/webstorm/json.html), and [more](https://github.com/json5/json5/wiki/In-the-Wild). It's also natively supported on [Apple platforms](https://developer.apple.com/documentation/foundation/jsondecoder/3766916-allowsjson5) like [[MacOS]] and [[iOS]].