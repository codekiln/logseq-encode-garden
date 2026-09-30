logseq-entity:: [[Logseq/Entity/Question]]

- # Can I use a [[Tailscale/Tailnet]] to view a website running on a private server as a way to make [[Software/Personal]]?
	- ## [[AI Answer]]
		- **Short answer:** yes. Run the site on the private server bound to localhost, publish it to the tailnet with `tailscale serve`, and open its `https://machine-name.tailnet-name.ts.net` address from any device signed in to the same tailnet. Nothing on the server needs to be open to the internet.
		- ### Serve keeps it inside the tailnet
			- [[Answer/Official]] from [Tailscale Serve](https://tailscale.com/kb/1312/serve): Serve routes traffic from other devices on the tailnet to a local service on your device. Access is limited to tailnet members and people a device has been shared with, and the service sees their identity in request headers.
			- `tailscale serve 3000` forwards requests to `http://127.0.0.1:3000`. The local service should listen on localhost only, so the tailnet address is the only way in.
			- Serve needs Tailscale client 1.52 or later for the current command syntax.
		- ### Names and HTTPS
			- With MagicDNS, the server is reachable by machine name, and by `machine-name.tailnet-name.ts.net` in full. Shared devices must use the full name. [[Answer/Official]] from [MagicDNS](https://tailscale.com/kb/1081/magicdns).
			- Serve serves over HTTPS and provisions a TLS certificate for that name. The tailnet must have HTTPS certificates enabled in the admin console DNS settings, which requires MagicDNS. The certificates come from Let's Encrypt and the private keys stay on the device. [[Answer/Official]] from [Enabling HTTPS](https://tailscale.com/kb/1153/enabling-https).
			- Trade-off: every certificate is recorded in the public Certificate Transparency log, so the machine names in the tailnet become publicly visible, even though access stays restricted. Tailscale advises against enabling HTTPS if a machine name contains anything sensitive.
		- ### Serve versus Funnel
			- Funnel publishes the same kind of local service to the public internet through a public URL, and visitors do not need Tailscale. It uses ports 443, 8443 and 10000, has fixed bandwidth limits, and needs MagicDNS, HTTPS and a funnel attribute in the tailnet policy. [[Answer/Official]] from [Tailscale Funnel](https://tailscale.com/kb/1223/funnel).
			- Serve and Funnel cannot both use one port. Whichever command ran last decides whether that port is private or public.
		- ### Fit for personal software
			- This suits software written for one person or a small group: a dashboard, notes app or agent front end on a home or cloud machine, used from a phone and laptop that are already on the tailnet. The same tunnel layer is [[Wireguard]].
			- Limits: every viewer needs Tailscale installed and signed in, or a device share. Anyone without that can see the site only through Funnel, which makes it public.
			- Not checked here: Tailscale's current plan limits on the number of users and devices, and how device sharing behaves for a site shared with another person. Consult Tailscale's pricing and sharing pages before relying on either.
