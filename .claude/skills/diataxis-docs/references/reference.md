# Diataxis Reference Docs in Logseq

Reference documentation provides **technical descriptions** of a product and how to use it. It is **information-oriented** and serves as a reliable source of truth: propositional knowledge users consult during practical work, described systematically, led by the structure of the product.

## Key Principles
1. **Describe and Only Describe** — neutral description is the imperative
2. **Adopt Standard Patterns** — consistency makes reference useful
3. **Respect the Structure of the Product** — mirror its logical organization
4. **Provide Examples** — illustrate usage without explaining or instructing
5. **Be Austere** — users consult, not read cover to cover
6. **Be Authoritative** — no doubt or ambiguity

## Structure (LFM)

```
tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Reference]]

- # [Topic Name] Reference
  - ## Overview
    - Brief, factual description; scope and boundaries
  - ## Structure
    - How the reference is organized; conventions used
  - ## Core Components
    - ### Component 1
      - Precise factual description; specs; parameters/properties; usage examples
    - ### Component 2
      - And so on...
  - ## Technical Details
    - Specifications, constraints, requirements; version info; dependencies
  - ## Related References
    - Links to related reference pages
```

## Naming and File Paths
Namespace pattern: `Topic/Subtopic/Ref/Specific Subject`.
- `[[API/Endpoints/Ref/Authentication]]` → `pages/API___Endpoints___Ref___Authentication.md`
- `[[Unicode/Block/Ref/Symbols for Legacy Computing]]` → `pages/Unicode___Block___Ref___Symbols for Legacy Computing.md`

## Required Tags
All Diataxis Reference pages MUST include `[[Diataxis/Reference]]` in frontmatter. Add it to existing tags; never remove existing tags.

## Language Guidelines
- Neutral, objective language; facts not opinions
- Consistent format; present tense; precise and unambiguous
- Avoid instructional language ("do this," "follow these steps")
- Separate description from explanation (link to explanation pages)

## Common Pitfalls
- Mixing reference with tutorials/how-to content
- Including opinions, speculation, or marketing language
- Inconsistent formats or structures
- Assuming auto-generated reference is sufficient
- Failing to update reference when the product changes

## Compass
informs cognition · serves theoretical knowledge · information-oriented · describes the product → reference.

Characteristics of good reference: austere, authoritative, map-like, structured.
