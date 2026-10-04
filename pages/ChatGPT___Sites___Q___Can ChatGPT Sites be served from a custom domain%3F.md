logseq-entity:: [[Logseq/Entity/Question]]
via:: [[OpenAI/Dev/Day/26]]

- # Can [[ChatGPT/Sites]] be served from a custom domain?
	- ## [[AI Answer]]
		- **Short answer:** Yes, with exceptions. A Site can use a domain you own by pointing its DNS records at the Site. Sites in Enterprise workspaces cannot at launch.
		- Setup, per [Stacktree](https://stacktr.ee/chatgpt-sites-custom-domain) and [PlayCode](https://playcode.io/blog/chatgpt-sites-explained)
			- You must already own the domain. Sites does not register or sell domains, and the domain stays at your registrar.
			- Open the Site's settings and choose **Add domain**.
			- Enter an apex domain or a subdomain.
			- Add the DNS records and values Sites shows at your domain provider.
			- Wait a few minutes, then refresh the domain status in Sites.
			- ChatGPT can walk you through the registrar's pages if browsing or computer use is on.
		- Limits
			- Not available for Enterprise workspace Sites at launch.
			- Availability is stated as "where available". The sources I found do not give a per-plan list.
			- A custom domain does not change who can view the Site. It stays public or limited to signed-in invited users.
		- Not verified
			- OpenAI's help center article, [Creating and using ChatGPT Sites](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites), returned HTTP 403 to my fetch, so the steps above come from secondary write-ups that cite it. Check it directly before relying on the Enterprise or plan details.
			- The DNS record types and whether HTTPS is issued automatically are shown only in the connection flow, per Stacktree, so they are not confirmed here.
