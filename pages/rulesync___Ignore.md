- [Rulesync Combined gitignore rules](https://rulesync.dyoshikawa.com/reference/file-formats.html#rulesync-aiignore-or-rulesyncignore)
	- Rulesync supports a single ignore list that can live in either location below:
	- `.rulesync/.aiignore` (recommended)
	- `.rulesyncignore` (project root)
	  
	  Rules and behavior:
	- You may use either location.
	- When both exist, Rulesync prefers `.rulesync/.aiignore` (recommended) over `.rulesyncignore` (legacy) when reading.
	- If neither file exists yet, Rulesync defaults to creating `.rulesync/.aiignore`.
	  
	  Notes:
	- Running `rulesync init` will create `.rulesync/.aiignore` if no ignore file is present.
	  
	  Example:
	  
	  ```
	  tmp/
	  credentials/
	  ```