logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Security/Vulnerability]]

- # What is TOCTOU?
	- ## [[AI Answer]]
		- **Short answer:** **TOCTOU** (**T**ime-**O**f-**C**heck to **T**ime-**O**f-**U**se) is a class of race-condition bug where a program checks a condition and then acts on it, but the state changes in the window between the two steps — so the action operates on something different from what was validated. It is catalogued in [[CWE]] as [CWE-367](https://cwe.mitre.org/data/definitions/367.html).
		- ### The core problem
			- The check and the use are **not atomic**. Between them, a concurrent actor (another process, thread, or user) can swap the resource out from under the program.
			- The classic exploit window is small but real, and attackers can widen it (filesystem contention, scheduler pressure) to win the race reliably.
		- ### Canonical example (filesystem)
			- A privileged program checks that a file is safe to write, then opens it:
			- ~~~c
			  if (access("/tmp/file", W_OK) == 0) {  // TIME OF CHECK: caller may write?
			      int fd = open("/tmp/file", O_WRONLY);  // TIME OF USE
			      write(fd, data, len);
			  }
			  ~~~
			- Between `access()` and `open()`, an attacker replaces `/tmp/file` with a symlink to `/etc/passwd`. The check passed on the harmless file; the write lands on the sensitive one — privilege escalation.
		- ### Why it happens
			- Checking by **name/path** and acting by **name/path** as two separate operations. The name is a stale reference; the object it points to can be re-bound in between.
			- `access()` + `open()`, `stat()` + `open()`, "check permissions then use", and check-then-create patterns are the usual culprits.
		- ### Mitigations
			- **Operate on a handle, not a name.** `open()` the resource once, then check and use *the same file descriptor* (`fstat`, `fchmod`, `openat` with `O_NOFOLLOW`). The handle can't be re-bound.
			- **Use atomic primitives.** `O_CREAT | O_EXCL` for safe creation; atomic compare-and-swap for shared memory.
			- **Drop privileges / avoid the check.** Don't use `access()` to gate a privileged operation — just attempt it as the real user and handle failure.
			- **Lock or serialize** access to the shared resource so the check and use can't be interleaved.
		- ### Beyond the filesystem
			- The pattern generalizes to any shared mutable state: database "check row then update", check-then-act on a bank balance, verifying a token then reusing it, or validating then re-reading a memory-mapped value. Also framed as a general concurrency defect (see [CWE-367](https://cwe.mitre.org/data/definitions/367.html)).
