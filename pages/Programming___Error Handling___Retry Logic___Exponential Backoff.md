tags:: [[Programming]], [[Error Handling]], [[Retry Logic]], [[Algorithm]]
alias:: [[Exponential Backoff]]

- # Exponential Backoff
	- A retry strategy where the delay between retry attempts increases exponentially
	- ## Key Concepts
		- Initial delay: The first waiting period after a failure
		- Multiplier/Base: The factor by which the delay increases each time (typically 2)
		- Max delay: Upper limit on how long to wait between retries
		- Max attempts: Maximum number of retry attempts before giving up
	- ## Common Use Cases
		- Network requests and API calls
		- Distributed systems communication
		- Rate limiting and throttling
		- Database connection retries
	- ## Benefits
		- Prevents overwhelming systems under stress
		- Allows temporary issues to resolve naturally
		- Reduces network congestion
		- More efficient than fixed-interval retries
	- ## Example Formula
		- `delay = min(max_delay, initial_delay * (base ^ attempt_number))`
		- For base=2:
			- 1st retry: 1s
			- 2nd retry: 2s
			- 3rd retry: 4s
			- 4th retry: 8s
			- etc.
		- Note:
			- The key property of *exponential backoff* is **multiplicative growth** of the wait-time:
			  
			  \[
			  t_n = t_0 \times f^{\,n},
			  \]
			  
			  where \(f>1\) is a constant factor and \(n\) is the retry count.  
			  Doubling (\(f = 2\)) yields the classic binary-exponential sequence
			  
			  \[
			  1\text{ s} \;\to\; 2\text{ s} \;\to\; 4\text{ s} \;\to\; 8\text{ s} \;\dots
			  \]
			  
			  which is what the code does with `delay = initial_delay * (base ^ attempt_number)`.  
			  Multiplying by a fixed constant on each failure therefore produces the exponential curve \(t_n = t_0\,2^{\,n}\).
	- ## Implementation Examples
		- [[LangChain/Blog/25/04/17 LangChain Python Improved Content Blocks Retry Logic and More]] - LangChain's Runnable.with_retry implementation
	- ## See also
		- [[LangChain/output_parsers/retry/RetryOutputParser]]