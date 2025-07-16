# How to Fall Back and ReParse when Structured Outputs Fail Parsing
	- via [[LangChain/How To/Fall Back and Reparse when Structured Outputs Fail]]
		- ```python
		  # This will be run as a fallback chain
		  fallback_chain = insert_errors | code_chain
		  N = 3  # Max re-tries
		  code_chain_re_try = code_chain.with_fallbacks(
		      fallbacks=[fallback_chain] * N, exception_key="error"
		  )
		  ```