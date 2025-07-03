tags:: [[Diataxis/How To]], [[WIP]]

- # How can we obtain a #Metric for how long a user spent engaged with a [[StreamIO/Chat/Channel]]?
	- [Event Object - Python Chat Messaging Docs](https://getstream.io/chat/docs/python/event_object/)
		- While it's a bit strange to think about when using #Python on a #Server, it's possible to have any client listen for `connection.changed` and `connection.recovered` events.
			- | **Event** | **Trigger** | **Recipients** | **Type** |
			  | ------------- | -------------- | ---- |
			  | `connection.changed` | when the state of the connection changed | local event | client event |
			  | `connection.recovered` | when the connection to chat servers is back online | local event | client event |
		- For example, in [[StreamIO/Chat/ReactSDK]], there's a [Connection Status - React Chat Messaging Docs](https://getstream.io/chat/docs/sdk/react/guides/theming/connection_status/) which enables figuring out when the connection drops. This could be sent back to a server API.