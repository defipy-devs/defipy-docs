# RTD v2.1 Alignment Spec

**Repo:** `defipy-docs/`
**Target site:** `defipy.readthedocs.io`
**Owner:** Ian Moore
**Status:** Ready to execute
**Estimated effort:** 90–120 minutes (one focused session)

---

## Goal

Stop the RTD docs site from disseminating misinformation about v2.1 without committing to ongoing maintenance parity with `defipy-org`.

After this work lands, a Google-found visitor to `defipy.readthedocs.io` should:

1. Get factually correct information about what DeFiPy v2.1 ships
2. See a clear pointer to `defipy.org` as the canonical, actively-maintained docs surface
3. Not encounter empty stub pages that signal abandonment

The work is **surgical**, not comprehensive. The principle is: **defipy.org is canonical; RTD is honest-but-redirected**.

---

## Out of scope

Explicit list of what this spec does **not** touch. Important to keep the work bounded and prevent it from sprawling into a full v2.1 docs port.

- **`docs/agentic_primitives/notebooks/`** — category notebooks for all 21 primitives. Content is math-grounded and primitive-stable across v2.0 → v2.1. Notebook outputs may reference v2.0 contextually but the math is correct. Skip.
- **`docs/math/`** — pure derivation notebooks (V2, V3, Balancer, Stableswap). Evergreen. Skip.
- **Protocol-specific tutorial trees** — `docs/uniswapv2/`, `docs/uniswapv3/`, `docs/balancer/`, `docs/stableswap/`. Pre-v2 work, still correct, no v2.1 implications. Skip.
- **`docs/_legacy/`** — earlier doc-structure parallel content. Not on the live toctree (presumably). Don't touch unless it surfaces in build warnings.
- **`docs/agentic/`** — duplicate-looking agentic content tree. Verify it's not on the live toctree; if it is, fold its v2.1 alignment into the agentic_overview update.
- **Theme/structure changes** — sphinx_rtd_theme stays. No Furo migration. No toctree restructuring.
- **Filling stub pages with full v2.1 content** — that's the "as onerous as defipy-org" path explicitly being avoided.
- **`docs/conf.py`** — leave version strings alone unless they're publicly visible and stale (verify during build).

---

## What's broken right now

Audit performed by reading the actual `.rst` files. Three tiers of staleness:

### Tier 1 — Actively misinforming (must fix)

These pages tell a reader something **false** about DeFiPy v2.1 as it ships today.

| File | What's wrong | What's true now |
|---|---|---|
| `docs/quick/whats_new_v2.rst` | Title says "What's new in v2.0"; describes LiveProvider as "stub, functional implementation lands in v2.1"; reports 629 tests | LiveProvider is fully implemented for V2 + V3 in v2.1; Multicall3 batching ships; PoolHealth gets fee_pips/tvl_in_token1/tick_current; get_w3() escape hatch is public; 686 tests / 11 skipped |
| `docs/twin/index.rst` | LiveProvider described as "v2.1, stub in v2.0; calling .snapshot() raises NotImplementedError" | LiveProvider works against any web3-compatible RPC; .snapshot() returns enriched PoolSnapshot with block_number, timestamp, chain_id |
| `docs/twin_concept.rst` | Same misinformation as above; "LiveProvider (v2.1) will build them from live chain reads" reads as future tense | LiveProvider builds twins from live chain reads, today |
| `docs/installation.rst` | Lists `[mcp]`, `[book]`, `[anvil]` extras only. Missing `[chain]` and `[agentic]`. Install commands not zsh-quoted | `[chain]` and `[agentic]` ship in v2.1; brackets need single-quoting for zsh users |
| `docs/index.rst` | Footer reads "🔗 DAPX-Anchor" (typo) — should be SPDX-Anchor; primitive-call example narrates "The same pattern works against live chain state once `LiveProvider` ships in v2.1" as future tense | LiveProvider ships in v2.1, today; SPDX-Anchor is the correct prefix |
| `docs/roadmap.rst` | "v2.1 (next)" section lists LiveProvider implementation as upcoming; "Multi-format tool schemas" listed under v2.1 (it's deferred to v2.2 per defipy-org) | v2.1 shipped; Balancer/Stableswap LiveProviders + V3 tick walking + multi-format schemas are v2.2 work |
| `docs/agentic_overview.rst` | Describes LiveProvider as "v2.1 stub" — "MockProvider ships; LiveProvider stub is v2.1" | Both providers ship in v2.1 |

### Tier 2 — Cosmetic version drift (skip; banner covers it)

Pages that are "v2.0-flavored" but not actively misleading after Tier 1 fixes land. The top-of-index banner (Tier 4 below) signals "this site is being superseded" loud enough that readers will know to cross-reference defipy.org for canonical.

- `docs/index.rst` lede ("DeFiPy is a unified Python SDK...") — fine as-is
- `docs/agentic_overview.rst` non-LiveProvider content — fine as-is

### Tier 3 — Empty stubs (must resolve)

Three `.rst` files in `docs/twin/` that exist only because the v2.0 brief said "stub exists so the toctree builds clean." After Tier 1 fixes, they become orphaned promises.

| File | Current state | Recommendation |
|---|---|---|
| `docs/twin/live_provider.rst` | Single line: "Page content coming in Brief 2." | **Redirect** to `https://defipy.org/live-provider/` |
| `docs/twin/mock_provider.rst` | Same | **Redirect** to `https://defipy.org/twin-concept/` (no dedicated MockProvider page on defipy-org; twin-concept covers it) |
| `docs/twin/custom_twins.rst` | Same | **Redirect** to `https://defipy.org/twin-concept/#custom-providers` (or twin-concept root if that anchor doesn't exist; verify) |

The redirect approach: replace stub content with a minimal `.. note::` block pointing at the canonical defipy.org page. One paragraph each. Doesn't break the toctree; doesn't pretend the page is more than it is.

### Tier 4 — Banner (must add)

Top of `docs/index.rst`, immediately under the title, before the existing lede:

```rst
.. note::

   **This site is in maintenance mode.** The canonical, actively-maintained
   DeFiPy documentation now lives at `defipy.org <https://defipy.org>`_.
   The content here describes DeFiPy v2.0 and has been updated for v2.1
   factual accuracy, but new features, examples, and integration walkthroughs
   land at defipy.org first. For the most current information, please refer
   to the canonical site.
```

Rationale: respects existing Google traffic (the page still answers their question); signals the future direction (defipy.org); doesn't apologize for RTD's existence; doesn't commit to keeping RTD up-to-date.

---

## File-by-file edit plan

In execution order. Each edit is concrete enough that a fresh-context Claude (or the user with hands on keyboard) could execute it without further design work.

### Edit 1 — `docs/index.rst`

**1a.** Add the maintenance-mode banner (Tier 4) immediately under the page title, before the existing first paragraph.

**1b.** Update the primitive-call narration paragraph after the code block. Current text:

> *The same pattern works against live chain state once `LiveProvider` ships in v2.1 — the primitives don't care where the pool state came from.*

Change to:

> *The same pattern works against live chain state via* ``LiveProvider`` *(shipped in v2.1) — the primitives don't care where the pool state came from. See* `LiveProvider on defipy.org <https://defipy.org/live-provider/>`_ *for the V2 + V3 surface.*

**1c.** Fix the SPDX-Anchor typo. Current text: `🔗 DAPX-Anchor:`. Change to: `🔗 SPDX-Anchor:`.

**1d.** Update the "Quick install" line that says "For MCP server, chain reads, or Foundry workflows, see :ref:`installation`." Add a brief note that the canonical install reference is on defipy.org for the most up-to-date extras. Keep the :ref:`installation` link working.

### Edit 2 — `docs/installation.rst`

**2a.** Add `[chain]` extra section (after the existing `[mcp]` section, before `[book]`). Borrow language from defipy-org's installation.mdx, RST-flavored. Includes the web3 < 7.0 pin note.

**2b.** Add `[agentic]` extra section (after `[chain]`, before `[book]`). The "canonical Python SDK for Agentic DeFi" framing.

**2c.** Add the `:::note[zsh users]` equivalent in RST — sphinx admonition explaining the bracket-quoting requirement. Place near the top, after the core install snippet.

**2d.** Update all install command examples to use single-quoted form: `pip install 'defipy[chain]'` rather than `pip install defipy[chain]`. Five-ish occurrences across the page.

### Edit 3 — `docs/quick/whats_new_v2.rst`

**Decision: do not retitle this page.** It's "What's new in v2.0" and that title is honest — it describes what shipped at v2.0. Adding v2.1 content would dilute it. Instead:

**3a.** Add a top-of-page `.. note::` block: "This page describes v2.0. For v2.1 changes, see the [v2.1 release notes on GitHub](https://github.com/defipy-devs/defipy/releases/tag/v2.0.0) and [defipy.org](https://defipy.org/)." (Adjust release tag to actual v2.1.0 tag once it exists.)

**3b.** Update the "What's deferred to v2.1+" section's first bullet — the LiveProvider line — to reflect that LiveProvider has shipped:

> Was: *LiveProvider implementation (ABC + stub ship in v2.0; on-chain snapshot construction is v2.1)*
> Now: *LiveProvider implementation — shipped in v2.1 for Uniswap V2 and V3. Balancer and Stableswap LiveProvider ship in v2.2.*

**3c.** Update the test count in the "Test coverage" section: 629 → 686 with note about the 11 skipped live-RPC tests.

**3d.** Leave the rest of the page intact. v2.0 was real; the page describes it accurately.

### Edit 4 — `docs/twin/index.rst`

**4a.** Update the LiveProvider class description in "Key Classes":

> Was: *(v2.1, stub in v2.0)* | "Ships as a stub in v2.0. Functional implementation lands in v2.1."
> Now: *(shipped in v2.1)* | "Constructs twins from live chain reads via web3-compatible RPC. Supports Uniswap V2 and V3. Balancer and Stableswap LiveProviders are v2.2 work."

**4b.** Update the bottom note about PoolSnapshot fields:

> Was: *PoolSnapshot stays minimal in v2.0 — no `block_number`, `timestamp`, or `chain_id`. Those are LiveProvider concerns and ship in v2.1 when they're actually needed.*
> Now: *PoolSnapshot carries `block_number`, `timestamp`, and `chain_id` as `Optional[int]` fields. LiveProvider populates them; MockProvider leaves them None to honestly signal "synthetic, not chain state."*

**4c.** Add a `.. note::` near the top pointing to defipy.org for canonical State Twin / LiveProvider docs.

### Edit 5 — `docs/twin_concept.rst`

**5a.** Same LiveProvider class-description update as Edit 4a (this page duplicates the Key Classes section).

**5b.** Same PoolSnapshot fields note update as Edit 4b.

**5c.** Update the body paragraph: *"`MockProvider` builds twins from canonical recipes for notebooks and demos. `LiveProvider` (v2.1) will build them from live chain reads."* → drop the future tense: *"`LiveProvider` (shipped in v2.1) builds them from live chain reads."*

**5d.** Add the same defipy.org canonical-docs `.. note::` near the top.

### Edit 6 — `docs/twin/live_provider.rst`

Replace the entire stub content with a redirect-flavored note:

```rst
.. _live_provider:

LiveProvider
====================

.. note::

   **LiveProvider documentation has moved to defipy.org.**

   The canonical reference for ``LiveProvider`` — including the V2 + V3
   quickstarts, ``get_w3()`` escape hatch, block pinning, V3 tick range
   semantics, Multicall3 batching, chain context fields, and the full
   API surface — is published at
   `defipy.org/live-provider <https://defipy.org/live-provider/>`_.

   This page is preserved as a stable URL for inbound references.
```

### Edit 7 — `docs/twin/mock_provider.rst`

Same redirect treatment, pointing at defipy.org's State Twin Concept page (which covers MockProvider):

```rst
.. _mock_provider:

MockProvider
====================

.. note::

   **MockProvider documentation has moved to defipy.org.**

   The canonical reference for ``MockProvider`` and its four canonical
   recipes (``eth_dai_v2``, ``eth_dai_v3``, ``eth_dai_balancer_50_50``,
   ``usdc_dai_stableswap_A10``) is published at
   `defipy.org/twin-concept <https://defipy.org/twin-concept/>`_.

   This page is preserved as a stable URL for inbound references.
```

### Edit 8 — `docs/twin/custom_twins.rst`

Same redirect treatment, pointing at defipy.org's State Twin Concept page (or its custom-providers section if that subsection exists at deploy time — verify before committing):

```rst
.. _custom_twins:

Building Custom Twins
=======================

.. note::

   **Custom Twins documentation has moved to defipy.org.**

   The canonical reference for writing a custom ``StateTwinProvider`` —
   including the worked CSV-backed provider example — is published at
   `defipy.org/twin-concept <https://defipy.org/twin-concept/>`_.

   This page is preserved as a stable URL for inbound references.
```

### Edit 9 — `docs/roadmap.rst`

**9a.** Move LiveProvider implementation from "v2.1 (next)" to a new "v2.1 (shipped)" section — or fold the v2.0/v2.1 sections together as "v2 (shipped)" and have v2.2+ be the planning surface.

Recommended: rename existing "v2.0 (shipped)" to "v2.0 (shipped 2026-04)" and add a new "v2.1 (shipped 2026-05)" section above it (or below; chronological order doesn't matter much). The v2.1 section should list:

- LiveProvider for V2 + V3
- Multicall3 batching
- get_w3() escape hatch
- PoolHealth ergonomics (fee_pips, tvl_in_token1, tick_current)
- [chain] and [agentic] install extras
- Fork-and-evaluate worked example
- 686 tests (11 skipped live-RPC)

**9b.** Update the "v2.1 (next)" → "v2.2 (next)" section. Items that move from v2.1 to v2.2:

- Balancer LiveProvider
- Stableswap LiveProvider
- V3 tick bitmap walking
- AssessLiquidityDepth
- Multi-format tool schemas (anthropic, openai)
- Anvil fork integration tests

**9c.** Update the changelog table at bottom — add v2.1.0 release line.

### Edit 10 — `docs/agentic_overview.rst`

**10a.** Update the bullet describing `defipy.twin`:

> Was: *`defipy.twin` — a state-source abstraction (MockProvider ships; LiveProvider stub is v2.1)*
> Now: *`defipy.twin` — a state-source abstraction (MockProvider + LiveProvider both ship in v2.1; LiveProvider supports Uniswap V2 and V3)*

**10b.** Add a `.. note::` pointing at defipy.org for canonical agentic docs.

---

## Verification

After all edits land, before pushing:

```bash
cd defipy-docs/docs
sphinx-build -b html . _build/html -W --keep-going
```

The `-W` flag treats warnings as errors. The `--keep-going` flag completes the build despite warnings to surface all of them.

Look for:

- ✅ Build completes without errors
- ✅ No "document isn't included in any toctree" warnings (orphaned pages)
- ✅ No "undefined label" warnings (broken `:ref:` targets)
- ✅ No `.rst` parse errors
- ✅ The maintenance banner renders at the top of `_build/html/index.html`
- ✅ The three twin/ stub pages render their redirect notes
- ✅ Installation page shows `[chain]` and `[agentic]` sections
- ✅ Roadmap page shows v2.1 in shipped section
- ✅ whats_new_v2 page has the top "see also v2.1 release notes" note

Spot-check pages in browser: open `_build/html/index.html`, click through to installation, twin/index, twin_concept, roadmap, whats_new_v2, agentic_overview. Verify content reads coherently with the v2.1 reality.

---

## Time budget

Realistic estimates per edit, in order:

| Edit | Scope | Time |
|---|---|---|
| 1 | index.rst — banner + 3 small fixes | 15 min |
| 2 | installation.rst — 4 sub-edits, RST formatting | 20 min |
| 3 | whats_new_v2.rst — note block + 2 line edits | 10 min |
| 4 | twin/index.rst — 3 small edits | 10 min |
| 5 | twin_concept.rst — 4 small edits | 10 min |
| 6, 7, 8 | three stub redirects | 10 min total |
| 9 | roadmap.rst — restructure v2.0/v2.1/v2.2 | 15 min |
| 10 | agentic_overview.rst — 2 small edits | 5 min |
| Verification | local sphinx-build + spot-checks | 15 min |
| **Total** | | **~110 min** |

Add ~30 minutes buffer for any RST formatting edge cases or edits that need a second pass after the build catches something. **Realistic total: 90–150 minutes.**

---

## What this work doesn't do (and that's okay)

Honest accounting of the remaining staleness after this spec lands:

- **The agentic_primitives notebooks still narrate as "v2"** — fine, they describe the substrate as v2 generally, no v2.0/v2.1 distinction in the math
- **The `docs/_legacy/` tree still exists** — verify it's not on any toctree; if it is, leave the warning for a follow-up cleanup
- **Theme is still sphinx_rtd_theme** — that's a v3.0 horizon item per the existing roadmap; not this spec's job
- **No `[chain]` install verification on RTD's actual build environment** — RTD builds the docs, not DeFiPy with extras; the `[chain]` mentions are documentation, not RTD-execution code
- **The duplicate `docs/agentic/` directory** — verify it's not toctree-active; if it is, fold its v2.1 alignment into Edit 10's scope

These are known incompletenesses, deliberately deferred. The principle holds: stop misinformation, signal the canonical site, don't commit to maintenance parity.

---

## What "done" looks like

A reader who lands on `defipy.readthedocs.io` from a Google search:

1. Sees a clear "this site is in maintenance mode; defipy.org is canonical" banner at the top
2. Gets factually correct information about v2.1 features (LiveProvider works, get_w3() exists, [chain] and [agentic] are install options)
3. Doesn't hit empty stub pages
4. Sees the roadmap reflect v2.1 as shipped, with v2.2 as the next planning surface
5. Has clear paths back to defipy.org for canonical content

A reader who knows DeFiPy is on v2.1 doesn't experience cognitive dissonance reading the RTD site. A reader who only knows DeFiPy from Google's old indexing of the RTD site gets a soft landing — accurate information, with a clear next step.

That's the bar. Nothing more is in scope.

---

## Open question

**The `docs/_legacy/` and `docs/agentic/` duplicate trees — fold into this spec or defer?**

Both directories appear to contain content that may or may not be active on the live toctree. A pre-execution sanity check: `grep -rn "_legacy\|^agentic/" docs/index.rst docs/conf.py` will show whether either is referenced.

If neither is on the toctree, leave them alone — they're inert. If either *is* on the toctree, fold its v2.1 alignment into this spec's relevant edit (the agentic/ one would join Edit 10; the _legacy/ one is a separate question of "do we just remove the directory?").

Recommend resolving this question during Edit 1 (when `index.rst` is open anyway) and adding any newly-discovered toctree-active duplicate to the appropriate edit.

---

*Spec authored: 2026-05-07*
*Target execution: post-PyPI push, when energy permits*
*Anchor on completion: optional but recommended given the file lives in `defipy-docs/`*
