# State — a second axis, not a second type

Type says what a thing is. State says whether it is still alive. They are independent, and a card
carries both.

| State | Meaning | What decides it |
|---|---|---|
| **LIVE** | Something reads it, runs it, or reaches it, now. | A named reader: a file and line, a routing row, a status code. |
| **LEFTOVER** | It was live. Something replaced it and it was never removed. | The thing that replaced it, named. |
| **GHOST** | It is referred to but does not exist — or exists only where the reference cannot reach it. | The reference, and the failed lookup. |

## The inversion rule

> **Appearance never decides state. Look for who reads it first.**

Every wrong verdict on this axis comes from reading the file instead of finding its reader. The four
shapes that fool people:

- **Big, current, well-written — and nothing reads it.** Recent edits are evidence about an author,
  not about a reader.
- **Small, ugly, stale-looking — and it is on the hot path.** A four-line file the machinery branches
  on is more live than a 40 KB document nobody loads.
- **Named like data, read like documentation.** A folder full of populated instances that the
  machinery never resolves into. Its readers are humans, and that is still LIVE — just LIVE for a
  different reader. Say which.
- **Named like an example, read like production.** The reverse. Check before you demote it.

The question is always the same: **who reads this first?** Answer with a path, then a line.

## A state may not ship without the evidence that decided it

Not a citation somewhere else in the map — in the same line as the verdict.

    **Type + State:** SURFACE · LIVE — `curl -o /dev/null -w '%{http_code}' <url>` → 200, and the
    served bytes equal `docs/index.html` on disk (39,722 B, sha1 ef9643e0…).

    **Type + State:** INSTRUCTION · LIVE, aiming at a GHOST — nothing under `specialist/` reads
    `CONTRIBUTING.md`; its line 12 names a path that `git ls-tree -r --name-only origin/main |
    grep -E '^case-studies/[^/]+/README\.md$'` returns nothing for.

Evidence that is allowed: a command and its output, a `file:line`, a status code, a byte count, a
commit SHA. Evidence that is **not** allowed: "appears unused", "looks current", "probably legacy".
If you cannot get evidence cheaply, write **UNVERIFIED** as the state and name the check that would
settle it. An honest gap is a map entry; a guess is a defect.

## Verify a ghost where the thing actually lives

A path missing from your clone is not a ghost — your clone might be behind, or the file might be
untracked and never pushed. Check the shared truth:

    git ls-tree -r --name-only origin/main | grep -E '<pattern>'

Empty output there, plus the reference that points at it, is a ghost. Empty output locally is a
question.

## State changes are movements, and movements have three parts

Start state, end state, actor — per `rules.md`. A card records the movement, **not the incident**
that revealed it. "The clone was one commit behind on Tuesday" is history and rots. "A file is
public after a push and after the site rebuilds; a clone behind origin shows bytes the web is not
serving" is the movement, and it is true next month too.
