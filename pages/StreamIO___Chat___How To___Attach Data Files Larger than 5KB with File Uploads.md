# How to attach data files larger than 5KB using [[StreamIO/Chat/File/Upload]]
	- ## Summary
		- Assumption: we don't want to show the file to the users for download, we just want to access the data to customize rendering in a react client.
		- ### 1 - Server uploads file to channel
			- call `stream_chat.channel.Channel.send_file` ([[StreamIO/Chat/Channel/Channel/send_file]])
				- ```python
				  def send_file(
				      self, url: str, name: str, user: Dict, content_type: str = None
				  ) -> StreamResponse:
				      return self.client.send_file(  # type: ignore
				          f"{self.url}/file", url, name, user, content_type=content_type
				      )
				  ```
				- #### What is the `url` parameter here and what values are valid to pass to it? ANS: path to local file or URL to remote file
				  collapsed:: true
					- Here, [the async version](https://github.com/GetStream/stream-chat-python/blob/dcd4d960db4984b7bfbe02906176af6f1e9d12d7/stream_chat/async_chat/client.py#L492-L518) of `send_file` is either reading the file locally or it is reading it from a URL. This is actually passing parameters to [[aiofile/AIOFile]] which takes a path in the case that [[Py/urllib/parse/urlparse]] returns `parts[0] == ""`:
						- ```python
						  async def send_file(
						      self, uri: str, url: str, name: str, user: Dict, content_type: str = None
						  ) -> StreamResponse:
						      ...
						      parts = urlparse(url)
						      if parts[0] == "":
						          async with AIOFile(url, "rb") as f:
						              content = await f.read()
						      else:
						          async with self.session.get(
						              url, headers={"User-Agent": "Mozilla/5.0"}
						          ) as content_response:
						              content = await content_response.read()
						      data = FormData()
						      ...
						      data.add_field("file", content, filename=name, content_type=content_type)
						      async with self.session.post(
						          "/" + uri.lstrip("/"),
						          params=self.get_default_params(),
						          data=data,
						          headers=headers,
						      ) as response:
						          return await self._parse_response(response)
						  ```
						- This is a little bit inconvenient if you need to construct a file on the fly. [[aiofile/AIOFile]] has `aiofile.aio.AIOFile.from_fp()` which takes as a parameter `FileIOType = Union[TextIO, BinaryIO]`, but this isn't available here; one would likely need to write to a temp file in order to pass a file path to the constructor of `AIOFile`.
				- #### What's a sample invocation of `Channel.send_file()` with writing a large dictionary to temp json file?
					- This example uses [[aiofiles/tempfile/NamedTemporaryFile]] - note that `aiofiles` is a different library from [[aiofile]] used by [[StreamIO/Chat/PySDK]].
						- ```python
						  import json, aiofiles.tempfile
						  from stream_chat.async_chat import StreamChatAsync
						  
						  big_payload = {...}
						  
						  async with aiofiles.tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as tmp:
						      await tmp.write(json.dumps(big_payload))
						      path = tmp.name            # keep after context exit
						  
						  async with StreamChatAsync(api_key="STREAM_KEY", api_secret="STREAM_SECRET") as chat:
						      chan = chat.channel("messaging", "general")
						      file_url = await chan.send_file(path, name="big_payload.json",
						                           user={"id": "system"},
						                           content_type="application/json")
						  
						  
						  ```
		- ### 2 - Store a reference to uploaded file in the attachments to a message
			- [[StreamIO/Chat/Channel/Channel/send_file]] (`stream_chat.channel.Channel.send_file`) returns a file reference. See [[StreamIO/Chat/REST/channels/TYPE/ID/file]] [here](https://getstream.io/chat/docs/rest/#/product%3Achat/UploadFile) for the response schema:
				- ```json
				  {
				    "duration": "string",
				    "file": "string",
				    // the following is for images
				    "thumb_url": "string"
				  }
				  ```
			-