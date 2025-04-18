# How to use a #Debugger with `langgraph dev` in [[PyCharm]]
	- ## Partially Working
		- ### Creating a [[PyCharm/Run Configuration]] for `langgraph-dev --allow-blocking`
			- [[langgraph/GitHub/Discussion/25/04/How to use langgraph dev in a PyCharm Debugger]]
				- #### [[My Notes]]
					- Marked as "partially working" because the `--allow-blocking` argument is needed because [[pydevd]] uses blocking operations to resolve symlinks to files, which triggers [[langgraph]]'s detection using [[Py/Lib/blockbuster]]
				- #### PyCharm Run Configuration parameters
					- **Run Configuration Type** - Python
					- **Virtual Environment** - Select your project's virtual environment
					- **Run Configuration Subtype** - `script`
					- **Script Path**: absolute path to the `langgraph` executable within the virtualenv, found with `which langgraph`
						- (anyone know how to make this more dynamic? just putting in `langgraph` yields `FileNotFoundError: [Errno 2] No such file or directory: 'langgraph'`
					- **Script Parameters**: `dev --allow-blocking`
						- no need for `--debug-port`, which is for  [[Py/debugpy]]  instead of PyCharm's  [[pydevd]]
	- ## Not Working
		- ### Attach to Process
			- #### 1 - `langgraph dev` in a terminal, then use [[PyCharm/Debug/Attach to Process]]
				- #### To reproduce
					- in a terminal - run `langgraph dev`
					- initiate [[PyCharm/Debug/Attach to Process]]
				- #### Expected Behavior - PyCharm is able to debug an external process
				- #### Actual Behavior - `error: Execution was interrupted, reason: signal SIGSTOP`.
					- ```
					  Attaching to a process with PID=85,887
					  /path/to/python/env/bin/python /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach_pydevd.py --port 59663 --pid 85887
					  Running: lldb --no-lldbinit --script-language Python -o 'process attach --pid 85887' -o 'command script import "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/linux_and_mac/lldb_prepare.py"' -o 'load_lib_and_attach "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach.dylib" 0 "import sys;sys.path.append(\"/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev\");sys.path.append(\"/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process\");import attach_script;attach_script.attach(port=59663, host=\"127.0.0.1\", protocol=\"\", debug_mode=\"\");" 0' -o 'process detach' -o 'script import os; os._exit(1)'
					  (lldb) process attach --pid 85887
					  Process 85887 stopped
					  * thread #1, queue = 'com.apple.main-thread', stop reason = signal SIGSTOP
					      frame #0: 0x00000001935353c8 libsystem_kernel.dylib`__semwait_signal + 8
					  libsystem_kernel.dylib`__semwait_signal:
					  ->  0x1935353c8 <+8>:  b.lo   0x1935353e8               ; <+40>
					      0x1935353cc <+12>: pacibsp 
					      0x1935353d0 <+16>: stp    x29, x30, [sp, #-0x10]!
					      0x1935353d4 <+20>: mov    x29, sp
					  Target 0: (python3.12) stopped.
					  Executable module set to "/path/to/python/3.12.1/bin/python3.12".
					  Architecture set to: arm64-apple-macosx-.
					  (lldb) command script import "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/linux_and_mac/lldb_prepare.py"
					  (lldb) load_lib_and_attach "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach.dylib" 0 "import sys;sys.path.append(\"/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev\");sys.path.append(\"/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process\");import attach_script;attach_script.attach(port=59663, host=\"127.0.0.1\", protocol=\"\", debug_mode=\"\");" 0
					  /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach.dylib
					  success
					  import sys;sys.path.append("/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev");sys.path.append("/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process");import attach_script;attach_script.attach(port=59663, host="127.0.0.1", protocol="", debug_mode="");
					  error: error: Execution was interrupted, reason: signal SIGSTOP.
					  The process has been returned to the state before expression evaluation.
					  (lldb) process detach
					  Process 85887 detached
					  (lldb) script import os; os._exit(1)
					  Traceback (most recent call last):
					    File "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach_pydevd.py", line 79, in <module>
					      main(process_command_line(sys.argv[1:]))
					    File "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach_pydevd.py", line 74, in main
					      add_code_to_python_process.run_python_code(
					    File "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/add_code_to_python_process.py", line 533, in run_python_code_mac
					      subprocess.check_call(' '.join(cmd), shell=True, env=env)
					    File "/path/to/python/3.12.1/lib/python3.12/subprocess.py", line 413, in check_call
					      raise CalledProcessError(retcode, cmd)
					  subprocess.CalledProcessError: Command 'lldb --no-lldbinit --script-language Python -o 'process attach --pid 85887' -o 'command script import "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/linux_and_mac/lldb_prepare.py"' -o 'load_lib_and_attach "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process/attach.dylib" 0 "import sys;sys.path.append(\"/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev\");sys.path.append(\"/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd_attach_to_process\");import attach_script;attach_script.attach(port=59663, host=\"127.0.0.1\", protocol=\"\", debug_mode=\"\");" 0' -o 'process detach' -o 'script import os; os._exit(1)'' returned non-zero exit status 1.
					  ```
			- #### 2 - `langgraph dev` in a [[PyCharm/Run Configuration]], then use [[PyCharm/Debug/Attach to Process]]
				- setup - same as 1, except running `langgraph dev` using a run configuration
				- same result as 1
		-