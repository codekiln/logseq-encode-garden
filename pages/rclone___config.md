# rclone config
	- ## Use [[rclone/config/file]] to get the current config file
		- by default, it's at
	- ## Use [[rclone/EnvVar/RCLONE_CONFIG_]] prefix to configure a [[rclone/remote]]
		- Section **[Docs → Usage → Environment Variables → Config file](https://rclone.org/docs/#config-file)**:
			- > “To find the name of the environment variable, you need to set, take `RCLONE_CONFIG_` + *name of remote* + `_` + *name of config-file option* and make it all uppercase.” [rclone.org](https://rclone.org/docs/)