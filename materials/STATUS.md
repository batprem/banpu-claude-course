# Build status · Banpu Claude for Business course materials

Updated 31 Oct 2026 by the course-orchestrator. Plan: `PLAN.md` (approved 30 Oct 2026) · Scope: `proposal/proposal.html` · Conventions: [STYLE.md](STYLE.md) · Sources: [SOURCES.md](SOURCES.md)

## Summary
All 8 modules are built and on `origin/master`. Each module was delegated to one Claude worker through Orca orchestration (run `run_2334d6bc8431`, at most 2 module workers at a time), then reviewed by the orchestrator against the page budget and the rules in AGENTS.md before commit.

Workers were repeatedly cut off by API connection loss ("Connection lost mid-response" / "The response stopped arriving") while writing large files. When that happened the orchestrator either resumed or relaunched the worker through Orca, or finished the remaining files itself. The "Built by" column records which.

## Modules
| Module | Time | Slides (budget) | Workshop pages (budget) | Diagrams | Artifacts (all with Export PDF) | Story / case | Built by | Commit |
|---|---|---|---|---|---|---|---|---|
| M1 Foundation & Security First | 60′ | 41 (40) | 4 (4) | 7 | Data Traffic Light game | Samsung source-code leak 2023 · Cato CTRL weaponised Skill 2025 | worker | `402d92f` |
| M2 Files & Folders + Prompt Patterns | 45′ | 15 (15) | 6 (6) | 8 | Workshop Companion · Prompt Playground · Excel Detective · Prototype Gallery | Replit agent deletes production DB 2025 · Matt Pocock `grill-me` | worker + orchestrator (README, SOURCES, specs) | `b958b6d` |
| M3 M365 Connectors | 45′ | 15 (15) | 6 (6) | 6 + 1 | Connector Mission | PHE 15,841 COVID cases lost in Excel 2020 · fictional Capex Tracker overwrite | worker + orchestrator (workshop, Artifact, IT setup, README, SOURCES) | `a12a3d6` |
| M4 Document Factory & Artifacts | 40′ | 15 (15) | 5 (5) | 6 | Monthly Ops Dashboard (v1/v2) · Output Picker | Deloitte Australia AI-error report refund 2025 | worker | `9b18a9f` |
| M5 Skills & Plugins | 30′ | 10 (10) | 4 (4) | 5 | Skill Security Checklist | ClawHavoc: 341 malicious Skills on ClawHub 2026 | worker | `1801c9d` |
| M6 Automation | 35′ | 15 (15) | 4 (4) | 8 | Automation Card | Air Canada chatbot ruling 2024 | worker ×3 + orchestrator (README, SOURCES, story swap) | `67c740b` |
| M7 Capstone | 75′ | 10 (10) | 13 (13) | 9 | Show & Share board | Novo Nordisk clinical documentation with Claude | worker (relaunched once) | `956364d` |
| M8 Security recap, Quiz & 30-day plan | 45′ | 20 (20) | 5 (5) | 9 | Security & Usage Quiz (18 Q + Traffic Light final round) · แผน 30 วัน | Microsoft AI research 38TB shared-link exposure (Wiz, 2023) | worker ×2 + orchestrator (plan Artifact script + spec, workshop, README, SOURCES) | `cc778ca` |

## Rules check (all modules)
- Thai learner-facing text; technical terms in English.
- Synthetic data only: fictional sites/people, emails `@example.com`, generators committed, large outputs (> 5 MB) gitignored and regenerable.
- M365 connectors only (SharePoint, Outlook). Google Drive appears only as "not allowed". No Copilot content.
- Every workflow has a Mermaid diagram using the 3 colour classes (คน/HITL · AI · Data/Connector). All decks render every diagram on screen and in print (renderer fix `4ee4408`).
- Every learner Artifact has an Export PDF button + print CSS.
- Every module has at least one story or real case. No case is repeated across modules (M3 and M6 originally reused the Replit case and were changed; M5's notes deliberately call back to M1's Cato case).
- External sources are listed per module in `materials/<mN>/SOURCES.md` and merged into `materials/SOURCES.md` (link-only unless the licence allows reuse). Generated illustrations are marked as original.

## Shared tooling
- `tools/build_slides.py` — renders `slides.md` to a 16:9 HTML deck. Arrow keys navigate, `N` shows notes, `P` prints (one slide per PDF page).
- `tools/merge_sources.py` — rebuilds `materials/SOURCES.md` from module source lists.
- `materials/_shared/export-pdf.html` — Export PDF snippet for Artifacts.

## Open questions for Prem / Hi-I (consolidated)
**Banpu tenant & IT**
1. Name of Banpu's approved tool for sensitive data (M1 slide 27, M8 rule 1 and quiz Q01), and whether Banpu has an official data classification to align the 15 Data Traffic Light cards with (M1).
2. Team-plan facts to re-check the week of training: audit/Compliance API vs Enterprise (M1), model menu (M1), Skills + code execution enabled (M5), file creation and Artifact sharing enabled (M4).
3. Test tenant: test accounts, `M3-Training` SharePoint site and test mailbox — or route B (local Sample Pack) for everyone (M3, M6, M7). See `materials/m3/data/IT_SETUP.md`.
4. Are M365 write tools enabled? The course assumes read-only (M3). Can admins disable "Automatically approve" in Cowork (M6)?
5. Outlook attachment size limit at Banpu (M4 slide 12).
6. Scheduled-task run conditions: Help Center pages disagree on remote vs local runs. Verify in the dry-run (M6).

**Content decisions**
7. Real Hi-I use cases: replace the 5 stand-in use cases or run them as bring-your-own (M7). Also per-class headcount, which sets the pitch length.
8. Naming real firms in stories (Samsung, Replit, Deloitte, Air Canada, Novo Nordisk): OK for a Banpu audience?
9. External energy data: keep IMF/FRED (citation wording to confirm) or add a Thai source such as EPPO (M4).
10. Skill approver role, sharing location, Plugin policy and whether to align the Skill checklist with IT approval (M5).
11. Illustrations: only M2 has generated illustrations (2). Add up to 2 per module?

**M8**
12. Course evaluation form (Hi-I's own or ours), whether quiz scores should be collected for Hi-I reporting (currently they stay on each learner's machine), and who receives the 30-day plans.

**Logistics**
13. Distribution of data packs (M2 core pack, M3 pack, M4 ~49 MB pack, M6/M7 zips): training SharePoint site or USB.
14. Matt Pocock `grill-me` licence (MIT per listings): confirm against the repo LICENSE before printing handouts (M2).

## Next steps (build order 7)
- Dry-run on a Banpu Claude Team account: time each workshop, check usage consumption, confirm connector and Cowork behaviour.
- Re-check the Help Center facts flagged in module READMEs the week of training.
