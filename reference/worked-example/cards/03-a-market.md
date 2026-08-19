# 03 · A Market

**Type + State:** INSTANCE · LIVE ×4 — four names an outsider recognizes: `jerusalem`, `khao-lak`,
`lisbon-portugal`, `novato`. LIVE for a **human** reader, and that is the whole subtlety: its first
readers are a contributor forking the repo (`CONTRIBUTING.md:10`, `specialist/README.md:26` — "copy
that pack as a starting point") and a visitor to the public page. `grep -rn "case-studies"
specialist/` returns two hits, both in `specialist/README.md`, both addressed to a person.

**What it is:** one geography, filled in. Each instance is the six slot files plus a
`region/README.md` — seven files where the blueprint has six; the README has no blueprint
counterpart and no reader in the machinery, so it is not a slot.

**Why it is shaped that way:** the blueprint is overwritten in place when a market is populated, so a
finished market has to live outside the read path or the next agent inherits somebody else's
Jerusalem. Parked copies are the cost of that design, and their value is evidence — proof the
architecture ports — not runtime data.

**Source path:** `case-studies/<slug>/region/`

**Hits:** nothing else in the repo. An instance is a leaf; edit one and only that one changes.

**Does not hit:** the specialist that answers questions about that city. To change what a running
Jerusalem specialist knows, the file is `specialist/reference/region/market.md` **on that agent's own
machine** — the routing table resolves inside `specialist/reference/`, never into `case-studies/`.
Editing `case-studies/jerusalem/` changes no answer anyone will ever receive.

**Done when:** you can name the slug and confirm the six slot files are present
(`ls case-studies/<slug>/region/`). If your question is about behavior rather than about the example,
you are in the wrong folder — go to card 01. Stop there.
