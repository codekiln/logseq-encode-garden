---
name: logseq-cleanup-math
description: >-
  Clean up and format LaTeX math in Logseq-Flavored Markdown so KaTeX renders
  it: unwrap math from code blocks, put `$$` delimiters on their own lines,
  collapse duplicate or mangled formulas, and use `$inline$` for variables in
  prose. Use when math in a page renders as literal text, when importing notes
  whose formulas came through garbled, or when the user asks to fix or format
  math in the graph. Do not use for non-math LFM formatting (logseq-lfm) or for
  code blocks that are genuinely code.
metadata:
  short-description: Fix LaTeX/KaTeX math formatting in Logseq pages
---
# Logseq Math Cleanup and Formatting

This command provides rules for cleaning up and properly formatting LaTeX math expressions in Logseq-Flavored Markdown (LFM) files.

## Math Rendering in Logseq

Logseq supports **LaTeX math rendering** using **KaTeX** — both inline and block math.

### Inline Math

- Wrap your LaTeX expression in **single dollar signs**: `$formula$`
- Example: `This is inline math: $E = mc^2$`
- Renders as: This is inline math: $E = mc^2$

### Block Math

- Wrap your expression in **double dollar signs on separate lines** (not inline)
- **CRITICAL:** The `$$` must be on separate lines, not inline like `$$formula$$`
- Correct format:
  ```
  - $$
    \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
    $$
  ```
- Incorrect format (will not render properly):
  ```
  - $$formula$$
  - ~~~
    $$formula$$
    ~~~
  ```

## Cleanup Rules

When cleaning up math in Logseq files, follow these rules:

### 1. Remove Code Blocks Around Math

- **DO NOT** wrap math expressions in code blocks (triple tildes `~~~` or triple backticks)
- Math should be directly in the markdown, not in code blocks
- Code blocks prevent math from rendering

### 2. Fix Block Math Formatting

- Ensure `$$` delimiters are on **separate lines** from the formula
- Convert inline block math `$$formula$$` to multi-line format:
  ```
  - $$
    formula
    $$
  ```

### 3. Clean Up Duplicate/Malformed Formulas

- Remove duplicate formula content (often formulas appear multiple times in different formats)
- Keep only the clean, properly formatted LaTeX version
- Remove any plain text or mixed-format versions of the same formula

### 4. Format Inline Math Variables

- Use inline math notation `$variable$` for mathematical variables in explanatory text
- Example: `$r_t(\theta)$ = ratio between new and old policy probabilities`
- Clean up mixed formats like `rt(θ)r_t(\theta)rt(θ)` to just `$r_t(\theta)$`

### 5. Proper LFM Nesting

- Ensure math expressions are properly nested within the LFM bullet point structure
- Block math should be indented with TABs to match the content hierarchy
- Example structure:
  ```
  - ## Section
    - The formula is:
      - $$
        formula
        $$
    - where:
      - $variable$ = explanation
  ```

## Example Cleanup

### Before (Incorrect):
```
- The optimization objective is roughly:
  - ~~~
    $$L^{PPO} = \mathbb{E}\left[...\right]$$
    ~~~
- where:
  - rt(θ)r_t(\theta)rt(θ) = ratio between...
```

### After (Correct):
```
- The optimization objective is roughly:
  - $$
    L^{PPO} = \mathbb{E}\left[\min\left(r_t(\theta)A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)A_t\right)\right]
    $$
- where:
  - $r_t(\theta)$ = ratio between new and old policy probabilities
```

## KaTeX Support

- KaTeX supports most LaTeX commands
- Does **not** support commands that rely on packages not included in KaTeX (e.g., `\usepackage`)
- You can mix math and Markdown freely

## Troubleshooting

If math doesn't render in Logseq:
1. Open **Settings → Editor**
2. Ensure **"Enable math rendering (KaTeX)"** is toggled on
3. Reload Logseq (Cmd/Ctrl+R)
4. Verify the math is not wrapped in code blocks
5. Verify block math uses `$$` on separate lines
