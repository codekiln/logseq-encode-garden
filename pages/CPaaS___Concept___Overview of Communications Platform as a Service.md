tags:: [[Diataxis/Explanation]], [[Communications]]

- # Communications Platform as a Service (CPaaS)
	- [[tldr]] **CPaaS** = specific service model delivering programmable [[Communications]] [[API]]s
	- CPaaS refers to a category of cloud-based platforms that enable the integration of real-time communication features—such as voice, video, messaging, and chat—into software applications via APIs and SDKs. These platforms abstract away the complexity of telecommunication infrastructure and provide developers with programmable interfaces to embed communications directly into their products.
- ### Explanation
	- The emergence of CPaaS represents a shift from rigid, hardware-based communication systems toward flexible, software-defined interfaces. CPaaS platforms allow teams to integrate communication modalities without managing physical infrastructure or carrier relationships. The approach promotes rapid development of communication features within web, mobile, and backend applications.
	- Several interrelated terms and concepts define the ecosystem:
		- **[[CPaaS]] ([[Communications/Platform]] as a Service)**: Cloud-hosted APIs for integrating voice, SMS, video, and chat.
			- Examples: Twilio, Vonage, Sinch, Infobip
		- **[[UCaaS]] ([[Communications/Unified]] as a Service)**: Broader offering than CPaaS, bundling internal communications like conferencing, VoIP, and messaging into a unified business service.
			- Examples: [[RingCentral]], [[Zoom]], [[Cisco/Webex]]
		- **[[RTC]] (Real-Time Communication)**: A category of technology enabling real-time voice/video/chat over IP networks.
			- Often implemented via [[WebRTC]], a standard for browser-native RTC.
		- **Programmable Communications**: Describes the model of exposing communication functions through developer-friendly APIs.
		- **Omnichannel Messaging**: The capability to send and receive messages over multiple channels (e.g., SMS, WhatsApp, email, Facebook Messenger) from a unified interface.
- ### Typical Capabilities
	- [[CPaaS]] and related platforms typically provide:
		- Voice (PSTN and [[VoIP]])
		- [[Video/Service]] (1:1, group, broadcasting)
		- [[SMS]] and MMS
		- [[Chat]] / In-app messaging
		- [[Email]]
		- [[Notification/Push]] Push notifications
		- Call routing / IVR (Interactive Voice Response)
		- Authentication (e.g., One-Time Passcodes, Multi-Factor Authentication)
		- Phone number masking
- ### #Examples by Focus Area
	- | Platform | Focus Area(s) |
	  | [[Twilio]] | Broad CPaaS — voice, messaging, video, auth |
	  | Vonage | CPaaS with strong video + voice |
	  | Sinch | Global SMS, WhatsApp, verification |
	  | [[StreamIO]] | In-app chat and activity feeds |
	  | Agora | Low-latency real-time audio/video, mobile focus |
	  | Daily | Fast-start WebRTC video SDKs |
	  | MessageBird | Omnichannel messaging |
	  | [[Cisco/Webex]] | UCaaS/CPaaS hybrid for enterprise |
-