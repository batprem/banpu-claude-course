# Brief: rewrite the speaker notes of a Slides deck (word-for-word script + tips)

Owner: course-orchestrator. Requested by Prem on 2 Nov 2026 for every slide of the 8 decks.

## Format of every `<aside>` (plain text, no markdown, ≤ 4,000 characters)
```
<script: exactly what the speaker says, in natural spoken Thai>
----------
<tips: timing marks, cues, what to demo/show, cautions, sources (SOURCES #n), open questions>
```
- The separator is a line containing exactly ten hyphens `----------` and nothing else. Exactly one per slide.
- **Script** (above the line): word-for-word, natural spoken Thai as the trainer would actually say it (เรา/คุณ, short sentences, friendly-professional; the deck already uses "ครับ", keep that). Product and technical terms stay in English (Claude, Cowork, Project, Skill, Artifact, Connector, SharePoint, Outlook, Human-in-the-Loop, Plan → Approve → Execute …). It must fit the slide's time: about 1 minute per content slide (roughly 120–180 Thai words / 400–700 Thai characters); section dividers, cover and closing slides 15–30 seconds; workshop/demo slides: the script covers what is said on that slide (the instructions/hand-off), and the tips say how long the activity runs. Ask the room questions in the script where the old notes suggested them.
- **Tips** (below the line): keep every useful fact from the existing notes — minute marks like `[5:00]`, demo steps, prompt IDs (M1-P02 …), file paths, fallback plans, sources and dates, Open questions, cautions. Reword into short lines. Do not lose any source citation or caution.
- Use only what the slide and the existing notes say. Never invent facts, numbers, names, quotes or anecdotes. Synthetic data only; no real Banpu data; M365 connectors only; never mention Samsung.

## Rules
- Change ONLY the text inside `<aside>…</aside>`. Everything else in each slide file stays byte-for-byte identical (content, styles, ids, order, deck.json). Do not add or remove slides.
- First `Artifact read` the deck's `project/deck.json` and all slide files (out_dir in your scratchpad) and compare with the repo; if a published file differs, adopt the published version before editing.
- Edit slide files with the Edit tool (Slides type rule: no scripts that generate slide files). Keep each response small — at most ~4 slides per response — because long outputs get cut by connection drops.
- After every few slides, republish the changed slide files to the SAME `url` with `root: materials/<mN>/deck` (deck.json is not sent; it does not change).
- Check with `python3 tools/check_notes.py <mN>` (non-aside content unchanged vs git HEAD, one separator per aside, script and tips both non-empty, ≤ 4,000 chars) until it prints `problems: none`, then read back 3 published slides.
- Report in worker_done: deck URL, slides changed / total, the check output, the sharing line from the last publish result. Do not commit or push; edit nothing outside `materials/<mN>/deck/project/slides/`.
