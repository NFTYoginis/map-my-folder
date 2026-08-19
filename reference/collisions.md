# Collisions — "Chat is not always Chat"

A collision is one word with two referents inside one territory. They are invisible to the people who
built the folder, because by then both meanings are obvious. They are the single most expensive thing
for a cold reader, who will pick one meaning, be right most of the time, and be silently wrong the
rest.

**Run the collision pass before writing cards** (walk A, step 5). A collision found afterwards
rewrites every card that used the word.

## How to find them

- Any word that names both a **file** and a **folder**.
- Any word that names both a **thing in the folder** and a **thing in the industry the folder serves**.
- Any word that names both a **template** and one of its **copies**.
- Any word whose meaning changes when it crosses the boundary to the outside — on disk vs. on the web,
  in the repo vs. in the product.

## How to write one

One line per collision, both referents, each with a path or a boundary. No adjudication — you are not
renaming anything, you are telling the reader which one they are holding.

---

## The worked example's collisions — `NFTYoginis/your-market-realtor`

| Word | Sense 1 | Sense 2 |
|---|---|---|
| **market** | `market.md` — a slot holding local conditions: segments, price bands, working languages | `<market-slug>` — the geography itself, the name of an instance (`khao-lak`, `novato`) |
| **region** | the **blueprint** at `specialist/reference/region/` — six unfilled files | an **instance** at `case-studies/<slug>/region/` — the same six files, filled |
| **services** | `services.md` — the agent's vetted list of *other people's* businesses: inspectors, lenders, movers | the agent's own services, which is what "services" means everywhere else in real estate |
| **case study** | a populated market kept in the repo as evidence the architecture ports | a client success story — which is what the phrase means everywhere else in business |
| **docs** | a folder on disk, `docs/` | the **site root** on the web: `/your-market-realtor/` → 200, `/your-market-realtor/docs/` → 404 |

**region** is the one that costs the most. Both senses are a folder named `region` holding six files
with identical names, and the difference between them is the difference between an edit that reaches
every future market and an edit that reaches nobody. See card
[`02-the-region-blueprint`](worked-example/cards/02-the-region-blueprint.md).
