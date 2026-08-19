# Map My Folder

An instrument you drop into a Claude Project and point at **your own folder**. It produces a map: a
catalog on one screen, and a handful of cards — each one shorter than the file it points at — so that
a later reader can change one thing without reading everything.

The later reader is usually a cold model with no memory of how the folder got that way.

> **Reading a map rather than making one?** Go straight to
> [`reference/worked-example/CATALOG.md`](reference/worked-example/CATALOG.md), find your row, open
> **one** card, stop. `identity.md` and `rules.md` are the *making* instrument; a reader who opens
> them will start making a map instead of reading yours.

## The one rule

> **Load the catalog, then one card. Never the whole `cards/` folder.**

A map you have to read in full is a folder you have to read in full, with an extra step. If a
question needs a second card, the first card was mis-scoped — that is a finding about the map, and
it gets fixed; it is not a licence to keep reading.

## Setup

**To make a map of your folder** — add these six files to a Claude Project and nothing else:

    identity.md
    rules.md
    reference/card-types.md
    reference/state.md
    reference/walks.md
    reference/card-shape.md

Then: **"Map `~/path/to/your/folder`."** Give a path, not a description.

**To read a map that already exists** — including the one shipped here — add its `CATALOG.md`. Add a
card only when the catalog sends you to one.

**Do not add `reference/worked-example/cards/` to a project.** Seven cards about somebody else's
repo will crowd out your own folder and teach the model to answer from the wrong territory. The
worked example is a sample of output, not payload.

## First-run prompts

| You want | Say |
|---|---|
| A map of your folder | `Map ~/code/whatever. Start with the enumeration; don't open anything yet.` |
| To know if it is even mappable | `Run the territory check on ~/code/whatever and stop.` |
| To read the shipped example | `What is Services?` — then check that it stopped after two hops |
| To check a map you already have | `python3 reference/checks/refusal-checks.py --map <map-dir> --territory <folder>` |

## What it is

- **Seven card types**, a closed set, each with a proof test — ENGINE, BLUEPRINT, INSTANCE, SLOT,
  MARKER, INSTRUCTION, SURFACE. [`reference/card-types.md`](reference/card-types.md)
- **A separate state axis** — LIVE / LEFTOVER / GHOST, where appearance never decides the verdict and
  no verdict ships without the evidence that decided it. [`reference/state.md`](reference/state.md)
- **Two walks**, kept apart: making a map (seven steps, cards last) and reading one (four steps, most
  reads stop at two). [`reference/walks.md`](reference/walks.md)
- **Two refusals**, one of them runnable: no photocopy, no slurping. [`rules.md`](rules.md),
  [`reference/checks/refusal-checks.py`](reference/checks/refusal-checks.py)
- **A worked example** — a full map of a real repo, `NFTYoginis/your-market-realtor`, with the
  commands and output behind every state verdict.
  [`reference/worked-example/`](reference/worked-example/)

## What it refuses

Three territories, declined out loud rather than half-mapped ([`identity.md`](identity.md)):

1. **A pile of one-offs** — no repeating shape, so no card would be more than a summary.
2. **A single application where every file is unique** — that wants a call graph.
3. **The methodology itself** — a folder system about folder systems, this repo included. Mapping a
   method with the method returns a mirror.

It also does not fix what it finds. The worked example ships with an open ghost
(`CONTRIBUTING.md:12` names a path that has never existed) precisely because closing it would have
been the easy move and the wrong one. A map that edits its territory while drawing it is a map of
something that no longer exists.

## The worked example

`NFTYoginis/your-market-realtor` — one specialist engine, one region blueprint, four populated
markets, a public site. Seven cards, and the ceiling was reached: everything else is one line in
[`notes.md`](reference/worked-example/notes.md) with the test it failed.

    reference/worked-example/
      CATALOG.md               ← start here
      cards/                   ← one card, when the catalog sends you
      notes.md                 ← every noun that got no card, and why
      verification-log.md      ← the commands and output behind every state verdict
      cold-run-transcript.md   ← a fresh session, no memory, asked one question

The transcript is not decoration. The first cold run failed — it never found the catalog and started
re-deriving the map from the territory — and that failure is why `README.md`, `identity.md` and
`rules.md` now open with a line telling a reader which walk they are on. Re-run it yourself with
[`reference/checks/cold-run.py`](reference/checks/cold-run.py) (`pip install anthropic`, set
`TERRITORY_DIR` and `QUESTION`):

    CATALOG_IN_CONTEXT=1 TERRITORY_DIR=./your-market-realtor QUESTION="What is Services?" \
        python3 reference/checks/cold-run.py

**`CATALOG_IN_CONTEXT=1` is the flag that matters.** It puts the catalog in the project — the
configuration this README tells a reader of an existing map to load, and the one the two-hop number
is measured in. Drop the flag and the session gets no framing at all: it has to find the map first,
which costs more reads. Both are real; always say which you ran.

To re-run the checks yourself, clone the territory and point the script at it:

    git clone https://github.com/NFTYoginis/your-market-realtor.git
    python3 reference/checks/refusal-checks.py \
        --map reference/worked-example --territory ./your-market-realtor

## Licence

MIT — see [`LICENSE`](LICENSE).
