see-also:: [[Logseq/Entity/Asset/B2]], [[Asset/Mount]]

- Binary files, such as recordings, Ableton Sets, presets, images and PDFs, go to B2 through DVC. Git tracks the `.dvc` file beside each one. This matters most in the [[GitP]] namespace, where Sets and recordings are large and change often.
- In this garden, the file gets an asset page named per [[Logseq/Entity/Asset]]. [[Asset/mise/Task/add]] tracks it, [[Asset/mise/Task/push]] backs it up, and [[GitP/mise/Task/media/upload]] uploads the named copy the page links. Pages link the working copy at `../assets/.remote/<mount>/<file>`.
- A garden that borrows a mount links the owning garden's mounted file, as [[Asset/Mount]] describes.
- A binary already committed to git moves the same way: track it with DVC, point its links at the mounted copy, then `git rm` the old file.