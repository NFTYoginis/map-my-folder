# 01 · The Engine

**Type + State:** ENGINE · LIVE — four instances read it and it names none of them: the routing table
in `specialist/rules.md` addresses only relative paths (`region/market.md`, `frameworks/pricing.md`),
and `grep -rn "Jerusalem\|Novato\|Khao\|Lisbon" specialist/` returns market names only in
`examples.md` and one illustrative clause at `identity.md:44` — never in a rule that selects a file.

**What it is:** the market-agnostic half of the specialist — who it is, what it refuses, which files
it opens for which job, and the frameworks, checklists and templates those jobs consume. It is what
gets loaded into a Claude Project; `specialist/README.md` is its install door.

**Why it is shaped that way:** one engine has to serve every geography, so everything local was
pushed out into a folder the engine *reads* rather than logic the engine *contains*. That is the
whole reason a fifth market is a copy instead of a fork — and the reason the engine can be edited
without knowing which market is running.

**Source path:** `specialist/`

**Hits:** every market that loads it, immediately and in place — the four here and any fork. A
changed routing row changes the next answer in every geography at once.

**Does not hit:** the public claims about it. `README.md` and `docs/index.html` state the counts and
capabilities by hand — "six files", "22 files" — and nothing regenerates them. A reader who edits the
engine reaches for the four case studies as the thing that must be updated; those are frozen copies
and need nothing. The surface that sells the engine is what goes stale, and it is not in this card
(see 07).

**Done when:** you can name the single file under `specialist/` whose change alters the job you are
touching — for a job, the routing row in `specialist/rules.md`; for refusals, `identity.md`; for the
first turn, `welcome.md` — and you have not opened a case study. Stop there.
