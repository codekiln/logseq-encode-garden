tags:: [[Diataxis/How To]]

- # How To Get 1Password’s “Scan QR Code” Option to Appear in the Chrome Extension
	- ## Goal
		- Make the **Scan QR Code** action available in the 1Password browser pop-up so you can add one-time-password (TOTP) codes directly from a website’s QR image.
	- ## Preconditions
		- Google Chrome 122 + and the latest **1Password** extension (≥ 2.19) installed.
		- Logged in and unlocked in both the desktop app and the browser extension.
		- A Login item for the site you’re enabling 2FA for.
	- ## Procedure
		- ### 1. Update & restart the extension
			- In Chrome, visit **chrome://extensions** → turn on *Developer mode* → **Update**.  
			  Re-launch Chrome to ensure the new build loads.  
			  See *[1Password for Chrome – Setup Guide](https://1password.com/resources/guides/1password-for-google-chrome/)*.
		- ### 2. Open the item’s detail view
			- Click the 1Password toolbar icon → search for the Login → press → to open *Item Details*.  
			  The three-dot **ellipsis** menu appears in the top-right of this pane.  
			  If you don’t open details (e.g., you stay in Quick-Access), the action list is shorter.
		- ### 3. Check whether a TOTP field already exists
			- **Scan QR Code** only shows when the Login *doesn’t yet* have a One-Time Password.  
			  If you previously saved a code, you’ll instead see **Reveal/Copy One-Time Password** or **Remove One-Time Password**.  
			  Click **Edit** → delete the existing TOTP field → **Save** to bring the Scan option back.
		- ### 4. Enable desktop-app integration
			- Ellipsis menu → **Settings** → **General** → toggle **Integrate this extension with the 1Password desktop app** *on*.  
			  A missing integration can hide advanced actions.  
			  Refer to *[If 1Password isn’t working in your browser](https://support.1password.com/1password-browser-troubleshooting/)*.
		- ### 5. Grant screen-recording permission (macOS only)
			- System Settings → Privacy & Security → **Screen Recording** → tick **1Password**.  
			  Without this, the extension can’t capture the QR image on screen.  
			  Details: *[1Password would like to record this screen](https://support.1password.com/screen-recording/)*.
		- ### 6. Re-install as a last resort
			- Remove the extension, quit Chrome, then reinstall from the Chrome Web Store.  
			  Sign in again and repeat Steps 2–4.
	- ## Troubleshooting
		- **Ellipsis missing altogether** → the item is in *compact* view; press → to expand or click **Open in new window** (⌘ O / Ctrl O).
		- **Scan option still absent after Step 3** → verify you’re working in the correct Login vault copy; duplicates may already contain TOTP.
		- **Scan button appears but nothing happens** → ensure the desktop app is unlocked and camera/screen permissions are granted.
	- ## References
		- *Use 1Password as an authenticator for sites with two-factor authentication* – explains where the Scan option lives. <https://support.1password.com/one-time-passwords/>
		- *Scan QR Code – option gone?* (community thread) <https://www.1password.community/discussions/1password/scan-qr-code---option-gone/125334>