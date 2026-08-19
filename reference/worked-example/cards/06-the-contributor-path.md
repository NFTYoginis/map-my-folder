# 06 · The Contributor Path

**Type + State:** INSTRUCTION · LIVE, aiming at a **GHOST**. Instruction: nothing under `specialist/`
reads it; delete it and no run changes. Ghost: its line 12 tells a contributor to add
`case-studies/[your-market-slug]/README.md`, and
`git ls-tree -r --name-only origin/main | grep -E '^case-studies/[^/]+/README\.md$'` returns nothing
(exit 1) — confirmed on origin at `702e79c`, not just in a clone. `find case-studies -name README.md`
returns four, all one level deeper, at `case-studies/<slug>/region/README.md`.

**What it is:** the door for the next market — fork, copy the blueprint to a slug, fill the six
files, add a README, open a PR — plus the bar for changing the architecture itself (test against two
case studies, name which).

**Why it is shaped that way:** it was written when the contributed unit was pictured as a folder with
a README standing beside a `region/` folder. The four contributions instead put the README inside
`region/`, next to the six files. The instruction was never reconciled with them.

**Source path:** `CONTRIBUTING.md`

**Hits:** the next contributor, once, at fork time. Nothing else — no run, no answer, no build.

**Does not hit:** the four case studies. Finding the mismatch, a reader reaches to move the four
READMEs up a level so they match the sentence. The four agree with each other and disagree only with
the sentence — four contributions passed through this instruction and none followed it, which is the
evidence that the sentence is the defect, not the folders.

**Done when:** you have the real path from `find`, not from the instruction, and you have written the
ghost down rather than closed it. Fixing it is a change to the territory and belongs in a commit of
its own, after the map ships. Stop there.
