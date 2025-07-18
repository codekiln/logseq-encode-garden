tags:: [[Programming]], [[Algorithm]], [[Diataxis/Reference]], [[Algorithm]] 
alias:: [[Dynamic Programming]]

- # Dynamic Programming Reference
	- ## Overview
		- Dynamic programming is an algorithmic paradigm that solves complex problems by breaking them down into simpler subproblems
		- It stores the results of subproblems to avoid redundant computations, trading space for time
		- The approach is particularly effective for optimization problems with overlapping subproblems and optimal substructure
	- ## Core Principles
		- ### Optimal Substructure
			- An optimal solution to a problem contains optimal solutions to its subproblems
			- Example: In shortest path problems, the optimal path from A to C contains the optimal path from A to B and B to C
			- Mathematical formulation: If $$S^*$$ is optimal for problem $$P$$, then any sub-solution $$S^*_i$$ is optimal for subproblem $$P_i$$
		- ### Overlapping Subproblems
			- The same subproblems are solved multiple times during the computation
			- Dynamic programming stores these results to avoid recomputation
			- Example: Fibonacci sequence calculation reuses $$F(n-1)$$ and $$F(n-2)$$ multiple times
			- Without DP: $$F(5)$$ computes $$F(3)$$ twice, $$F(2)$$ three times, $$F(1)$$ five times
	- ## Implementation Approaches
		- ### Top-Down (Memoization)
			- Recursive approach with caching of computed results
			- Starts from the original problem and works down to base cases
			- Uses a memo table to store intermediate results
			- Example: Recursive Fibonacci with memoization
			- ~~~
			  def fib_memo(n, memo={}):
			      if n in memo:
			          return memo[n]
			      if n <= 1:
			          return n
			      memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
			      return memo[n]
			  ~~~
		- ### Bottom-Up (Tabulation)
			- Iterative approach that builds solutions from base cases up
			- Fills a table systematically, ensuring all dependencies are computed first
			- Generally more space-efficient than top-down approaches
			- Example: Iterative Fibonacci using an array
			- ~~~
			  def fib_tab(n):
			      if n <= 1:
			          return n
			      dp = [0] * (n + 1)
			      dp[1] = 1
			      for i in range(2, n + 1):
			          dp[i] = dp[i-1] + dp[i-2]
			      return dp[n]
			  ~~~
	- ## Classic Problems
		- ### Fibonacci Sequence
			- Problem: Calculate $$F(n)$$ where $$F(n) = F(n-1) + F(n-2)$$, $$F(0) = 0$$, $$F(1) = 1$$
			- Time complexity: $$O(n)$$ with DP vs $$O(2^n)$$ with naive recursion
			- Space complexity: $$O(1)$$ with bottom-up, $$O(n)$$ with top-down
			- Mathematical recurrence: $$F(n) = F(n-1) + F(n-2)$$ for $$n \geq 2$$
		- ### Longest Common Subsequence (LCS)
			- Problem: Find the longest subsequence common to two strings
			- Time complexity: $$O(m \times n)$$ where $$m$$, $$n$$ are string lengths
			- Space complexity: $$O(m \times n)$$ for the DP table
			- Recurrence relation:
				- If $$s_1[i] == s_2[j]$$: $$dp[i][j] = dp[i-1][j-1] + 1$$
				- Else: $$dp[i][j] = \max(dp[i-1][j], dp[i][j-1])$$
		- ### Knapsack Problem
			- Problem: Maximize value while staying within weight capacity
			- Variants: 0/1 (each item once), unbounded (unlimited items)
			- Time complexity: $$O(n \times W)$$ where $$n$$ is items, $$W$$ is capacity
			- 0/1 Knapsack recurrence:
				- If $$w[i] \leq j$$: $$dp[i][j] = \max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])$$
				- Else: $$dp[i][j] = dp[i-1][j]$$
		- ### Edit Distance
			- Problem: Minimum operations to transform one string to another
			- Operations: insert, delete, substitute
			- Time complexity: $$O(m \times n)$$ where $$m$$, $$n$$ are string lengths
			- Recurrence relation:
				- If $$s_1[i] == s_2[j]$$: $$dp[i][j] = dp[i-1][j-1]$$
				- Else: $$dp[i][j] = 1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])$$
		- ### Matrix Chain Multiplication
			- Problem: Find optimal parenthesization to minimize scalar multiplications
			- Time complexity: $$O(n^3)$$ for the DP solution
			- Space complexity: $$O(n^2)$$ for the memoization table
			- Recurrence: $$dp[i][j] = \min(dp[i][k] + dp[k+1][j] + p[i-1] \times p[k] \times p[j])$$ for $$i \leq k < j$$
	- ## Algorithmic Patterns
		- ### State Definition
			- $$dp[i][j]$$ represents the optimal solution for subproblem $$(i,j)$$
			- State dimensions depend on problem constraints
			- Example: LCS uses 2D state for string positions
			- Common patterns:
				- $$dp[i]$$
	- 1D state (Fibonacci, climbing stairs)
		- $$dp[i][j]$$
	- 2D state (LCS, edit distance)
		- $$dp[i][j][k]$$
	- 3D state (complex constraints)
		- ### Transition Function
			- Formula that relates current state to previous states
			- Must handle all possible cases and edge conditions
			- Example: LCS transition considers character match/mismatch
			- General form: $$dp[\text{current\_state}] = f(dp[\text{previous\_states}])$$
		- ### Base Cases
			- Initial conditions that don't depend on other subproblems
			- Must be defined for all boundary conditions
			- Example: $$dp[0][0] = 0$$ for many problems
			- Common base cases:
				- $$dp[0] = 0$$ or $$dp[0] = 1$$
				- $$dp[i][0] = 0$$ for 2D problems
				- $$dp[0][j] = 0$$ for 2D problems
	- ## Space Optimization Techniques
		- ### Rolling Arrays
			- Use only the last few rows/columns of the DP table
			- Reduces space complexity from $$O(n^2)$$ to $$O(n)$$ in many cases
			- Example: LCS can be solved with $$O(\min(m,n))$$ space
			- Implementation pattern:
			- ~~~
			  # Instead of dp[n][m], use dp[2][m] or dp[m]
			  prev = [0] * (m + 1)
			  curr = [0] * (m + 1)
			  for i in range(1, n + 1):
			      for j in range(1, m + 1):
			          # compute curr[j] using prev
			      prev, curr = curr, prev  # swap arrays
			  ~~~
		- ### State Compression
			- Represent multiple states in a single variable
			- Common in bitmask DP problems
			- Example: Traveling Salesman Problem with bitmasks
			- Bit manipulation: $$\text{state} |= (1 << i)$$ to set bit $$i$$
	- ## Time Complexity Analysis
		- ### General Formula
			- Time = Number of states × Time per transition
			- Space = Number of states × Space per state
			- Mathematical form: $$T(n) = \sum(\text{states}) \times T(\text{transition})$$
		- ### Common Patterns
			- 1D DP: $$O(n)$$ states, $$O(1)$$ transitions → $$O(n)$$ total
			- 2D DP: $$O(n^2)$$ states, $$O(1)$$ transitions → $$O(n^2)$$ total
			- Tree DP: $$O(n)$$ states, $$O(\text{degree})$$ transitions → $$O(n \times \text{degree})$$ total
			- State space analysis: $$|S| = \prod(\text{dimensions})$$
	- ## Problem Recognition
		- ### Key Indicators
			- Optimization problems (min/max)
			- Problems that can be broken into subproblems
			- Overlapping computations in naive solutions
			- Problems with "all possible" or "count ways" in description
			- Keywords: "minimum", "maximum", "optimal", "shortest", "longest"
		- ### When Not to Use
			- Problems without optimal substructure
			- Problems with exponential state space
			- Problems better solved by greedy algorithms
			- Problems with polynomial-time greedy solutions
	- ## Mathematical Foundations
		- ### Bellman's Principle of Optimality
			- "An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision."
			- Mathematical form: If $$\pi^*$$ is optimal, then $$\pi^*_t$$ is optimal for subproblem starting at time $$t$$
		- ### Recurrence Relations
			- Dynamic programming problems are characterized by recurrence relations
			- General form: $$T(n) = \sum(T(\text{subproblems})) + \text{cost\_of\_combining}$$
			- Example: $$F(n) = F(n-1) + F(n-2)$$ for Fibonacci
	- ## Related References
		- [[Programming/Algorithm/Ref/Greedy]]
		- [[Programming/Algorithm/Ref/Divide and Conquer]]
		- [[Programming/Algorithm/Ref/Recursion]]
		- [[Programming/Complexity/Ref/Time Complexity]]