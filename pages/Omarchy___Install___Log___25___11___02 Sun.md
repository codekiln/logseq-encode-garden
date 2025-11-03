# Install Log
	- ## Failed Omarchy 3.1.4 Install on Early 2015 Retina MacBook Pro (Intel) with Broadcom BCM43602
	- Trying to install `omarchy-3.1.4.iso` USB on an early 2015 Retina MacBook Pro (Intel).
		- I used [[balenaEtcher]] to install into a 16GB [[USB/Drive]]
	- **Installation method:** Automated Script (`.automated_script.sh`)
	- **Summary:**
	- Secure Boot wasn’t enabled.
	- Ran the installer wizard from USB; system powered off before the “Reboot now” screen.
	- On reboot (USB removed), got the flashing folder/question-mark (“support.apple.com/mac/startup”).
	- Booted back into USB; partitions existed (`/dev/sda1` EFI, `/dev/sda2` Linux root).
	- Found Wi-Fi had not been connected during install. Connected manually using `iwctl` and confirmed with `ping archlinux.org`.
	- Re-ran the installation using `.automated_script.sh`, which invokes `./configurator`, but the process halted there before completing.
	- **Additional Info:**
	- While troubleshooting, I encountered repeated Broadcom Wi-Fi firmware errors:
	- ```
	  brcmfmac: Direct firmware load for brcm/brcmfmac43602-pcie.Apple Inc.-MacBookPro11,4.bin failed with error -2
	  You are using the broadcom-wl driver, which is not maintained and is incompatible with Linux kernel security mitigations.
	  ```
	- This prevents the installer from loading the GUI and halts before bootloader setup. I can confirm Ethernet works, and I can connect manually via `iwctl`.
	- Looking for guidance on patching or blacklisting the Broadcom driver (`brcmfmac`) during installation, or any firmware workaround for BCM43602 on the 2015 MacBook Pro. I see there's a similar thread here - https://www.reddit.com/r/archlinux/comments/1g158h3/wifi_on_2015_mbp_bcm43602_im_about_to_pull_my/ but I don't quite know what to do
	- **Request:**
	- What’s the correct procedure to perform a full installation of Omarchy 3.1.4 on an early 2015 MacBook Pro after connecting to Wi-Fi, using the automated script? Should any special steps be taken for EFI bootloader registration or Broadcom driver compatibility on older Macs?
	- *(Will upload logs or screenshots if needed; please advise which would be most useful.)*
	-