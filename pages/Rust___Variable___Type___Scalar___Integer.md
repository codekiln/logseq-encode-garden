- types
	- **Table 3-1: Integer Types in Rust**
	  | Length | Signed | Unsigned |
	  | ---- | ---- | ---- |
	  | 8-bit | `i8` | `u8` |
	  | 16-bit | `i16` | `u16` |
	  | 32-bit | `i32` | `u32` |
	  | 64-bit | `i64` | `u64` |
	  | 128-bit | `i128` | `u128` |
	  | architecture dependent | `isize` | `usize` |
- signed integers use [[Programming/Two's Complement]]
- `isize` and `usize`
	- flexible: 64 bits if you’re on a 64-bit architecture and 32 bits if you’re on a 32-bit architecture
	- [[Rust/isize]] is the signed integer that fits on whatever computer is running the code
	- [[Rust/usize]] is the unsigned integer that fits on whatever computer is running the code
- [[Rust/Error/Panic]] will occur if you assign a value outside of the capacity
	- [[Rust/Compile/Debug]] mode will check for this
	- [[Rust/Compile/Release]] will NOT check for this
		- instead, it will silently perform [[Programming/Two's Complement/Wrapping]]
		- mitigations
			- Wrap in all modes with the `wrapping_*` methods, such as `wrapping_add`.
			- Return the `None` value if there is overflow with the `checked_*` methods.
			- Return the value and a Boolean indicating whether there was overflow with the `overflowing_*` methods.
			- Saturate at the value’s minimum or maximum values with the `saturating_*` methods.
- see also
	- [Data Types - The Rust Programming Language](https://rust-book.cs.brown.edu/ch03-02-data-types.html)