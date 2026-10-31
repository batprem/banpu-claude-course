# Brief: publish a module's workshop sheet and interactive Artifacts on claude.ai

Owner: course-orchestrator. Requirement from Prem (31 Oct 2026): every workshop sheet and every learner Artifact is a published Claude Artifact with Export PDF.

## Before writing anything
- Read `AGENTS.md`, `materials/STYLE.md`, `materials/<mN>/workshop.md`, `materials/<mN>/README.md`.
- Artifact tool: `action: "quickstart"`, `intent: "other"` once for the workshop sheet (a page to use and print, not an editable doc). Build it as a hand-written HTML page; do not start it from a Docs/Slides type.
- Load the `artifact-design` skill (page contract: title, tokens, dark mode, phone width, allowed CDNs) and the `artifact-capabilities` skill (`downloads`).

## 1. Workshop sheet → `materials/<mN>/artifacts/workshop-sheet.html` (new)
- Learner-facing Thai, **same content and the same page count** as `workshop.md`: one `<section class="card pdf-page-break">` per `## ` page (the first without `pdf-page-break`), in order. Page budget = 1 page per 5 workshop minutes; do not add or drop pages.
- Each step keeps: เป้าหมาย · Prompt (copy-ready block with a **Copy** button, `no-print`) · ✅ checkpoint (a real checkbox; remember ticks in `localStorage` wrapped in try/catch, convenience only) · time.
- Engagement: a sticky progress bar (pages ticked / total) and a per-page time chip. Keep it calm and printable.
- Every Mermaid diagram in workshop.md stays a diagram: render with `https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js` (exact version) keeping the classDefs `human #E4572E / ai #2E86AB / data #3BA55C` and the legend line; or inline SVG.
- Font IBM Plex Sans Thai (Google Fonts), colours from STYLE.md, works at phone width.
- `<title>`: "<mN> Workshop" style (2–4 words). `<body data-pdf-name="<mN>-Workshop">`.

## 2. Export PDF (every page you publish)
- Use `materials/_shared/export-pdf-artifact.html` exactly (html2pdf.js → `downloads.save`, fallback `window.print()`), and publish with `capabilities: {downloads: true}`.
- In existing interactive Artifacts, replace the old `export-pdf.html` button/styles with this snippet (keep their `no-print` / `print-expand` classes; add `pdf-page-break` only where a page break is wanted). Change nothing else in their behaviour.

## 3. Interactive Artifacts → publish each `materials/<mN>/artifacts/*.html` (except workshop-sheet, done above)
- Read the **whole** file before publishing (rule). Synthetic data only; external loads only Google Fonts / allowed CDNs with exact versions; no network calls, no AI calls unless the spec says so. Fix only what the page contract or the Export PDF rule requires; note any fix.
- Publish each as its own Artifact (`file_path` = that file, `icon` one generic word, one-sentence Thai/English `description`, `capabilities: {downloads: true}`). Re-publishing later: same file path, omit `icon`.

## 4. Record
- In `materials/<mN>/README.md` add a section `## Claude Artifacts (claude.ai)` — a table: Artifact · file · claude.ai URL · Export PDF ✅ — including the module's Slides Artifact URL already in the Files table.
- Report every URL in worker_done. Do not edit other modules, `STATUS.md`, STYLE.md, tools, slides or the Slides decks. Do not commit or push.

## Acceptance (orchestrator re-checks)
- workshop-sheet.html `card` sections = `## ` pages in workshop.md; every prompt code block present; checkpoints are checkboxes; diagrams present.
- Every published file in `artifacts/` contains `export-pdf-artifact` markers (`exportPdfBtn`, `downloads`) and no old `onclick="window.print()"` button.
- Every URL listed in README and in worker_done; local files are what was published.
- Samsung is never mentioned (removed from the course).
