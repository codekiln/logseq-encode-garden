# Constructing a Logseq asset link

Read `Logseq/Entity/Asset` for filename mapping and `Logseq/Entity/Asset/B2`
for remote locations. Keep one naming authority in those graph pages.

## Existing file paths

Calculate the path relative to the page's `pages/` directory. A file at
`<garden>/assets/Folder/File.pdf` becomes:

```markdown
[File](../assets/Folder/File.pdf)
```

Use `![label](location)` for images, audio, and video; use `[label](location)`
for downloadable documents and presets. Percent-encode URL characters in link
locations without changing the file's name.

## New asset pages

Derive the flat filename from the asset page using the entity definition.
For remotely stored files, the optional local copy is under `assets/.remote/`
and the B2 URL uses that filename directly beneath the garden's bucket.

```markdown
![September 24 episode recording](../assets/.remote/GitP___A___Session___26___09___24-Thu___Asset___Synth___Full.mp3)
```

## Direct file links

When explicitly requested for a file outside the garden, use a direct file URL:

```markdown
[Recording](file:///Users/username/Documents/recording.wav)
```

Return copyable link syntax when asked to construct a link. When writing an asset
page, write the usable link directly into its body.
