# Worked example: Chapter 4, section 4.1

## Pages involved

| Logical page | Disk file |
| --- | --- |
| `[[LV4AD/Ch/04 Opening Files]]` | `LV4AD___Ch___04 Opening Files.md` |
| `[[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers]]` | `LV4AD___Ch___04 Opening Files___01 Introducing File Pickers.md` |
| `[[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers/Fastest Way to Close LazyVim]]` | `LV4AD___Ch___04 Opening Files___01 Introducing File Pickers___Fastest Way to Close LazyVim.md` |

The section subpage is the **source page**; the card is a direct child title
under it — same shape as `[[Source/Page/Short Card Title]]` on
`[[Logseq/Entity/Card]]`, without a `/Card/` segment.

## Card page (factored)

```
logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Keyshort]]

- ### What is the fastest [[Keyshort]] to close [[LazyVim]]? [[card]]
  card-last-interval:: 5.62
  card-repeats:: 1
  card-ease-factor:: 2.6
  card-next-schedule:: 2026-09-20T20:13:53.103Z
  card-last-reviewed:: 2026-09-15T06:13:53.104Z
  card-last-score:: 5
	- `<leader> qq`
	- it's fastest because we don't have to hit shift to get `:`, also the space leader is easier than `:`
```

## Section page (embed replaces inline card)

```
- [4.1 Introducing File Pickers](https://lazyvim-ambitious-devs.phillips.codes/course/chapter-4/#_introducing_file_pickers)
	- [[nvim/Plugin/snacks.nvim/Picker]] is written by [[Person/Folke Lemaitre]], creator of LazyVim
	- {{embed [[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers/Fastest Way to Close LazyVim]]}}
	- …remaining inline [[card]] blocks until factored…
```

## Chapter page (provenance embed under highlight)

Section heading cross-links the section deck:

```
- ## [4.1. Introducing File Pickers](…#_introducing_file_pickers) (My Notes: [[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers]])
```

Provenance: highlight that teaches `Space q q` gets the embed as a child:

```
	- > So close [[nvim]] with `Space q q`
		- {{embed [[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers/Fastest Way to Close LazyVim]]}}
```

## Provenance matching hints (same section)

| Card short title (candidate) | Match highlight by |
| --- | --- |
| Fastest Way to Close LazyVim | `Space q q` / close Neovim |
| Activate File Picker Keyshorts | `Space Space`, `<Space>ff`, Find Files (Root Directory) |
| File Picker Smart Case | smart case / case insensitive picker search |

## Multi-answer card (section 4.4)

When two answers differ by scope or role, number both the prompt and answer
bullets. Example: `[[LV4AD/Ch/04 Opening Files/04 Mini.files Alternative/Open Mini.files Keyshorts]]`

```
- ### 1. What [[Keyshort]] opens [[nvim/Plugin/mini.files]] at the directory of the current file, and 2. what [[Keyshort]] opens it at the current working directory? [[card]]
	- 1. `<leader>fm` — opens at the directory containing the file in the active buffer
	- 2. `<leader>fM` — opens at Neovim's current working directory (cwd); not the same root/cwd split as picker/explorer until customized ([[LV4AD/Ch/05 Plugin Basics]])
```

Same pattern for picker/explorer pairs: `[[LV4AD/Ch/04 Opening Files/01 Introducing File Pickers/Activate File Picker Keyshorts]]` (two keyshorts + command name).
