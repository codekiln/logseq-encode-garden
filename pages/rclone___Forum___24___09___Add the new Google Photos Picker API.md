# [Add the new Google Photos Picker API to rclone - Feature - rclone forum](https://forum.rclone.org/t/add-the-new-google-photos-picker-api-to-rclone/47938/6)
	- [[My Notes]]
		- announces a change to the google photos API that would probably make [[rclone/gphotosdl]] stop working if it is not modified by [[2025/03]].
		- Links to [Google Photos API changes from March 2025 · Issue #511 · gilesknap/gphotos-sync](https://github.com/gilesknap/gphotos-sync/issues/511) which ended up closing that project
	- Quotes
		- > The current Photo Library API would change **so it only have access to photos and albums that are created by rclone**
		- > This is pretty disheartening as I want to be able to download all my albums and shared albums through rclone as well.
		- [[Person/Nick Craig-Wood]] says
			- > I read this email and ignored it because rclone doesn't use the library API, but apparently they have renamed it and that is what we use.
			  > Library API: Affected scopes and methods
			  As part of our changes to the Google Photos APIs, we have made the following updates.
			  > As shown on the updated Authorization page, the following scopes will be removed from the Library API after March 31, 2025:
				- `photoslibrary.readonly`
				- `photoslibrary.sharing`
				- `photoslibrary`
			- > Rclone uses the first or last scope.
			- > We can probably make uploading work ok, but I think the photo picker API is probably a non starter for rclone.
		- > would mean I cannot use rclone (or anything else except google takeout...) to backup my Google Photos, which I do automatically
-