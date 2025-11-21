- # 2:45pm - 3:04pm Talk: Using AI-Generated Kernels to Instantly Speed Up PyTorch [[Person/Natalie Serrino]]
	- ## Talk: Using AI-Generated Kernels to Instantly Speed Up PyTorch
		- In this talk, we'll talk about how AI generated kernels can meaningfully speed up custom PyTorch code, without any human effort.
		- Lots of great frameworks exist to optimize PyTorch with programmatic optimizations, such as Triton and MLX. But the strongest AI performance gains come from hand-written, low-level kernels that are targeted to the exact device and workload. These are tedious and time-consuming to write, especially when supporting multiple platforms. What if we could automate this process with AI?
		- We'll cover the best practices for AI generating low-level kernels, from how to test and validate the kernels, and what type of agents and contexts are needed to get the best results. We'll cover the research we did where this approach improved PyTorch inference performance on Apple devices.

