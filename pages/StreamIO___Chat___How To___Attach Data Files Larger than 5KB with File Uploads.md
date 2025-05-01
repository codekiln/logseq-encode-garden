# How-to: attach a JSON (or any binary) file > 5 KB to an existing Stream Chat message
	- *Diátaxis — How-to guide*
	- ## Problem
		- You already have a message in a Stream Chat channel and you want to:
			- 1. Serialize a large Python object to JSON (or other format)
			- 2. Upload the resulting file to Stream's CDN
			- 3. Add the signed file URL as an attachment **to that existing message**
	- ## Prerequisites
		- | Requirement | Value |
		  |-------------|-------|
		  | Python      | 3.8 + |
		  | Packages    | `stream-chat>=5`, `aiofiles`, `python-dotenv` |
		  | Environment | `STREAM_APP_KEY`, `STREAM_APP_SECRET` set |
		  | Channel cfg | `uploads: true` (the helper will enable it if missing) |
	- ## High-level flow
		- ~~~mermaid
		  flowchart TD
		      A["Payload (dict/str)"] --> B["Helper: upload_json_as_attachment"]
		      B --> C["Temp file (NamedTemporaryFile delete=false)"]
		      C --> D["channel.send_file(tmp_path)"]
		      D --> E["partial_update_message adds attachment"]
		      E --> F["Signed CDN URL visible to members"]
		  ~~~
	- ## Implementation
		- ### 1. Define a reusable helper
			- Create a small utility so you can call one function instead of repeating the boilerplate:
			- ~~~python
			  import json, os, aiofiles.tempfile, contextlib
			  from stream_chat.async_chat import StreamChatAsync
			  from stream_chat.base.exceptions import StreamAPIException
			  
			  async def upload_json_as_attachment(
			      chat: StreamChatAsync,
			      channel_type: str,
			      channel_id: str,
			      message_id: str,
			      attachment_name: str,
			      payload: dict | str,
			      user_id: str,
			  ):
			      """
			      • Serializes *payload* to JSON (if dict)  
			      • Writes it to a temp file  
			      • Uploads via channel.send_file  
			      • Adds the file as an attachment to *message_id*  
			      • Returns the Stream API response
			      """
			      channel = chat.channel(channel_type, channel_id)
			  
			      # 1 write payload
			      async with aiofiles.tempfile.NamedTemporaryFile(
			          "w", suffix=".json", delete=False
			      ) as tmp:
			          text = json.dumps(payload) if isinstance(payload, dict) else str(payload)
			          await tmp.write(text)
			          await tmp.flush()
			          tmp_path = tmp.name
			  
			      # 2 upload temp file
			      try:
			          resp = await channel.send_file(
			              tmp_path,
			              name=f"{attachment_name}.json",
			              user={"id": user_id},
			              content_type="application/json",
			          )
			      except StreamAPIException as exc:
			          # Enable uploads on the fly if needed
			          if "upload disabled" not in str(exc):
			              raise
			          await channel.update_partial({"config_overrides": {"uploads": True}})
			          resp = await channel.send_file(
			              tmp_path,
			              name=f"{attachment_name}.json",
			              user={"id": user_id},
			              content_type="application/json",
			          )
			  
			      # 3 attach to message
			      url = resp["file"]
			      attachment = {
			          "type": "file",
			          "url": url,
			          "name": f"{attachment_name}.json",
			          "asset_url": url,
			          "mime_type": "application/json",
			      }
			      await chat.partial_update_message(
			          message_id,
			          {"set": {"attachments": [attachment]}},
			      )
			  
			      # 4 clean up temp file
			      with contextlib.suppress(FileNotFoundError):
			          os.remove(tmp_path)
			  
			      return url
			  ~~~
		- ### 2. Use the helper in your async workflow
			- ~~~python
			  import asyncio, uuid, os
			  from stream_chat.async_chat import StreamChatAsync
			  
			  STREAM_APP_KEY    = os.getenv("STREAM_APP_KEY")
			  STREAM_APP_SECRET = os.getenv("STREAM_APP_SECRET")
			  
			  async def main():
			      chat = StreamChatAsync(api_key=STREAM_APP_KEY, api_secret=STREAM_APP_SECRET)
			  
			      CHANNEL_TYPE = "messaging"
			      CHANNEL_ID   = "existing-channel"
			      MESSAGE_ID   = "existing-message"
			      USER_ID      = "system"
			  
			      # Example large payload
			      payload = {"id": str(uuid.uuid4()), "records": [{"foo": "bar"}] * 1_000}
			      name    = f"data_{payload['id']}"
			  
			      url = await upload_json_as_attachment(
			          chat,
			          CHANNEL_TYPE,
			          CHANNEL_ID,
			          MESSAGE_ID,
			          name,
			          payload,
			          user_id=USER_ID,
			      )
			      print("Attachment URL:", url)
			  
			      await chat.close()
			  
			  asyncio.run(main())
			  ~~~
	- ## How it works
		- | Step | Detail |
		  |------|--------|
		  | 1    | A temp file (`delete=False`) stores the serialized payload so `send_file` can reopen it. |
		  | 2    | `channel.send_file` uploads the file; if uploads are disabled the helper enables them then retries. |
		  | 3    | The returned CDN URL is injected into the message's `attachments` array with `partial_update_message`. |
		  | 4    | Temp file is removed afterwards. |
	- ## Access control & link expiry
		- *Stream CDN links are signed:*
			- **Scope:** the specific channel and the current set of permissions
			- **Lifetime:** ~5 minutes; refresh automatically when re-fetching the message list
			- **Revocation:** deleting the message, file, or channel invalidates existing links
			- **Visibility:** only authenticated channel members can fetch; others receive **401**
	- ## Troubleshooting
		- | Symptom | Cause & fix |
		  |---------|-------------|
		  | `StreamAPIException … upload disabled` | Channel type config has `"uploads": false`. The helper flips it with `update_partial` automatically. |
		  | `FileNotFoundError` during upload | Make sure `delete=False`; do not remove the temp file before `send_file` completes. |
		  | CDN link returns 401 for some users | They must be authenticated **and** a member of the channel. |
	- ## References
		- Stream Chat docs → *File Uploads › Access control and link expiration*