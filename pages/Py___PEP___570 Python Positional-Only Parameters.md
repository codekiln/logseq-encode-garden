#
- [PEP 570 – Python Positional-Only Parameters | peps.python.org](https://peps.python.org/pep-0570/)
	- ## Official Summary
		- This PEP proposes to introduce a new syntax, `/`, for specifying positional-only parameters in Python function definitions.
		- Positional-only parameters have no externally-usable name. When a function accepting positional-only parameters is called, positional arguments are mapped to these parameters based solely on their order.
		- When designing APIs (application programming interfaces), library authors try to ensure correct and intended usage of an API. Without the ability to specify which parameters are positional-only, library authors must be careful when choosing appropriate parameter names. This care must be taken even for required parameters or when the parameters have no external semantic meaning for callers of the API.
	- ## [[My Notes]]
		- if you put `/` in a python function parameter definition, it means that parameters before that can only be called in a positional way
		- ### #Example
			- ```python
			  >>> help(pow)
			  ...
			  pow(x, y, z=None, /)
			  ...
			  
			  >>> pow(x=5, y=3)
			  Traceback (most recent call last):
			    File "<stdin>", line 1, in <module>
			  TypeError: pow() takes no keyword arguments
			  ```