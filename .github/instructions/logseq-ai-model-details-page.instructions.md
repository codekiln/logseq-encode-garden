---
description: ''
---
# AI Model Detailed Documentation Guide
This rule extends `logseq-naming-conventions.mdc` for creating comprehensive AI model documentation pages.

## When to Use This Rule
- When creating detailed model documentation for a specific model version
- When documenting model capabilities and benchmarks for a particular release
- When creating model comparison pages
- When the model is a primary focus of discussion
- When detailed technical specifications are needed

## Page Creation Process

### 1. Research Model Information
- Search for official model cards and documentation
- Look for benchmark results and performance metrics
- Find pricing and availability information
- Gather technical specifications
- Identify the specific model version code (e.g., `gemini-2.5-pro-preview-05-06`)

### 2. Create Page Structure
```markdown
---
alias:: [[model-code]]
tags:: [[AI/Model]]
---

- # [Model Name](official-documentation-url)
  - ## Key Features
    - List major capabilities and improvements
    - Include context window size
    - Note knowledge cutoff date
    - Specify model version status (stable/preview/experimental)
  - ## Performance Highlights
    - Include benchmark results
    - Link to benchmark pages
    - Note performance improvements
  - ## Model Tiers (if applicable)
    - List available variants
    - Compare capabilities
    - Note pricing differences
  - ## Access Details
    - API availability
    - Pricing information
    - Usage limitations
    - Rate limits
  - ## Technical Specifications
    - Model architecture
    - Training data
    - Input/output formats
    - Special capabilities
    - Model version code
  - ## References
    - Link to official documentation
    - Link to research papers
    - Link to benchmark results
```

### 3. Required Research Sources
- Official model documentation
- Model cards
- Research papers
- Benchmark results
- Pricing pages
- API documentation

## Examples

<CORRECT_✅>
```markdown
- # [GPT-4.1](https://platform.openai.com/docs/models/gpt-4.1)
  - ## Key Features
    - New family of models: GPT-4.1, GPT-4.1 Mini, and GPT-4.1 Nano
    - Major improvements in coding, instruction following, and long-context understanding
    - Supports up to 1 million tokens context window
    - Knowledge cutoff: [[2024/06]]
```
</CORRECT_✅>

<INCORRECT_❌>
```markdown
- # GPT-4.1
  - ## Features
    - New model family
    - Better performance
    - More tokens
    - Updated knowledge
```
</INCORRECT_❌>

## Best Practices
- Always link to official documentation in the H1 title
- Include benchmark results with links to benchmark pages
- Document model variants and their differences
- Keep pricing and availability information up to date
- Link to related models and comparisons
- Follow the singular naming convention from `logseq-naming-conventions.mdc`
- Use model codes in aliases (e.g., `[[gemini-2.5-pro-preview-05-06]]` instead of `[[Gemini 2.5 Pro Preview 05-06]]`)
- Always document specific model versions, not model families
- Include model version status (stable/preview/experimental) in key features
- Specify rate limits and usage restrictions for preview/experimental models

## When to Update
- When new benchmark results are available
- When pricing or availability changes
- When new variants are released
- When official documentation is updated
- When new capabilities are discovered
- When model version status changes (e.g., from preview to stable)

## Related Rules
- `logseq-ai-model-reference.mdc` - For quick model references
- `logseq-naming-conventions.mdc` - For naming conventions
- `logseq-directory-structure.mdc` - For page organization
