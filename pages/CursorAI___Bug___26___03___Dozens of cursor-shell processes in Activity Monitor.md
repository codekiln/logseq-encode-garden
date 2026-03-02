# CursorAI Bug - Dozens of `cursor-shell` processes in activity monitor
	- ```
	  ps aux | grep cursor-shell | wc -l
	        26
	  ```
	- ## Cursor Shell Process Accumulation — Technical Summary
	  
	  **Observation**
	  26 `cursor-shell` processes were running despite Cursor UI being closed.
	  
	  **Initial Inspection**
	- Most processes had `PPID = 1` → orphaned and adopted by `launchd`.
	- State `S` / `Ss` → sleeping, not zombies.
	- CPU ~0%, low memory usage.
	- Multiple agent versions present:
		- `2026.02.13-41ac335`
		- `2026.02.27-e7d2ef6`
	- Backing binaries located in:
	  `~/.local/share/cursor-agent/versions/...`
	  
	  **Process Role**
	  `cursor-shell` is:
	- A Node-based PTY host
	- Backend for Cursor terminal sessions
	- Manages:
		- SQLite chat storage
		- AI tracking database
		- askpass socket
		- PTY devices
		- Workspace context
		  
		  Architecture (simplified):
		  
		  Cursor UI
		  → cursor-agent (Node backend)
		  → cursor-shell (PTY host)
		  → user shell
		  → tmux
		  
		  **Root Cause**
	- Cursor spawns agent processes per workspace/session.
	- On exit or upgrade, agents were not fully cleaned up.
	- Old agents persisted as detached orphan processes.
	- Cursor update left prior agent version processes running.
	- Over time, accumulation reached 26.
	  
	  **Why tmux Died During Cleanup**
	  Running:
	  
	  ```
	  pkill -f cursor-shell
	  ```
	  
	  Killed:
	- Orphaned agents (expected)
	- Active `cursor-shell` backing a live tmux PTY (unexpected)
	  
	  Since tmux depended on that PTY host, killing it terminated the controlling terminal → tmux exited.
	  
	  This was expected Unix behavior, not corruption.
	  
	  **Current State**
	- Orphaned processes removed.
	- One active `cursor-shell` remains attached to real TTY.
	- No evidence of network activity or malicious behavior.
	- Issue classified as lifecycle leakage, not security concern.
	  
	  **Lessons**
	- `cursor-shell` serves dual purpose: background agent + terminal PTY host.
	- Bulk `pkill` is unsafe when PTY-backed sessions exist.
	- Safer cleanup: kill only processes with `PPID == 1`.
	  
	  **Conclusion**
	  Behavior consistent with Electron-style process leakage across upgrades and workspace churn. Not abnormal, but poor process lifecycle management.
	-