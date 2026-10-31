# Brief: rebuild a module's lecture deck as a Claude Slides Artifact

Owner: course-orchestrator. Prototype and reference: M1 (`materials/m1/deck/`, https://claude.ai/artifact/B5QugBgGE4eWMe69TrCvbv).

## Goal
Turn `materials/<mN>/slides.md` into a deck built on Claude's **core Slides Artifact type**. Keep the **same slides in the same order, the same content and the same speaker notes**. No new facts, numbers or cases; wording may be trimmed only to fit.

## How
1. Read `AGENTS.md`, `materials/STYLE.md`, `materials/<mN>/slides.md`, and the M1 reference slides in `materials/m1/deck/project/slides/` (s01 cover, s03 story, s04 section divider, s05 table, s07/s17/s21/s29/s32/s35 pinned diagrams, s39 flow diagram).
2. `Artifact` tool: `action: "quickstart"`, `intent: "slides"`. Then create the deck with the returned `type_url`, `title: "<mN> · <module title>"`, `auto_open: "after_first_write"`, no files. Follow the type's instructions in the create result (they are the format authority). There is no design system; use the M1 look below.
3. Write the files with your file-writing tool (no generator scripts) under `root = materials/<mN>/deck`: `project/deck.json` (full `order`, `sections` = the module's section dividers, the IBM Plex Sans Thai face exactly as in M1's deck.json), then `project/slides/s01.html … sNN.html`. Publish deck.json + cover first, then 3 slides per publish.
4. If a publish is refused because someone else changed a file, read it and merge; never overwrite blindly.

## M1 look (copy, do not reinvent)
- Font `'IBM Plex Sans Thai', Tahoma, sans-serif`. Paper `#FAF8F3` content slides, ink `#1F2933` section dividers/cover with eyebrow `#F2A541`, muted text `#3A4651` / `#5B6670`.
- Type scale: h1 96, h2 60–64, body 34–38, tables 30–32, labels/footer 24. **Nothing under 24px.**
- Story/case slides: 24px orange bar on the left edge + eyebrow `เรื่องจริง · STORY`, quote block with `border-left:10px solid #E4572E`.
- Tables: header `tr` `#1F2933` with light text; rows alternate `#FFFDF8` / `#F3EDE2`.

## Diagrams (hard rule: every workflow keeps a diagram)
- Mermaid does not render in this type. Redraw **every** Mermaid diagram in the module with pinned `<div>` boxes + `<x-connector>` (see M1 s07/s17/s29), or flow layout for a straight chain (M1 s39). Read `artifact-type/reference/diagrams.md` and `diagram-recipes.md` from the deck (Artifact `read`, `path`) before the first diagram.
- Colours by Mermaid class: `human` → `#E4572E`, `ai` → `#2E86AB`, `data` → `#3BA55C`, white bold text ≥24px. Decisions = pill radius. Same nodes and edges as the Mermaid source; edge labels as pinned `<p>`, or "ถ้าใช่ / ถ้าไม่" first lines inside boxes.
- Every diagram slide carries the pinned legend row (คน (HITL) · AI · Data/Connector) at `bottom:56px`, slide padding `128px 128px 160px`.
- Put a node-list HTML comment above the boxes; compute connector endpoints from box edge midpoints.

## Notes, PDF, data
- Speaker notes from the `???` blocks go into one `<aside>` as the slide's last child (plain text, markdown stripped, ≤4000 chars).
- PDF/PPTX export is built into the type (Share › Export); nothing to add.
- Synthetic data only, M365 connectors only, Thai learner-facing text — exactly as in slides.md.

## Finish
- Update the Files table in `materials/<mN>/README.md` like M1's (rows: Slides Artifact URL · `deck/project/...` sources · `slides.md` superseded for delivery).
- Do not edit other modules, `materials/STATUS.md`, STYLE.md or tools. Do not commit or push (the orchestrator does).
- Report: Artifact URL, slide count vs slides.md, diagram count vs Mermaid blocks in slides.md, any content you had to trim.
