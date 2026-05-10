---
name: review-posts
description: Reviews blog posts in content/blog/ for spelling, grammar, clarity, and structure — without changing the author's voice. Use this skill whenever the user asks to review, proofread, edit, or improve a blog post, even casually (e.g. "can you look at this post", "clean up my article", "check this draft").
---
# Review Posts

Review the blog post with a light editorial hand. The goal is to improve clarity and correctness while preserving the author's voice and intent — not to rewrite.

## What to fix

- **Spelling and grammar**: correct errors without altering word choice or sentence rhythm beyond what's necessary.
- **Awkward phrasing**: smooth out sentences that are hard to read, but keep the author's style intact.
- **Paragraph focus**: each paragraph should carry one main idea. If several distinct claims are packed into one, split or reorder them — don't cut.
- **Term definitions**: if an important or unusual term appears without explanation, add a brief inline definition the first time it's used.
- **Cause–effect clarity**: where the reasoning is implicit, make it explicit with connectives like "Because …" or "So …" only when the relationship isn't already clear to a general reader.

## What to leave alone

- The author's voice, tone, and style choices.
- Content, arguments, and structure beyond the paragraph-level fixes above.
- Anything that works fine as-is — don't change for the sake of changing.

## Output

Return the full revised post with your edits applied inline. If you made non-obvious changes, add a short bulleted summary at the end listing what you changed and why — keep it under 5 items. Skip the summary if the edits were minor.
