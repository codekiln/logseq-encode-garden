alias:: [[Person/Viznut/Font/unscii]]
created-by:: [[Person/Viznut]]

- # [Unscii - a bitmapped Unicode font for blocky graphics](http://viznut.fi/unscii/)
	- In 2020-03-10, the new [Unicode version 13.0](http://www.unicode.org/versions/Unicode13.0.0/) added 214 graphics characters for "legacy computing" (including, among all, the missing PETSCII characters, and a majority of missing Teletext/Videotex characters). Most of these were already included in Unscii 1.x, but now I have been able to give them proper Unicode mappings as well. This is the main reason for the Unscii 2.0 release.
	- Additionally, Unscii 2.0 fixes errors in some characters, legibility in some others and adds a bunch of new ones.
	- A test picture representing what is currently available in Unicode (feel free to copy-paste it to your editor to see what it looks like in other fonts):
	- ```
	  ╎┆┊  ╱🭽▔🭾╲    🮲🮳       🮸🮀🮵🮶🮀🮁🮁🮀🮼🯁🯂🯃      ▵        ↑        ◬
	  ╶─╴╺━╸ ═ ╎┆┊ ⎹ ⎸▣⎹ ⎸  ▝▛▀▜▘ 🯲🯷🯶                   △    ▴   ╽       ◭⬘◮
	  ╷┌┬┐┍┯┑╒╤╕╏┇┋ 🮷 🭼▁🭿 ⎸  ▚▌█▐▞ 🯹🯵🯱 🯰     ▁▂▃▄▅▆▇█ ◃◅◁╳▷▻▹ ▲ ←╼╋╾→     ◩⬒⬔
	  │├┼┤┝┿┥╞╪╡╏┇┋ ⎹╱ ╳ ╲⎸  ▗▙▄▟▖ 🯴🯳🯸      █🮆🮅🮄▀🮃🮂▔⎹    ▽ ◂◄◀🮽▶►▸╿  ⮝   ⬖◧◫◨⬗
	  ╵└┴┘┕┷┙╘╧╛┞╀┦  ▔▔▔▔▔   🬑🬜🬰🬪🬟      🮞🮟 ▕▉ ◞◡◯◡ ◎🭵    ▿    ▼   ↓ ⮜◈⮞   ⬕⬓◪  
	  ╻┎┰┒┏┳┓  ┭╆╈╅┮╍╍╌╌  🬥🬦🬍🬲🬵🬹🬱🬷🬌🬓🬙   🮝🮜 🮇▊◝◠◯◉◯◡◟🭴         ▾      ⮟   ◕ ⬙ ◔
	  ┃┠╂┨┣╋┫ ╺┽╊◙╉┾┅┅┄┄  🬔🬡🬖🬻🬞🬭🬏🬺🬢🬒🬧      🮈▋◍ ◠◯◠◜ 🭳  ◿◺                     
	  ╹┖┸┚┗┻┛ ━┵╄╇╃┶┉┉┈┈  🬃🬤🬫🬴🬠🬋🬐🬸🬛🬗🬇   🭇🬼 ▐▌ ◌🮣🮢 🮦 🭲  ◹◸ 🭯 🮀⚞⚟🮀  🯊     ◙◛◶─◵
	  ╓╥╖   ╔╦╗┢╁┪ ┟┱┲┧  🬣🬯🬈🬬🬁🬂🬀🬝🬅🬮🬘   🭢🭗 🮉▍ 🮤🮪🮫🮥🮧 🭱  🭯 🭮◙🭬╭──╮⎫🮻⎧    ◘◙│◲┼◱╭◒╮
	  ║╟╫╢🮐🮒🮐╠╬╣ ╹┃ ┡┹┺┩  🬳🬉🬩🬕🬊🬎🬆🬨🬚🬄🬶   🭊🬿 🮊▎ 🮩🮬🮭🮨  🭰 ◢🭫◣ 🮚 │ ▢ ⎮🏎⎪    ◙◚◷┼◴│◑╋◐
	  ╙╨╜🮔 🮓╚╩╝   🯆 🯅  🯇     🮣🮢   🯉  🯈 🭥🭚 🮋▏🮮 🮡🮠   ⎸🭮🭪◆🭨🮛🮿🭬╰─🮯─╯⎬⎯⎨       ◳─◰╰◓╯    
	  ░░🮐🮑🮐▓▓██🮗🮗▤▤▥▥▦▦▩▩▧▧🮘🮘🮙🮙▨▨🮕🮕🮖🮖 🭋🭀 █▁🭻🭺🭹🭸🭷🭶▔  ◥🭩◤ 🭭      ⎮⯊⎪ ▱▰    ▭▬
	  ░░▒🮎▒▓▓██🮗🮗▤▤▥▥▦▦▩▩▧▧🮘🮘🮙🮙▨▨🮕🮕🮖🮖 🭦🭛         🮰 🭇🬼🭭 🭊🬿 🭋🭀   ⎭⯋⎩ ▯▮  ▫◻□■◼▪⬝·
	    🮌█🮍                 ╲╱  🭇🬼🭈🬽🭉🬾◢◣🭇🭃🭎🬼🭈🭆🭂🭍🭑🬽🭉🭁🭌🬾🭈🭄🭏🬽🭅🭐 ◦○◯⬤◖◗ ⬫⬦⬨♢◊◇◆♦⬧⬥⬩⬪
	    ▒🮏▒                     🭢🭗🭣🭘🭤🭙◥◤🭢🭔🭟🭗🭣🭧🭓🭞🭜🭘🭤🭒🭝🭙🭣🭕🭠🭘🭖🭡  ∘⭘●          
	                                               🭢🭗  🭥🭚 🭦🭛    •
	  ```
	-