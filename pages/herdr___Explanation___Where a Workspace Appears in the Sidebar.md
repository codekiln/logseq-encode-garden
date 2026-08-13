tags:: [[herdr]], [[Diataxis/Explanation]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[herdr/Explanation/Where Input Box Text Comes From]], [[git/worktree]], [[AI/Coding/Idea/26/08/Standing agent inboxes on long-lived worktrees]]

- # Where a workspace appears in the sidebar
	- Behaviour read from the [herdrdev/herdr](https://github.com/herdrdev/herdr) source at [952729ee preserve logical lines in scrollback editor](https://github.com/herdrdev/herdr/commit/952729ee) — `herdr 0.8.0`, `preview-2026-08-04-d78e3d3b5126-90-g952729ee`. Every line reference below is read from that source; nothing here is a figure measured against a running session.
	- ## Overview
		- The workspace list is flat, with one exception: a **worktree group**, drawn as one un-indented parent row with its members indented beneath it. There is no general tree, and no workspace carries a "parent workspace" field.
		- A group is the set of workspaces that agree on one string — the absolute path of the repository's shared Git directory. Placement follows from that string and nothing else.
		- So the indent carries a specific meaning: these checkouts share one `.git` directory. Closing, close confirmation, dragging, and collapsing all act on the group that meaning defines.
	- ## The rule, in one pass
		- Every frame, herdr rebuilds the list from scratch (`src/ui/sidebar.rs:338-436`). The whole derivation is four steps:
			- 1. Bucket every workspace that has a `worktree_space` membership by that membership's `key`. A workspace with no membership is never bucketed.
			- 2. A bucket becomes a **group** only if it holds two or more workspaces *and* at least one of them has `is_linked_worktree == false` (`src/ui/sidebar.rs:348-357`).
			- 3. The **parent** is the first member in workspace order with `is_linked_worktree == false` (`src/ui/sidebar.rs:395-399`). It is not stored anywhere; it is picked fresh each frame.
			- 4. The group is emitted at the position of whichever member the iteration reaches first — parent row un-indented, then every other member indented, in workspace order.
		- Two things follow. A group of linked worktrees whose parent workspace has been closed collapses back to a flat list, because step 2 fails. And a lone worktree opened with no parent workspace present also stays flat, for the same reason.
	- ## Mechanism
		- ### The group key is a path to a Git directory
			- `WorktreeSpaceMembership` holds five fields — `key`, `label`, `repo_root`, `checkout_path`, `is_linked_worktree` (`src/workspace.rs:35-41`).
			- `key` is the absolute, symlink-resolved path of `git_common_dir`, written out as a string (`src/workspace/git/discovery.rs:71-77`). For an ordinary clone that is `<repo>/.git`. A linked [[git/worktree]] reports the same common directory, which is why a worktree and its repo land in one bucket.
			- The key is a filesystem fact about Git, not a herdr identifier. Two checkouts of the same remote cloned twice have two different keys and never group.
		- ### Membership is a stored field, but only the worktree actions write it
			- `worktree_space: Option<WorktreeSpaceMembership>` is a real field on the workspace (`src/workspace.rs:198`), and it is persisted in the session snapshot (`src/persist/snapshot.rs:57`, written at `:293`).
			- Exactly one function writes it — `set_worktree_membership` (`src/app/api/worktrees.rs:449-471`) — and every caller builds its argument through `worktree_membership` (`:705-717`), which copies `key`, `label` and `repo_root` verbatim out of a `WorktreeSource`.
			- A `WorktreeSource` is only ever produced by resolving a repository: from a workspace's own membership or its Git metadata (`src/app/api/worktrees.rs:282-325`), or from a `--cwd` path (`:204-217`). Both refuse a linked worktree as the source, with the error `linked_worktree_source` and the message "New and open worktree actions start from the repo parent workspace." The equivalent TUI entry point refuses identically (`src/app/worktrees.rs:14-77`).
			- So the field is stored, but no one chooses its value. It holds a fact about Git, and the only writer works that fact out from Git.
		- ### Opening a worktree stamps two workspaces, and picks the parent by key
			- `worktree open` first resolves the source repo, then finds the target among `git worktree list` output for that repo root only (`src/app/api/worktrees.rs:473-487`). A path outside the source repository returns `worktree_not_found`; there is no way to name a checkout belonging to a different repository.
			- Before opening the child, `ensure_source_parent_membership` locates the parent (`:380-399`). It looks up `find_parent_workspace_by_key` — the first workspace whose membership *or* Git metadata carries that key with `is_linked_worktree == false` (`:427-435`) — and if none exists, it **creates one at the repo root**. That is why running the command from an unrelated workspace produces a new repo workspace rather than nesting under the caller.
			- If the target checkout is already open as a plain, ungrouped workspace, no new workspace is created. That workspace is found by path and **adopted in place** — the membership is stamped onto it and it joins the group where it already sits, and the response returns its existing id with `already_open` set. The lookup matches on the membership's checkout path, on the workspace's Git checkout key, or on the directory it resolves to (`:569-596`), so a workspace whose pane simply sits in the worktree qualifies.
			- A worktree created with plain `git worktree add` and opened as an ordinary workspace can therefore be brought into a group afterwards, without losing the panes already running in it. The repo's own `worktree open` is the only thing that does it.
		- ### A restart re-checks the membership against Git
			- On restore, a persisted membership is re-validated before it is accepted: the `checkout_path` must still exist, and `git_space_metadata(checkout_path).key` must still equal the stored `key` (`src/persist/restore.rs:436-443`). Anything else is dropped and the workspace comes back flat.
			- The check is against the membership's own `checkout_path`, not against the directories the workspace's panes are in. A workspace's placement is therefore governed by the checkout its membership names, and that checkout's real Git identity is verified every session.
		- ### Repository identity comes from one pane, not from all of them
			- A workspace's Git identity is resolved from the first tab's root pane, falling back to the directory the workspace was created in (`src/workspace.rs:1101-1110`). Panes that later `cd` elsewhere, and panes in other tabs, do not contribute.
			- This is separate from membership. A workspace can report no repository at all and still sit in a group, if it holds a membership; and it can sit squarely inside a repository and stay flat, if it does not.
	- ## What the indent controls
		- Closing a group's parent closes **every member of the group**, not just the parent row (`src/app/actions.rs:1678-1698`). When `confirm_close` is on, the same key lookup drives the confirmation prompt, and a `tab close` or `pane close` that would take the parent's last tab returns `confirmation_required` instead (`src/app/actions.rs:1987-2002`).
		- Dragging a group in the sidebar moves the whole block, and a linked-worktree child refuses to be dragged out of its group at all (`src/app/input/sidebar.rs:383-464`).
		- The API surface reflects the same shape: `workspace.move` takes an `insert_index` and `workspace.move_block` takes a list of ids (`src/api/schema/workspaces.rs:26-36`). Both reorder. Neither re-parents.
		- Taken together, the indent tells you which workspaces close as a unit and which move as a unit. Making it settable would change what those actions do.
	- ## Predicting placement
		- | Workspace                                                     | Membership  | Placement                             |
		  | ------------------------------------------------------------- | ----------- | ------------------------------------- |
		  | created with `workspace create` in any directory              | none        | flat, always                          |
		  | a `git worktree add` checkout opened as an ordinary workspace | none        | flat, until `worktree open` adopts it |
		  | repo workspace, no worktrees open                             | key, parent | flat — the bucket has one member      |
		  | repo workspace with one or more of its worktrees open         | key, parent | un-indented parent of that group      |
		  | a worktree opened via `worktree open` or `worktree create`    | key, linked | indented under its repo's workspace   |
		  | a worktree whose repo workspace was closed                    | key, linked | flat — no non-linked member remains   |
		- Two workspaces in the same repository do **not** group merely by being in the same repository: without a membership, step 1 never buckets them. Grouping is opt-in through the worktree actions.
	- ## Workspaces that supervise several repositories
		- A workspace that oversees worktrees belonging to more than one repository cannot have all of them nest beneath it. This is a consequence of the derivation rather than a missing option.
			- The want behind it is organisational — these checkouts belong together because one operator watches them. The mechanism answers a different question, and only that one: do these checkouts share a `.git`. It is the same gap between what herdr can observe and what a reader wants the display to mean that runs through [[herdr/Explanation/Where Input Box Text Comes From]].
			- A group is a bucket over a single `key`, and `key` is one Git directory path. Three repositories are three keys and therefore three buckets, and a workspace holds at most one membership. It can be the parent of at most one group.
			- The one thing that does work today: a supervising workspace whose own directory is inside one of those repositories becomes that repository's parent as soon as a worktree is opened with it as the source, because `ensure_source_parent_membership` stamps the source workspace itself when its key matches. One of the three nests; the other two form their own groups.
		- `workspace report_metadata` is not a way around it. It carries only free-text tokens with an optional TTL (`src/api/schema/workspaces.rs:39-49`), those tokens are read solely when rendering a row's text (`src/ui/sidebar.rs:207`), and they are not restored with the session. Nothing in the grouping pass reads them.
	- ## What a change would have to touch
		- Nesting independent of repository would mean a second, presentational grouping key: an optional field on the workspace, an API method to set it, a snapshot field, and a restore path that deliberately skips the Git re-validation — since the whole point would be a group that is not a Git fact.
		- The grouping pass itself is a small edit; `workspace_list_entries_inner` would bucket on the override and fall back to the membership key. The cost is everywhere else. Around sixty call sites across eleven files read `worktree_space()`, and they split into two kinds that a single field would conflate: rendering (row layout, collapse state at `src/ui/sidebar.rs:260-280`, child labels at `:284-301`, the dialogs, the mobile switcher) and behaviour (worktree source resolution, remove, focus-parent-after-remove, drag and mouse routing, the group close and its confirmation, and the `worktree` block of the workspace API at `src/app/creation.rs:507-515`).
		- Letting the override reach the behavioural sites causes real damage: closing a parent would close workspaces in unrelated repositories, and `worktree remove` would hand focus to a workspace in some other repo. Keeping it to rendering only is safe, but then the indent stops telling you which workspaces close together, which is most of what it is for today.
	- ## Misconceptions
		- **"Nesting follows the repository a workspace sits in."** It follows a stored membership that only the worktree actions write. Two workspaces inside one clone stay flat until one of them is opened as a worktree of the other.
		- **"`--workspace` chooses where the result appears."** It names the source to branch from, and it must resolve to a non-linked checkout. The destination is then found by key, which may be an entirely different workspace, or a newly created one.
		- **"`worktree open` always creates a workspace."** Run against a checkout that is already open, it adopts that workspace instead and hands back the same id. Registering an existing pane's worktree in place is the normal path, not a special one.
		- **"The parent is recorded when the group forms."** It is recomputed every frame as the first non-linked member in workspace order. Reordering the list can change which row is drawn as the parent.
		- **"A label or metadata token can hint at placement."** Labels and tokens are row text. The grouping pass reads neither.
		- **"Editing what herdr stored would move a workspace."** It would, until the next restart. Restore drops any membership whose checkout no longer reports the stored key, so every session starts from what Git says.
		- **"The indent is cosmetic."** Closing the parent row closes every member of the group.
