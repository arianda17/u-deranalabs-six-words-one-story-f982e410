#!/usr/bin/env python3.13
"""Six Words, One Story entry for make.fun bounty u-deranalabs-six-words-one-story-f982e410.

The six-word story: "He promised forever. She counted seconds."
A promise of forever against a woman counting down — the gap between
the two is the whole story, left for the reader to fill in.
"""

STORY = "He promised forever. She counted seconds."

# Validate the story has exactly six words before writing.
assert len(STORY.split()) == 6, "story must be exactly six words"

print(STORY)