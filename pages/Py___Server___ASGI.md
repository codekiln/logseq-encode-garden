tags:: [[Diataxis/Explanation]], [[Server]], [[Specification]] 
alias:: [[ASGI]]

- # ASGI (Asynchronous Server Gateway Interface) — Conceptual Overview
	- ## Overview
		- **Definition** – ASGI is a Python-specific interface that standardises how async-capable web servers hand off requests to applications, covering HTTP/1.1, HTTP/2, and WebSocket, while remaining compatible with traditional WSGI apps. See the official [ASGI documentation](https://asgi.readthedocs.io/en/latest/).
	- ## Context
		- **Why ASGI?** WSGI assumes a single, synchronous request–response cycle, which limits long-lived connections and efficient parallel I/O. Modern use-cases—streaming APIs, WebSockets, HTTP/2 multiplexing—demand an asynchronous gateway.
		- **Origins** – Conceived by Andrew Godwin in the Django Channels project (2016) as “codenamed ASGI”, later formalised into the 2019 ASGI 3.0 spec [[PyBay-talk slides](https://speakerdeck.com/pybay/2016-andrew-godwin-django-channels-and-distributed-systems)].
	- ## Key Principles
		- **Async-first, Sync-friendly** – Enables `async` handlers but provides adapters so classic WSGI apps still run.
		- **Protocol-agnostic Core** – The spec defines a generic *scope/receive/send* triad; protocols (HTTP, WebSocket) are layered on top.
		- **Minimal Surface** – A small, typed dictionary‐based contract keeps servers and frameworks decoupled.
	- ## Mechanism
		- ### 1. Scope
			- Immutable dict describing the connection (`type`, headers, HTTP version, client IP, etc.).
		- ### 2. `receive()`
			- Awaitable that yields incoming events (e.g., request body chunks, WebSocket messages).
		- ### 3. `send()`
			- Awaitable to emit outgoing events (response headers, body, WebSocket frames).
		- ### Example
			- ~~~python
			  async def app(scope, receive, send):
			      assert scope["type"] == "http"
			      await send({"type": "http.response.start",
			                  "status": 200, "headers": [[b"content-type", b"text/plain"]]})
			      await send({"type": "http.response.body",
			                  "body": b"Hello, ASGI!"})
			  ~~~
	- ## ASGI vs WSGI
		- **Concurrency Model** – ASGI uses [[Py/asyncio/Event Loop]]s; WSGI spawns (threads|processes).
		- **Protocol Support** – WSGI: HTTP/1.1 only. ASGI: HTTP/1.1, HTTP/2, WebSocket (*spec*); HTTP/3 via server extensions (e.g., [[Hypercorn]]) [Hypercorn docs](https://hypercorn.readthedocs.io/en/latest/).
		- **Long-lived Streams** – WebSockets & server-push viable in ASGI; need work-arounds (e.g., polling) in WSGI.
		- **Backward Compatibility** – ASGI provides a WSGI wrapper, letting legacy frameworks run unchanged.
	- ## Common ASGI Servers
		- **Uvicorn** – High-performance asyncio/uvloop server; supports HTTP/1.1 & WebSockets [Uvicorn site](https://www.uvicorn.org/).
		- **Daphne** – Original Channels server; supports HTTP/1.1, HTTP/2, WebSockets [Django docs](https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/daphne/).
		- **[[Hypercorn]]** – Sans-IO design, HTTP/1 → HTTP/3, WebSockets, optional Trio workers [PyPI](https://pypi.org/project/Hypercorn/).
		- **bareASGI / others** – Experimental servers showcasing QUIC/HTTP-3 [bareASGI guide](https://rob-blackbourn.github.io/bareASGI/4.0/user-guide/h3/).
	- ## What the Spec *Does & Doesn’t* Include
		- **Included**
			- HTTP/1.1 request–response cycle.
			- HTTP/2 streams (header ordering & multiplexing guidance).
			- WebSocket handshake and message events.
		- **Not Explicitly Included**
			- **Server-Sent Events (SSE)** – Possible at framework level; not mentioned in the core spec [Community discussion](https://github.com/encode/uvicorn/discussions/2635).
			- **HTTP/3 / QUIC** – Outside 3.0 spec; available through server implementations (Hypercorn with `aioquic`).
	- ## Outside the Python Ecosystem?
		- **Name-scope** – ASGI is tightly bound to Python’s `asyncio` & typing; other languages use different gateways (e.g., Node’s `http` module, Go’s `net/http`). Referring to “ASGI” in non-Python contexts is uncommon; instead, concepts like “async middleware” or “actor gateways” are used.
	- ## Misconceptions
		- “ASGI replaces WSGI entirely” → It *extends* rather than replaces; many stacks run both side-by-side.
		- “ASGI natively handles SSE” → Not in spec; frameworks implement SSE atop HTTP streaming.
		- “All ASGI servers support HTTP/3” → Only some (Hypercorn) do; others remain HTTP/1.1 + WebSocket.
	- ## Related
		- [[WSGI]] · [HTTP/3 explainer](https://www.cloudflare.com/learning/performance/http3/) · [Django Channels](https://channels.readthedocs.io/)