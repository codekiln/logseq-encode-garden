logseq-entity:: [[Logseq/Entity/Concept]]

- # WireGuard
	- ## Overview
		- **WireGuard** is a VPN protocol and implementation that presents an encrypted tunnel as an ordinary network interface. It carries IP packets inside UDP and aims to be simpler and faster than older VPNs such as OpenVPN and IPsec, with a small enough codebase to audit. [^1]
	- ## Context
		- It began on Linux and now runs on Windows, macOS, BSD, iOS and Android. The kernel components are licensed GPLv2. [^1]
		- [[Tailscale]] builds its [[Tailscale/Tailnet]] on WireGuard, using the userspace Go implementation `wireguard-go`, and adds key distribution, sign-in, NAT traversal and access control around it. [^2]
	- ## Key Principles
		- **Small and opinionated.** One fixed set of modern primitives instead of negotiated cipher suites: Curve25519, ChaCha20, Poly1305, BLAKE2, SipHash24 and HKDF, arranged with the Noise protocol framework. [^1]
		- **Peers identified by public keys.** Each peer holds a private key and lists the public keys of the peers it will accept. Packets are encrypted to a peer's public key and sent to its endpoint. [^1]
		- **Roaming.** A peer's endpoint can change, for example when a laptop switches between networks, without rebuilding the tunnel. [^1]
	- ## Mechanism
		- WireGuard itself does not distribute keys or discover peers. Plain WireGuard requires each peer's keys and endpoints to be configured by hand. A coordination layer, such as Tailscale's, automates that step. [^2]
	- ## Misconceptions
		- WireGuard is not Tailscale. WireGuard is the tunnel protocol, and Tailscale is a service that manages many WireGuard tunnels as one network.
	- ## Footnotes
		- [^1]: https://www.wireguard.com/
		- [^2]: https://tailscale.com/blog/how-tailscale-works
