# Build status · Banpu Claude for Business course materials

Updated 31 Oct 2026 by the course-orchestrator. Plan: `PLAN.md` (approved 30 Oct 2026) · Scope: `proposal/proposal.html` · Conventions: [STYLE.md](STYLE.md) · Sources: [SOURCES.md](SOURCES.md)

## Summary
All 8 modules are built and on `origin/master`. Each module was delegated to one Claude worker through Orca orchestration (run `run_2334d6bc8431`, at most 2 module workers at a time), then reviewed by the orchestrator against the page budget and the rules in AGENTS.md before commit.

Workers were repeatedly cut off by API connection loss ("Connection lost mid-response" / "The response stopped arriving") while writing large files. When that happened the orchestrator either resumed or relaunched the worker through Orca, or finished the remaining files itself. The "Built by" column records which.

**31 Oct 2026, second pass — everything learners and the trainer use is now a Claude Artifact on claude.ai (29 Artifacts: 8 Slides decks, 8 workshop sheets, 13 interactive pages; table below).**
- Lecture decks: every `slides.md` was rebuilt on Claude's core **Slides Artifact type** (same slide count, content and speaker notes; Mermaid diagrams redrawn natively with boxes + connectors in the 3 colours, legend on every diagram slide). PDF/PPTX export is built into the type (Share › Export). M1 was built by the orchestrator as the prototype; M2–M8 by Orca Claude workers (run `run_6946e31302a7`, max 2 at a time) following `materials/_shared/SLIDES_ARTIFACT_BRIEF.md`. Sources live in `materials/<mN>/deck/project/`; `slides.md`/`slides.html` remain as the content source, superseded for delivery.
- Workshop sheets: every `workshop.md` is now `materials/<mN>/artifacts/workshop-sheet.html` (same page count, copy-ready prompts, checkbox checkpoints, progress bar, workshop diagrams) and every existing interactive Artifact was published as its own Artifact. Built by Orca Claude workers following `materials/_shared/WORKSHOP_ARTIFACT_BRIEF.md`.
- Export PDF on every published page: `materials/_shared/export-pdf-artifact.html` builds an A4 PDF in the page (html2pdf.js 0.10.1) and offers it through the `downloads` capability; it falls back to the browser print dialog where that is unavailable (e.g. the file opened locally).
- Review: the orchestrator checked every module (counts vs source, diagrams + legend, notes, no text under 24px on slides, Export PDF markers, no Samsung, URLs in README) and confirmed each published file equals the committed file before committing per module.
- M1's opening story was changed on Prem's request: the Samsung 2023 case is removed everywhere and replaced by the July 2025 shared-ChatGPT-chats-in-Google case (Fast Company; SOURCES #1–2).

## Modules
| Module | Time | Slides (budget) | Workshop pages (budget) | Diagrams | Artifacts (all with Export PDF) | Story / case | Built by | Commit |
|---|---|---|---|---|---|---|---|---|
| M1 Foundation & Security First | 60′ | 41 (40) | 4 (4) | 7 | Data Traffic Light game | Shared ChatGPT chats indexed by Google 2025 · Cato CTRL weaponised Skill 2025 | worker | `402d92f` |
| M2 Files & Folders + Prompt Patterns | 45′ | 15 (15) | 6 (6) | 8 | Workshop Companion · Prompt Playground · Excel Detective · Prototype Gallery | Replit agent deletes production DB 2025 · Matt Pocock `grill-me` | worker + orchestrator (README, SOURCES, specs) | `b958b6d` |
| M3 M365 Connectors | 45′ | 15 (15) | 6 (6) | 6 + 1 | Connector Mission | PHE 15,841 COVID cases lost in Excel 2020 · fictional Capex Tracker overwrite | worker + orchestrator (workshop, Artifact, IT setup, README, SOURCES) | `a12a3d6` |
| M4 Document Factory & Artifacts | 40′ | 15 (15) | 5 (5) | 6 | Monthly Ops Dashboard (v1/v2) · Output Picker | Deloitte Australia AI-error report refund 2025 | worker | `9b18a9f` |
| M5 Skills & Plugins | 30′ | 10 (10) | 4 (4) | 5 | Skill Security Checklist | ClawHavoc: 341 malicious Skills on ClawHub 2026 | worker | `1801c9d` |
| M6 Automation | 35′ | 15 (15) | 4 (4) | 8 | Automation Card | Air Canada chatbot ruling 2024 | worker ×3 + orchestrator (README, SOURCES, story swap) | `67c740b` |
| M7 Capstone | 75′ | 10 (10) | 13 (13) | 9 | Show & Share board | Novo Nordisk clinical documentation with Claude | worker (relaunched once) | `956364d` |
| M8 Security recap, Quiz & 30-day plan | 45′ | 20 (20) | 5 (5) | 9 | Security & Usage Quiz (18 Q + Traffic Light final round) · แผน 30 วัน | Microsoft AI research 38TB shared-link exposure (Wiz, 2023) | worker ×2 + orchestrator (plan Artifact script + spec, workshop, README, SOURCES) | `cc778ca` |

## Claude Artifacts on claude.ai (all 29)
Each module README has the same list under `## Claude Artifacts (claude.ai)`.

**Visibility (checked 31 Oct 2026): all 29 are still private.** Prem asked for "anyone with the link, no login". That could not be done from this session:
- The Artifact tool cannot change sharing or visibility; it is set only from each page's **Share** menu on claude.ai, by the owner.
- A logged-out `curl` returns HTTP 200 for all 29 URLs, but every response is the same generic app shell (title "Claude Artifact", ~35 KB, no module content); the Artifact content and the access check load afterwards in the browser. So HTTP 200 does **not** show the page is public. A real check means opening each link in a private/incognito window after sharing.
- Expected limits when sharing:
  - The 8 Slides decks get the `assets` and `mcp` (Google Drive) capabilities from the Slides type. Per the Artifact runtime docs, pages with these are organisation-internal and cannot be shared publicly. Expect at most "everyone in the organisation" for the decks; the PDF/PPTX export (Share › Export) is the way to hand a deck to people outside.
  - The 21 workshop and interactive pages declare only `downloads`, so the page itself does not block public sharing. Whether a public link is allowed depends on the account's plan and admin settings (M4's notes cite the Help Center saying Team-plan Artifacts are shared within the organisation only).

| Module | Artifact | Source in repo | claude.ai URL | Export PDF |
|---|---|---|---|---|
| M1 | Slides · 41 slides | `m1/deck/project/` | https://claude.ai/artifact/B5QugBgGE4eWMe69TrCvbv | Share › Export (PDF/PPTX) |
| M1 | Workshop sheet · 4 หน้า | `m1/artifacts/workshop-sheet.html` | https://claude.ai/artifact/W9dt4fKCCRZn4pZMXycNdR | ✅ |
| M1 | Data Traffic Light (เกม 15 ใบ) | `m1/artifacts/data-traffic-light.html` | https://claude.ai/artifact/F9jhpdSui1ybEe4M794LvZ | ✅ |
| M2 | Slides · 15 slides | `m2/deck/project/` | https://claude.ai/artifact/3kKwMXkqyNFfRMEQxCQVwu | Share › Export (PDF/PPTX) |
| M2 | Workshop sheet · 6 หน้า | `m2/artifacts/workshop-sheet.html` | https://claude.ai/artifact/2kVCrZwhnqqwMHBF326PvR | ✅ |
| M2 | Workshop Companion | `m2/artifacts/workshop-companion.html` | https://claude.ai/artifact/Vyp7t1u44Ga5W4YbpuMYdP | ✅ |
| M2 | Excel Detective | `m2/artifacts/excel-detective.html` | https://claude.ai/artifact/1ytRQDkazJW4Xw24zZwkLu | ✅ |
| M2 | Prompt Playground | `m2/artifacts/prompt-playground.html` | https://claude.ai/artifact/LQ7Mh4vNj4syXPARm6ucV8 | ✅ |
| M2 | Prototype Gallery | `m2/artifacts/prototype-gallery.html` | https://claude.ai/artifact/3s1YpuHwGK7QvSn7ogm2Aq | ✅ |
| M3 | Slides · 15 slides | `m3/deck/project/` | https://claude.ai/artifact/MFFCrgSvtQS9S4guydcnoz | Share › Export (PDF/PPTX) |
| M3 | Workshop sheet · 6 หน้า | `m3/artifacts/workshop-sheet.html` | https://claude.ai/artifact/WTTy6F421gQfVwrxUFSax1 | ✅ |
| M3 | Connector Mission | `m3/artifacts/connector-mission.html` | https://claude.ai/artifact/F4gquxgXQwnB8cSTo3hsBq | ✅ |
| M4 | Slides · 15 slides | `m4/deck/project/` | https://claude.ai/artifact/KgQ57jcEaEb58SShmpLqkr | Share › Export (PDF/PPTX) |
| M4 | Workshop sheet · 5 หน้า | `m4/artifacts/workshop-sheet.html` | https://claude.ai/artifact/WJDTLqhbUEgPCh3EbEMgFK | ✅ |
| M4 | Monthly Ops Dashboard (v1/v2) | `m4/artifacts/monthly-ops-dashboard.html` | https://claude.ai/artifact/5wEyprUmbagfBfBXXe4SJP | ✅ |
| M4 | Output Picker | `m4/artifacts/output-picker.html` | https://claude.ai/artifact/S47Pyq2mMTUk85nZ2HQL67 | ✅ |
| M5 | Slides · 10 slides | `m5/deck/project/` | https://claude.ai/artifact/PRZrJe9wv2nWeJSaTFy416 | Share › Export (PDF/PPTX) |
| M5 | Workshop sheet · 4 หน้า | `m5/artifacts/workshop-sheet.html` | https://claude.ai/artifact/VcgZfUcr3i1u6iWZpB1PN3 | ✅ |
| M5 | Skill Security Checklist | `m5/artifacts/skill-security-checklist.html` | https://claude.ai/artifact/8M5tgdbZfTgxtFuFkjXqqn | ✅ |
| M6 | Slides · 15 slides | `m6/deck/project/` | https://claude.ai/artifact/77u51h2Mek9CgrSedciouK | Share › Export (PDF/PPTX) |
| M6 | Workshop sheet · 4 หน้า | `m6/artifacts/workshop-sheet.html` | https://claude.ai/artifact/WpGFhe1gXGwqSYhLeteZYo | ✅ |
| M6 | Automation Card | `m6/artifacts/automation-card.html` | https://claude.ai/artifact/HFdt3zwrfBgErGfv6q5TUk | ✅ |
| M7 | Slides · 10 slides | `m7/deck/project/` | https://claude.ai/artifact/17aWEiXMohcTuVjq2mKxzh | Share › Export (PDF/PPTX) |
| M7 | Workshop sheet · 13 หน้า | `m7/artifacts/workshop-sheet.html` (from `build_workshop_sheet.py`) | https://claude.ai/artifact/GYFfuKNKMURfsooszp4cKc | ✅ |
| M7 | Show & Share Board | `m7/artifacts/show-share-board.html` | https://claude.ai/artifact/VncwbAfqEmSuDFBtGfx5uy | ✅ |
| M8 | Slides · 20 slides | `m8/deck/project/` | https://claude.ai/artifact/Uix5PCdLVDFT2EpceDUi1Q | Share › Export (PDF/PPTX) |
| M8 | Workshop sheet · 5 หน้า | `m8/artifacts/workshop-sheet.html` | https://claude.ai/artifact/CQD1FRgAQ1T27Lx4MSJ59L | ✅ |
| M8 | Security & Usage Quiz | `m8/artifacts/security-quiz.html` | https://claude.ai/artifact/L6PcYj1MiRy7Aah9cUVgsv | ✅ |
| M8 | แผน 30 วันของฉัน | `m8/artifacts/plan-30-days.html` | https://claude.ai/artifact/Dn5jDTNdz6YBP8DT23T7Nt | ✅ |

Republish after an edit: decks with the Artifact tool (`url` + `root: materials/<mN>/deck`, changed slide files only); pages with the Artifact tool and the same `file_path` (keep `capabilities: {downloads: true}`).

## Rules check (all modules)
- Thai learner-facing text; technical terms in English.
- Synthetic data only: fictional sites/people, emails `@example.com`, generators committed, large outputs (> 5 MB) gitignored and regenerable.
- M365 connectors only (SharePoint, Outlook). Google Drive appears only as "not allowed". No Copilot content.
- Every workflow has a diagram using the 3 colour classes (คน/HITL · AI · Data/Connector). Mermaid sources stay in `diagrams/*.mmd`; the Slides Artifacts redraw all 52 slide diagrams natively with a legend; workshop sheets render theirs with Mermaid 10.9.1 or inline SVG.
- Every published Artifact has Export PDF: Slides via the type's Share › Export (PDF/PPTX); every page via the `downloads`-based Export PDF button with print fallback.
- Every module has at least one story or real case. No case is repeated across modules (M3 and M6 originally reused the Replit case and were changed; M5's notes deliberately call back to M1's Cato case).
- External sources are listed per module in `materials/<mN>/SOURCES.md` and merged into `materials/SOURCES.md` (link-only unless the licence allows reuse). Generated illustrations are marked as original.

## Shared tooling
- `tools/build_slides.py` — renders `slides.md` to a 16:9 HTML deck. Arrow keys navigate, `N` shows notes, `P` prints (one slide per PDF page).
- `tools/merge_sources.py` — rebuilds `materials/SOURCES.md` from module source lists.
- `materials/_shared/export-pdf.html` — original print-based Export PDF snippet (local files only).
- `materials/_shared/export-pdf-artifact.html` — Export PDF for published Artifacts (html2pdf.js → `downloads.save`, print fallback).
- `materials/_shared/SLIDES_ARTIFACT_BRIEF.md` · `materials/_shared/WORKSHOP_ARTIFACT_BRIEF.md` — worker briefs for the Slides decks and the workshop/interactive Artifacts.
- `materials/m7/artifacts/build_workshop_sheet.py` — regenerates the 13-page M7 workshop sheet from `workshop.md`.

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
8. Naming real firms in stories (OpenAI/ChatGPT, Replit, Deloitte, Air Canada, Novo Nordisk): OK for a Banpu audience?
9. External energy data: keep IMF/FRED (citation wording to confirm) or add a Thai source such as EPPO (M4).
10. Skill approver role, sharing location, Plugin policy and whether to align the Skill checklist with IT approval (M5).
11. Illustrations: only M2 has generated illustrations (2). Add up to 2 per module?

**M8**
12. Course evaluation form (Hi-I's own or ours), whether quiz scores should be collected for Hi-I reporting (currently they stay on each learner's machine), and who receives the 30-day plans.

**Logistics**
13. Distribution of data packs (M2 core pack, M3 pack, M4 ~49 MB pack, M6/M7 zips): training SharePoint site or USB.
14. Matt Pocock `grill-me` licence (MIT per listings): confirm against the repo LICENSE before printing handouts (M2).

**Claude Artifacts (new, 31 Oct)**
15. Sharing: all 29 Artifacts are private to Prem's account. Prem asked for public links (no login); the tool cannot set this. Open each URL, Share menu → the widest option offered (public link where the plan allows; otherwise the organisation), then check each in an incognito window. If public links are not allowed, decide between organisation-only sharing (learners log in with their Banpu Team account) and PDF exports for anyone outside.
16. Live check still to do in the browser: click Export PDF on each page once (the in-page PDF path was not clicked through in this session) and download one deck as PDF from Share › Export, checking Thai rendering and that the 3-colour diagrams survive.
17. Prototype Gallery (M2) shared voting expects a shared store that claude.ai does not provide, so votes stay per browser. Switch it to the Artifact `db` capability for a room-wide tally?
18. While the decks were being written, a second writer re-saved near-identical copies of some slides (every deck; most likely the Slides page in an open browser tab normalising files). All versions were read and kept/merged and the repo equals what is published; worth confirming no other session was editing.

## Next steps (build order 7)
- Dry-run on a Banpu Claude Team account: time each workshop, check usage consumption, confirm connector and Cowork behaviour.
- Re-check the Help Center facts flagged in module READMEs the week of training.
