# `_legacy/` — staging area

Files here are **not part of the active docs build.** They've been moved out of the
active source tree during the v2 reorg (Day 5-6) pending final disposition.

## Why this exists

During the v2 reorg, some files are being dropped, renamed, or restructured. Rather
than `git rm`-ing them immediately, we stage them here. End-of-Day-6, we review the
full list and make deletion/preservation calls with the whole picture in view.

## Sphinx behavior

This directory is listed in `docs/conf.py`'s `exclude_patterns`, so Sphinx
completely ignores it. Files inside it:

- do not appear in the sidebar
- do not trigger "document isn't included in any toctree" warnings
- do not cause "duplicate label" errors even if their labels match active pages

## Current contents

**Redundant v2-section stubs** — child pages whose content was folded into the
section index (`index.rst`) when we flattened the sidebar and dropped the
caption/title redundancy:

- `agentic/overview.rst` → merged into `docs/agentic/index.rst`
- `twin/concept.rst` → merged into `docs/twin/index.rst`
- `agentic_primitives/primitive_contract.rst` → merged into `docs/agentic_primitives/index.rst`

These were stubs, not real content — staging them is more about consistency
than preserving anything substantive. Safe to delete at end-of-Day-6.

## Disposition checklist (end-of-Day-6)

For each file in this folder, decide:

- **Keep in active docs** — move back to original path, ensure referenced in toctree
- **Delete permanently** — `git rm`, commit with message noting the decision
- **Leave staged** — if uncertain, leave here for the next docs pass

Nothing in this folder should survive a Phase 2 release without a positive decision.
