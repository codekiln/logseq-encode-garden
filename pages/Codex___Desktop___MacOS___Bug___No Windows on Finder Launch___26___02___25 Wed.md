- [[2026-02-25 Wed]]
	- After double clicking on dock icon, it bounced and then app failed to launch some minutes later
	- Started it from the command line, saw a few errors before it crashed.
		- ```
		  [git] git.command.complete argsCount=4 failureReason=abortedBeforeStart isRemote=false requestId=6ec90bfd subcommand=rev-parse success=false
		  [git-repo-watcher] Starting git repo watcher
		  [git] git.command.complete aborted=false allowedNonZeroExitCodes=undefined command="git --no-optional-locks config --get remote.upstream.url" commandArgs=["git","--no-optional-locks","config","--get","remote.upstream.url"] cwd=/Users/pnore/Documents/GitHub/codekiln/beans durationMs=14 exitCode=1 failureReason=command_failed id=70b9ea81 isRemote=false startTimeMs=1772012487694 subcommand=config timedOut=false
		  [sparkle] Sparkle installUpdatesIfAvailable requested.
		  (node:77534) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
		  (Use `Codex --trace-deprecation ...` to show where the warning was created)
		  [worker-manager] Worker exited code=1
		  [IpcRouter] Socket error errorCode=EPIPE errorMessage="write EPIPE" errorName=Error errorStack="Error: write EPIPE\n    at afterWriteDispatched (node:internal/stream_base_commons:159:15)\n    at writeGeneric (node:internal/stream_base_commons:150:3)\n    at Socket._writeGeneric (node:net:966:11)\n    at Socket._write (node:net:978:8)\n    at writeOrBuffer (node:internal/streams/writable:570:12)\n    at _write (node:internal/streams/writable:499:10)\n    at Writable.write (node:internal/streams/writable:508:10)\n    at Mt (/Applications/Codex.app/Contents/Resources/app.asar/.vite/build/main-Bs98CzMV.js:419:1778)\n    at z7.broadcastClientStatus (/Applications/Codex.app/Contents/Resources/app.asar/.vite/build/main-Bs98CzMV.js:419:6877)\n    at z7.unregisterClient (/Applications/Codex.app/Contents/Resources/app.asar/.vite/build/main-Bs98CzMV.js:419:5962)"
		  ```
	- it was open just long enough to see that update was available.
	- Used [[MacOS/Activity/Monitor]] to see that a process was still up; tried to quit, didn't respond. Force quit.
	- Removed version in `/Applications/Codex.app`, redownloaded, re-added.
	- Again, same issue. after double clicking on icon, it bounced for a few minutes and then app failed to launch.
	- Opening up [[MacOS/Activity/Monitor]] and after searching, saw `Codex (Not Responding)`
	- took [[MacOS/Activity/Monitor/Sample]]; didn't see anything useful.
	- Restarted from command line, then it worked from command line.
	-