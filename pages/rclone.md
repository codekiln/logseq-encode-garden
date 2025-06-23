created-by:: [[Person/Nick Craig-Wood]]
tags:: [[CLI/Tool]], [[File/Backup]]

- # [rclone](https://rclone.org/docs/)
	- ## installation
		- [Installation with curl](https://rclone.org/install/#macos-precompiled)
		- [[rclone/config]] [rclone config docs](https://rclone.org/docs/) for more details
	- ## #Examples
		- ### list buckets (directories) on a named remote with [[rclone/lsd]]
			- `rclone lsd <REMOTE_NAME>:`
			- You must include the trailing `:`
		- ### list files in a specific bucket with [[rclone/ls]]
			- `rclone ls <REMOTE_NAME>:<BUCKET_NAME>`
		- ### copy a single file to a given bucket with [[rclone/copy]]
			- `rclone copy IMG_0528.PNG <REMOTE_NAME>:<BUCKET_NAME>`