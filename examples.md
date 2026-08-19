# Worked examples

Three. One read, one map-making move, one refusal. The refusal is not the odd one out — it is the
most common correct output.

---

## Example 1 — a read that stops in two hops

**Input**

> What is Services?

**What happens:** walk B. Catalog, one card, stop.

**Output**

> **Hop 1 — [`CATALOG.md`](reference/worked-example/CATALOG.md).** `services.md` is in the row
> *"contracts · glossary · market · neighborhoods · regulations · services"* → **card 04, The Six
> Slots**, with a flag that three of those six words mean two things here.
>
> **Hop 2 — [`04-the-six-slots.md`](reference/worked-example/cards/04-the-six-slots.md).**
>
> **Services** is one of the six slots inside a market. It holds the agent's vetted list of *other
> people's* businesses — inspectors, lenders, stagers, movers — **not** the agent's own services,
> which is what the word means everywhere else in real estate. It is the newest slot
> (`specialist/README.md:26` calls it "new in v2") and it is routed as its own job, a "services
> lookup", rather than as background reading.
>
> Source: `specialist/reference/region/services.md` for the blank, `case-studies/<slug>/region/
> services.md` for the four filled ones.
>
> **Stop.** Two files opened, both of them map. Nothing in the territory was read to answer this.

**Why it stops:** the question was *what is this*, so the read ends at *What it is*. The Hits line is
about blast radius and is only paid for by someone who is changing something. Had the answer needed a
second card, that would be a finding about card 04's boundary — recorded, not read around.

---

## Example 2 — a map-making move: state, decided by the reader

**Input**

> `case-studies/` holds four populated markets. Classify it.

**The wrong finish, and it is the intuitive one:** four folders of real market data, sitting in a repo
whose product is a market-aware specialist → INSTANCE, LIVE, read by the specialist at run time.
Three of those four are right.

**The move** — walk A, step 4: find the reader before reading the file.

    $ grep -rn "case-studies" specialist/
    specialist/README.md:26:  … If your market resembles one of the examples in `../case-studies/`,
                              copy that pack as a starting point and edit.
    specialist/README.md:88:  … or copy a populated one from `../case-studies/`.

Two hits, both in a README, both addressed to a person. The routing table that selects files for a
job (`specialist/rules.md`) names `region/*.md` — resolving inside `specialist/reference/`, never
into `case-studies/`.

**Output**

> **INSTANCE · LIVE ×4** — live for a *human* reader (a contributor forking the repo, a visitor to
> the public page), not for the running specialist. Evidence: the two greps above.
>
> **Hits:** nothing. An instance is a leaf.
> **Does not hit:** the specialist that answers questions about that city. Editing
> `case-studies/jerusalem/` changes no answer anyone will ever receive.

**The rule this exercises:** *appearance never decides state; look for who reads it first.* The
verdict "LIVE" survived — but LIVE *for whom* inverted, and the Does-not-hit line inverted with it.
That line is the difference between a map and a directory listing.

---

## Example 3 — the refusal, before the second file is opened

**Input**

> Map `~/scratch/` for me — it's where I keep everything.
>
>     $ find ~/scratch -type f | head -12
>     resize-photos.sh      notes-2024.md        invoice-template.xlsx
>     dns-backup.json       old-resume.pdf       scrape.py
>     meeting-notes.txt     budget.numbers       fix-permissions.sh
>     todo.md               vpn-config.ovpn      readme.txt

**Output**

> There is no repeating unit here. I count 12 files and no two of them share a shape, so a map would
> be a file listing with adjectives. Ask me again when one of these has been copied.
>
> What you have is a pile of one-offs, which is the first thing I refuse
> ([`identity.md`](identity.md)). `ls -lt` will tell you what you touched recently, and it costs
> nothing. If one of these grows a second copy — the same shape under a different name — that is when
> a map starts paying for itself.

**What did not happen:** no file was opened, no card was drafted, no partial map was offered as a
consolation. The refusal came from the enumeration alone, which is the only place it is cheap.

**The two neighbours of this refusal**, both also declined out loud: a single application where every
file is unique (that wants a call graph, not a map), and the methodology itself — a folder system
about folder systems, this one included. Mapping a method with the method returns a mirror.
