- # Problem Summary
  - In a tmux + Vim/Neovim workflow running inside iTerm2 on macOS, keyboard input typed in the **right pane** is visually rendered in the **left pane**.
  - This is not synchronize-panes (confirmed off).
  - The issue makes Vim nearly unusable because typed characters appear in the wrong pane despite focus being correct.
- # Environment
  - macOS
  - iTerm2
  - tmux 3.6a
  - `$TERM` outside tmux: `xterm-256color`
  - `$TERM` inside tmux: `tmux-256color`
  - `synchronize-panes`: off
  - `paste` mode in Vim: off
  - `assume-paste-time`: 1
  - Using Vim or Neovim in split panes
- # Observed Behavior
  - Two panes in tmux.
  - Vim running in right pane.
  - Insert mode active in right pane.
  - Characters typed appear in left pane display buffer.
  - Cursor visually remains in right pane.
  - No synchronize-panes enabled.
  - This suggests a **terminal rendering desynchronization**, not actual input duplication.
- # What Is *Not* the Cause
  - Not tmux synchronize-panes.
  - Not basic `$TERM` mismatch.
  - Not Vim paste mode.
  - Not basic keybinding duplication.
  - Not shell prompt misbehavior.
- # Most Likely Root Cause
  - Terminal focus-event or extended key negotiation desync between:
    - tmux ≥ 3.4 (3.6a in use)
    - iTerm2
    - Alternate screen apps (Vim)
  - tmux 3.6 tightened terminal feature negotiation, including:
    - Focus events
    - Extended keys
    - Bracketed paste
    - Terminal passthrough
    - Alternate screen behavior
  - iTerm2 partially supports some of these but can enter a bad state where:
    - Pane focus tracking is wrong
    - Cursor rendering and input routing diverge
    - Escape sequences leak across panes
  - The symptom (input displayed in wrong pane but not truly sent there) matches known focus-event and extended-key glitches.
- # Hypothesis Ranking
  - **focus-events enabled + iTerm2 bug**
  - **extended-keys negotiation bug**
  - **allow-passthrough misbehavior**
  - **alternate-screen rendering issue**
  - **iTerm2 session-level focus reporting**
- # Reproduction Isolation Plan
  - ## Step 1 — Clean tmux
    - ~~~
      tmux -L clean -f /dev/null
      ~~~
    - No config.
    - Split panes.
    - Run Vim in right pane.
    - Test input.
    - If problem disappears → configuration issue.
    - If problem persists → iTerm2 issue.
  - ## Step 2 — Disable tmux advanced features
    - Add to `.tmux.conf`:
    - ~~~
      set -g focus-events off
      set -g extended-keys off
      set -g allow-passthrough off
      set -g assume-paste-time 0
      set -g mouse off
      ~~~
    - Restart tmux fully:
    - ~~~
      tmux kill-server
      ~~~
    - Test again.
  - ## Step 3 — Disable alternate screen
    - Temporarily:
    - ~~~
      set -g alternate-screen off
      ~~~
    - If issue disappears, rendering negotiation is failing.
  - ## Step 4 — iTerm2 Settings Audit
    - In iTerm2:
    - Preferences → Advanced:
      - Disable:
        - Report Terminal Focus
        - Allow session to receive focus events
        - Applications may access clipboard
    - Preferences → Profiles → Terminal:
      - Uncheck "Report terminal focus"
    - Restart iTerm2 completely.
  - ## Step 5 — Force terminal compatibility downgrade
    - In `.tmux.conf`:
    - ~~~
      set -g default-terminal "screen-256color"
      ~~~
    - Instead of:
    - ~~~
      tmux-256color
      ~~~
    - Restart and test.
    - If problem disappears, terminfo capability mismatch is the trigger.
- # Deep Diagnostic Commands
  - Run inside tmux:
  - ~~~
    tmux info
    tmux show -g
    tmux show-window-options -g
    infocmp tmux-256color
    ~~~
  - Run outside:
  - ~~~
    infocmp xterm-256color
    ~~~
  - Compare:
    - Ms
    - Tc
    - Focus capability
    - Smkx / Rmkx
    - XT
    - RGB
  - Look for capability mismatch.
- # Underlying Technical Explanation
  - tmux tracks pane focus and rendering independently from terminal focus.
  - If:
    - Focus events are misreported,
    - Or extended key mode negotiation is incomplete,
    - Or alternate screen state desyncs,
  - then tmux may:
    - Route input to correct pane internally,
    - But terminal rendering buffer may attach to wrong pane,
    - Causing characters to visually appear in another pane.
  - This is a rendering synchronization fault, not input duplication.
- # Recommended Fix Order
  - Disable focus-events.
  - Disable extended-keys.
  - Downgrade default-terminal to screen-256color.
  - Disable alternate-screen.
  - Disable focus reporting in iTerm2.
  - Clean tmux session test.
- # Most Probable Final Fix
  - One of these lines resolving it:
  - ~~~
    set -g focus-events off
    ~~~
  - or
  - ~~~
    set -g default-terminal "screen-256color"
    ~~~
  - or disabling focus reporting in iTerm2.
- # Next Steps
  - Investigate rendering desync between tmux 3.6a and iTerm2 involving focus-events, extended-keys, and alternate-screen negotiation.
  - Reproduce in clean tmux instance.
  - Systematically disable:
    - focus-events
    - extended-keys
    - allow-passthrough
    - alternate-screen
  - Test with downgraded `default-terminal`.
  - Determine whether issue is configuration-induced or iTerm2 feature negotiation incompatibility.
