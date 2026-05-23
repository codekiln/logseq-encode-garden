- Prefs for [[Software/Testing]] in [[Python]]
	- use [[Pytest]]
	- use [[Pytest/Fixture]]s
	- separate integration from unit tests by folder, for example:
		- ```
		  my-package/
		    my_package/
		      my_module.py
		    tests/
		      conftest.py
		      integration/
		        my_package/
		          test_my_module.py
		      unit/
		        my_package/
		          test_my_module.py
		  
		  ```