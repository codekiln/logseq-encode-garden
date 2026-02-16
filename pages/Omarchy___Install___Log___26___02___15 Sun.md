# Arch Linux Install Log - Intel MacBook Pro
	- Public note: sensitive identifiers have been redacted for sharing.
	- ## Goal
		- Install [[Arch]] (manual [[Omarchy]] method) on an Intel MacBook Pro with a full disk wipe.
	- ## Quick Run Log
		- Trying [[Omarchy/Install/Manual]] another time with [[Omarchy/v/3/3/0]].
		- DONE download raw [[Arch]] ISO `archlinux-2026.02.01-x86_64.iso` from an official Arch mirror.
		- DONE verify downloaded `archlinux-2026.02.01-x86_64.iso` against `archlinux-2026.02.01-x86_64.iso.sig` using `gpg --keyserver-options auto-key-retrieve --verify archlinux-2026.02.01-x86_64.iso.sig`.
			- ~~~
			  gpg --keyserver-options auto-key-retrieve --verify archlinux-2026.02.01-x86_64.iso.sig
			  gpg: assuming signed data in 'archlinux-2026.02.01-x86_64.iso'
			  gpg: Signature made Sun Feb  1 03:08:03 2026 EST
			  gpg:                using EDDSA key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
			  gpg:                issuer "pierre@archlinux.org"
			  gpg: key 76A5EF9054449A5C: public key "Pierre Schmitz <pierre@archlinux.org>" imported
			  gpg: key 7F2D434B9741E8AC: public key "Pierre Schmitz <pierre@archlinux.org>" imported
			  gpg: key 76A5EF9054449A5C: "Pierre Schmitz <pierre@archlinux.org>" not changed
			  gpg: key 7F2D434B9741E8AC: "Pierre Schmitz <pierre@archlinux.org>" not changed
			  gpg: Total number processed: 4
			  gpg:               imported: 2
			  gpg:              unchanged: 2
			  gpg: no ultimately trusted keys found
			  gpg: Good signature from "Pierre Schmitz <pierre@archlinux.org>" [unknown]
			  gpg: WARNING: The key's User ID is not certified with a trusted signature!
			  gpg:          There is no indication that the signature belongs to the owner.
			  Primary key fingerprint: 3E80 CA1A 8B89 F69C BA57  D98A 76A5 EF90 5444 9A5C
			  ~~~
			- Result: `Good signature` confirms the `.sig` matches the ISO bytes.
			- Note: trust warning means local Web of Trust trust is not established yet; it is not a signature failure.
			- Verified fingerprint `3E80 CA1A 8B89 F69C BA57 D98A 76A5 EF90 5444 9A5C` against official Arch sources:
				- [Arch Linux Downloads](https://archlinux.org/download/)
				- [Arch Linux Master Keys](https://archlinux.org/master-keys/)
		- DONE use [[balenaEtcher]] to write the ISO to a USB drive.
		- DONE insert USB and power on while holding the Option key.
		- DONE select Wi-Fi and then choose EFI Boot.
		- DONE boot the Arch ISO in UEFI mode.
		- DONE confirm wireless hardware with `lspci | grep -i network`.
			- `Broadcom Inc. and subsidiaries BCM43602 802.11ac Wireless LAN SoC (rev 01)`
		- DONE try `iwctl`.
			- ~~~
			  device list
			  station wlan0 scan
			  station wlan0 get-networks
			  station wlan0 connect YOUR_SSID
			  ~~~
	- ## 1) Boot and Initial Setup
		- Burned Arch ISO to USB.
		- Booted while holding Option.
		- Selected EFI Boot.
		- Verified UEFI mode.
	- ## 2) Disk Partitioning (Full Wipe)
		- Used `cfdisk /dev/sda`.
		- Final GPT layout:
			- `/dev/sda1` - 512M - EFI System
			- `/dev/sda2` - ~465G - Linux filesystem
		- Formatted:
			- ~~~
			  mkfs.fat -F32 /dev/sda1
			  mkfs.ext4 /dev/sda2
			  ~~~
		- Mounted:
			- ~~~
			  mount /dev/sda2 /mnt
			  mkdir /mnt/boot
			  mount /dev/sda1 /mnt/boot
			  ~~~
	- ## 3) Base Install
		- ~~~
		  pacstrap /mnt base linux linux-firmware networkmanager sudo vim
		  ~~~
		- Generated fstab:
			- ~~~
			  genfstab -U /mnt >> /mnt/etc/fstab
			  ~~~
		- Entered chroot:
			- ~~~
			  arch-chroot /mnt
			  ~~~
	- ## 4) System Configuration
		- ### Timezone
			- ~~~
			  ln -sf /usr/share/zoneinfo/<local-timezone> /etc/localtime
			  hwclock --systohc
			  ~~~
		- ### Locale
			- Uncommented `en_US.UTF-8 UTF-8` in `/etc/locale.gen`.
			- ~~~
			  locale-gen
			  echo "LANG=en_US.UTF-8" > /etc/locale.conf
			  ~~~
		- ### Hostname
			- ~~~
			  echo "<host-name>" > /etc/hostname
			  ~~~
			- Created `/etc/hosts`.
		- ### Root Password
			- ~~~
			  passwd
			  ~~~
		- ### Enable NetworkManager
			- ~~~
			  systemctl enable NetworkManager
			  ~~~
	- ## 5) Bootloader (systemd-boot)
		- Installed:
			- ~~~
			  bootctl install
			  ~~~
		- Created `/boot/loader/loader.conf`:
			- ~~~
			  default arch
			  timeout 3
			  editor no
			  console-mode keep
			  ~~~
		- Created `/boot/loader/entries/arch.conf`.
		- Used PARTUUID instead of `/dev/sda2`:
			- ~~~
			  blkid -s PARTUUID -o value /dev/sda2
			  ~~~
		- Entry file:
			- ~~~
			  title   Arch Linux
			  linux   /vmlinuz-linux
			  initrd  /initramfs-linux.img
			  options root=PARTUUID=<value> rw
			  ~~~
	- ## 6) First Boot
		- Rebooted.
		- Held Option.
		- Selected EFI Boot.
		- Reached `<host-name> login:` prompt.
		- System successfully booted from internal disk.
	- ## 7) Wi-Fi Debugging (Broadcom `BCM43602`)
		- Initial attempts:
			- Installed `broadcom-wl`.
			- `modprobe wl` succeeded.
			- No network interface appeared.
			- `dmesg` showed NULL ieee80211 pointer error.
		- Conclusion:
			- `wl` driver is unstable on the current kernel.
	- ## 8) Temporary Networking Attempts
		- ### Attempt 1: iPhone USB Tethering (successful on ISO)
			- During live ISO phase:
				- Loaded `ipheth`.
				- USB device detected correctly.
				- Kernel message observed:
					- ~~~
					  ipheth 1-5:1.2: Apple iPhone USB Ethernet device attached
					  ipheth 1-5:1.2 enp0s20u5i2: renamed from eth0
					  ~~~
				- Interface `enp0s20u5i2` appeared in `ip link`.
				- Ran:
					- ~~~
					  dhcpcd enp0s20u5i2
					  ~~~
				- Successfully obtained DHCP lease (172.20.10.x).
				- Verified connectivity with:
					- ~~~
					  ping archlinux.org
					  ~~~
			- This provided temporary working internet during installation.
		- ### Attempt 2: iPhone USB Tethering (post-install failure)
			- After reboot into installed system:
				- `ipheth` module loaded.
				- USB device detected.
				- Repeated USB connect/disconnect loops.
				- No network interface created.
				- No blue hotspot banner on iPhone.
				- Possible Lightning port instability or USB negotiation issue (hypothesis, not confirmed).
			- Conclusion:
				- USB tethering is unreliable post-install.
				- Root cause is undetermined and may be Lightning port instability, USB cable behavior, iOS policy differences, or kernel behavior differences between live ISO and installed system.
		- ### Attempt 3: Continue Without Network
			- `pacman` failed (no internet).
	- ## 9) Get Internet to Finish Installation
		- Use another computer as internet bridge.
		- Hardware required:
			- USB-A to Gigabit Ethernet adapter (for MacBook)
			- Existing Ethernet cable
		- Topology:
			- Internet (Wi-Fi) -> Internet Sharing -> Ethernet -> USB-A to Ethernet adapter -> Arch MacBook
		- Windows steps:
			- `ncpa.cpl`
			- Wi-Fi adapter -> Properties -> Sharing
			- Enable Internet Sharing
			- Share to Ethernet
		- Arch steps:
			- ~~~
			  ip link
			  dhcpcd <ethernet-interface>
			  ping archlinux.org
			  ~~~
	- ## Current State
		- [x] Arch installed
		- [x] Bootloader working
		- [x] System boots cleanly
		- [x] NetworkManager enabled
		- [ ] Wi-Fi not yet functional
		- [ ] Temporary network pending via Ethernet bridge
	- ## Next Steps After Ethernet Is Live
		- Remove unstable `broadcom-wl`.
		- Use in-kernel `brcmfmac` + firmware.
		- Possibly install `linux-lts`.
		- Confirm Wi-Fi device appears.
	- ## Summary
		- Installation succeeded cleanly.
		- The only blocker is reliable network access for firmware and driver stabilization.
		- Once Ethernet bridge is connected, system finalization should take about 10 minutes.
