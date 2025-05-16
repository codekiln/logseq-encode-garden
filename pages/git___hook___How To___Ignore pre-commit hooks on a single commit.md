# One-time escape hatch – make a commit even though the old [[git/hook]] are broken
	- *`--no-verify` skips whatever is in `.git/hooks/pre-commit` just this once; the commit goes through so you can add the new config.*
		- `git commit --no-verify -m "chore: begin migration to pre-commit"`
-