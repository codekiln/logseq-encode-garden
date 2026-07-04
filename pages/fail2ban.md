logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Cyril Jaquier]]
date-created:: [[2004]]

- # [fail2ban](https://www.fail2ban.org)
	- [fail2ban/fail2ban](https://github.com/fail2ban/fail2ban) — [[GitHub/Star]]s: 18,092 as of [[2026-07-04 Sat]]
	- An intrusion-prevention daemon that scans log files (for example `/var/log/auth.log`) for repeated authentication failures and bans the offending IPs by updating firewall rules.
	- Written in [[Python]].
	- Bans are enforced through pluggable actions (`iptables`, `nftables`, `firewalld`, and others) and expire after a configurable window, so it mainly blunts brute-force and dictionary attacks against services like [[SSH]].
	- Behavior is defined by **jails** that pair a **filter** (regex patterns matched against a log) with an **action**; defaults ship in `jail.conf` and are overridden in `jail.local`.
