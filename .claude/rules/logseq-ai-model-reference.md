---
paths:
  - journals/*.md
  - pages/*.md
---
# AI Model Reference Quick Guide
This rule extends the logseq-naming-conventions rule for quickly referencing AI models in the knowledge graph without creating detailed pages.

## When to Use This Rule
- When mentioning a model in passing
- When creating changelog entries
- When comparing models
- When listing available models
- When creating stub pages for future detailed documentation

## Quick Reference Format

### Provider Namespaces
- [[OpenAI/Model/...]] - For OpenAI models
- [[Anthropic/Model/...]] - For Anthropic models
- [[Google/AI/Model/...]] - For Google models
- [[DeepSeek/Model/...]] - For DeepSeek models
- [[xAI/Model/...]] - For xAI/Grok models

### Version Format
- Use forward slashes for version hierarchy
- Example: `[[OpenAI/Model/GPT/4/1]]` for GPT-4.1
- Example: `[[Anthropic/Model/Claude/3.5/Sonnet]]` for Claude 3.5 Sonnet

### Quick Stub Page Creation
When creating a stub page for a new model:

1. Create the page with minimal frontmatter:
   ```markdown
   ---
   alias:: [[model-name]]
   tags:: [[AI/Model]]
   ---
   ```

2. Add a basic structure:
   ```markdown
   - # Model Name
     - *Stub page - detailed documentation pending*
   ```

3. Add the model to the appropriate provider's model list page if it exists

## Examples

<CORRECT_✅>
```markdown
- ### New models
  - Added [[Google/AI/Model/Gemini/2.5/Pro]], [[Google/AI/Model/Gemini/2.5/Flash]]
  - Added [[xAI/Model/Grok/3]], [[xAI/Model/Grok/3/Mini]]
  - Added [[OpenAI/Model/GPT/4/1]], [[OpenAI/Model/o3]] and [[OpenAI/Model/o4/Mini]]
```
</CORRECT_✅>

<INCORRECT_❌>
```markdown
- ### New models
  - Added Gemini 2.5 Pro, Gemini 2.5 Flash
  - Added Grok 3, Grok 3 Mini
  - Added GPT-4.1, o3 and o4-mini
```
</INCORRECT_❌>

## Best Practices
- Always use the full namespace path when referencing models
- Create stub pages for new models to maintain consistency
- Use aliases for common model references
- Link to existing model pages when available
- Follow the singular naming convention from the logseq-naming-conventions rule

## When to Create a Detailed Page
- When the model is a primary focus of discussion
- When documenting model capabilities or benchmarks
- When creating comparison pages
- When the model is frequently referenced
- When detailed technical specifications are needed

In these cases, refer to the logseq-ai-model-details-page rule for creating comprehensive model documentation.
