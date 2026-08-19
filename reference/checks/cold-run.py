#!/usr/bin/env python3
"""Cold-run gate — one question, one fresh session, no memory and no coaching.

Run it against any map. Set MAP_DIR and TERRITORY_DIR to the two folders and QUESTION to the thing a
reader would actually ask. A hop is a file opened; `list_dir` is free, as a project file listing is.

**CATALOG_IN_CONTEXT=1 puts the map's catalog in the project** — the configuration the README tells a
reader of an existing map to load, and the one the "catalog + one card" claim is measured in. Without
it the session gets no framing at all and has to find the map itself, which costs more reads. Both
numbers are real; they are answers to different questions, so always report which flag was set.

Needs `pip install anthropic` and ANTHROPIC_API_KEY. Transcript prints as JSON on stdout.

Fresh session, no memory, no project instructions, no coaching. The model gets two folders (the map
and the repository it maps) behind a free `list_dir` and a metered `read_file`, and one question.

Pass depends on the configuration you ran, so record the flag with the number: with
CATALOG_IN_CONTEXT=1 the budget is the catalog (already in the project) plus ONE card opened;
unframed, the session must also find the map, so expect more. In both, the answer must be
correct, no territory file should be opened for an identification question, and it must stop.
"""

import json
import os
import sys

from anthropic import Anthropic

MAP = os.environ.get("MAP_DIR", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
TERRITORY = os.environ.get("TERRITORY_DIR", os.path.abspath("./your-market-realtor"))
QUESTION = os.environ.get("QUESTION", "What is Services?")

ROOTS = {"map": MAP, "repo": TERRITORY}

# Two configurations, and the difference is the whole point of the gate.
#   unset            → UNFRAMED: the session sees two folder names and must find its own way in.
#   CATALOG_IN_CONTEXT=1  → the map's catalog is in the project, which is what the README tells a
#                      reader of an existing map to load. Set it to a path to use a different
#                      catalog (absolute, or relative to MAP).
_CIC = os.environ.get("CATALOG_IN_CONTEXT", "").strip()
CATALOG_IN_CONTEXT = _CIC not in ("", "0", "false", "False", "no")
CATALOG_PATH = ""
if CATALOG_IN_CONTEXT:
    rel = "reference/worked-example/CATALOG.md" if _CIC in ("1", "true", "True", "yes") else _CIC
    CATALOG_PATH = rel if os.path.isabs(rel) else os.path.join(MAP, rel)
    if not os.path.isfile(CATALOG_PATH):
        sys.exit(f"CATALOG_IN_CONTEXT set but no catalog at {CATALOG_PATH}")

if CATALOG_IN_CONTEXT:
    with open(CATALOG_PATH, encoding="utf-8") as _fh:
        _CATALOG = _fh.read()
    SYSTEM = (
        "You are in a fresh session. You have no memory of any previous conversation and no notes.\n\n"
        "Your project contains one file, a map of a repository. It is reproduced below.\n\n"
        "Two folders are also available to you through tools:\n"
        f"  map  — {MAP}   (the map folder; the catalog below lives at "
        f"{os.path.relpath(os.path.dirname(CATALOG_PATH), MAP)}/)\n"
        f"  repo — {TERRITORY}   (the repository the map describes)\n\n"
        "Use `list_dir` to see what is there and `read_file` to read something. Answer the user's "
        "question.\n\n"
        "--- CATALOG.md ---\n" + _CATALOG
    )
else:
    SYSTEM = (
        "You are in a fresh session. You have no memory of any previous conversation and no notes.\n\n"
        "Two folders are available to you through tools:\n"
        f"  map  — {MAP}\n"
        f"  repo — {TERRITORY}\n\n"
        "Use `list_dir` to see what is there and `read_file` to read something. Answer the user's "
        "question."
    )

TOOLS = [
    {
        "name": "list_dir",
        "description": "List the entries of a directory. Path is relative to a root: "
                       "'map' or 'repo'. Use '.' for the root itself.",
        "input_schema": {
            "type": "object",
            "properties": {
                "root": {"type": "string", "enum": ["map", "repo"]},
                "path": {"type": "string"},
                "recursive": {"type": "boolean"},
            },
            "required": ["root", "path"],
        },
    },
    {
        "name": "read_file",
        "description": "Read a file. Path is relative to a root: 'map' or 'repo'.",
        "input_schema": {
            "type": "object",
            "properties": {
                "root": {"type": "string", "enum": ["map", "repo"]},
                "path": {"type": "string"},
            },
            "required": ["root", "path"],
        },
    },
]

reads = []      # metered hops
listings = []   # free


def safe(root, path):
    base = ROOTS[root]
    full = os.path.normpath(os.path.join(base, path))
    if not full.startswith(base):
        raise ValueError("outside root")
    return full


def do_list(root, path, recursive=False):
    full = safe(root, path)
    listings.append(f"{root}:{path}")
    if not os.path.isdir(full):
        return f"not a directory: {path}"
    out = []
    if recursive:
        for dirpath, dirnames, names in os.walk(full):
            dirnames[:] = [d for d in dirnames if d != ".git"]
            rel = os.path.relpath(dirpath, full)
            for n in sorted(names):
                p = n if rel == "." else os.path.join(rel, n)
                out.append(f"{p}  ({os.path.getsize(os.path.join(dirpath, n))} B)")
    else:
        for n in sorted(os.listdir(full)):
            if n == ".git":
                continue
            p = os.path.join(full, n)
            out.append(f"{n}/" if os.path.isdir(p) else f"{n}  ({os.path.getsize(p)} B)")
    return "\n".join(out) or "(empty)"


def do_read(root, path):
    full = safe(root, path)
    reads.append(f"{root}:{path}")
    if not os.path.isfile(full):
        return f"no such file: {path}"
    with open(full, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main():
    client = Anthropic(max_retries=8)
    messages = [{"role": "user", "content": QUESTION}]
    transcript = []

    for turn in range(12):
        resp = client.messages.create(
            model="claude-opus-5",
            max_tokens=16000,
            system=SYSTEM,
            thinking={"type": "adaptive"},
            tools=TOOLS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": resp.content})

        text_blocks = [b.text for b in resp.content if b.type == "text"]
        tool_uses = [b for b in resp.content if b.type == "tool_use"]
        transcript.append({
            "turn": turn,
            "stop_reason": resp.stop_reason,
            "text": "\n".join(text_blocks),
            "tool_calls": [{"name": b.name, "input": b.input} for b in tool_uses],
            "usage": {"in": resp.usage.input_tokens, "out": resp.usage.output_tokens},
        })

        if resp.stop_reason != "tool_use":
            break

        results = []
        for b in tool_uses:
            try:
                if b.name == "list_dir":
                    content = do_list(b.input["root"], b.input["path"],
                                      b.input.get("recursive", False))
                else:
                    content = do_read(b.input["root"], b.input["path"])
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": content})
            except Exception as exc:  # noqa: BLE001 — surfaced to the model as an error result
                results.append({"type": "tool_result", "tool_use_id": b.id,
                                "content": str(exc), "is_error": True})
        messages.append({"role": "user", "content": results})

    out = {
        "question": QUESTION,
        "model": "claude-opus-5",
        "catalog_in_context": CATALOG_IN_CONTEXT,
        "catalog_path": CATALOG_PATH or None,
        "file_reads": reads,
        "listings": listings,
        "hops": len(reads),
        "transcript": transcript,
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
