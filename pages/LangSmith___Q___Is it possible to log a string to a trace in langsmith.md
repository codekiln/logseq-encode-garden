tags:: [[Question/My]]

- # Is it possible to log a string to a [[LangSmith/Trace]]?
	- **Impetus**: it's difficult to get access to log messages in [[langgraph/Cloud]]. Could we instead log onto the trace?
	- ## Research
		- Yes, there are several ways to add custom data to a LangSmith trace:
			- 1. Using metadata ([docs](https://docs.smith.langchain.com/observability/how_to_guides/add_metadata_tags)):
				- With the `@traceable` decorator or `traceable` function:
					- ```python
					  @ls.traceable(
					    metadata={"my-log": "my message"}
					  )
					  def my_function():
					    # Your code here
					    pass
					  ```
				- Dynamically within a traced function ([docs](https://docs.smith.langchain.com/observability/how_to_guides/access_current_run)):
					- ```python
					  @ls.traceable
					  def my_function():
					    rt = ls.get_current_run_tree()
					    rt.metadata["log_message"] = "my log message"
					  ```
			- 2. Using the context manager ([docs](https://docs.smith.langchain.com/observability/how_to_guides/trace_without_environment_variables)):
				- ```python
				  with ls.trace(
				    metadata={"log": "my message"}
				  ) as rt:
				    # Your code here
				    rt.metadata["another_log"] = "another message"
				  ```
			- 3. At invocation time using `langsmith_extra` ([docs](https://docs.smith.langchain.com/observability/how_to_guides/annotate_code_for_tracing)):
				- ```python
				  my_traced_function(
				    langsmith_extra={
				      "metadata": {"log": "my message"}
				    }
				  )
				  ```
		- The metadata can be any JSON-serializable key-value pairs
		- You can view these logs in the LangSmith UI or query them programmatically ([docs](https://docs.smith.langchain.com/observability/how_to_guides/query_traces))
		- This provides a way to add logging information that will be associated with the specific trace/run
	- ## [[My Question]]s - Follow-Up
		- ### What about if I'm running within [[langgraph/Cloud]] or [[langgraph/Studio]]? All interactions are automatically logged to langsmith without needing to add ls.trace. should I just use the context manager?
			- When running in LangGraph Cloud/Studio:
				- All LangGraph operations are automatically traced to LangSmith
				- You have two main options for adding custom logs:
					- 1. Use `get_current_run_tree()` to access the current trace:
						- ```python
						  from langsmith import get_current_run_tree
						  
						  def my_node():
						      rt = get_current_run_tree()
						      rt.metadata["my_log"] = "some message"
						      # ... rest of node logic
						  ```
					- 2. Use the context manager for specific sub-sections:
						- ```python
						  from langsmith import trace
						  
						  def my_node():
						      with trace(
						          name="sub-operation",
						          metadata={"log": "message"}
						      ) as rt:
						          # ... sub-operation logic
						          rt.metadata["another_log"] = "another message"
						  ```
				- The first approach is simpler if you just want to add logs to the existing trace
				- The second approach is better if you want to create a separate sub-trace
		- ### What about if I'm inside a test function marked with [[LangSmith/PyTest/mark]] `@pytest.mark.langsmith`?
			- When using `@pytest.mark.langsmith`:
				- The test function is automatically traced
				- You can use the `testing` module to log data ([docs](https://docs.smith.langchain.com/evaluation/how_to_guides/pytest)):
					- ```python
					  from langsmith import testing as t
					  
					  @pytest.mark.langsmith
					  def test_my_function():
					      # Log test inputs
					      t.log_inputs({"input_key": "input_value"})
					      
					      # Run your test logic
					      result = my_function()
					      
					      # Log test outputs
					      t.log_outputs({"output_key": result})
					      
					      # Add custom feedback/logs
					      with t.trace_feedback():
					          t.log_feedback(key="my_log", score=1.0)
					  ```
				- The test results and all logged data will be available in the LangSmith UI
				- You can group tests into test suites using `LANGSMITH_TEST_SUITE` environment variable
				- Test runs can be cached using `LANGSMITH_TEST_CACHE` to save resources