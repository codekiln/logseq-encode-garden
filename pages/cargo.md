tags:: [[Rust/Tool]], [[Package Manager]]

- packages are referred to as [[cargo/crate]]s
	- [[cargo/new]] creates a new package
		- you may need to specify `--name` flag if the folder starts with a number (illegal for package names to have numbers)
	- [[cargo/build]] builds
	- [[cargo/build/--release]] builds with optimizations, putting executable in `target/release` instead of `target/debug`
	- [[cargo/run]] builds and runs **more convenient**
	- [[cargo/check]] does [[Static Code Analysis]], specifically [[Programming/Code/Analysis/Static/Type/Check/ing]]
	-