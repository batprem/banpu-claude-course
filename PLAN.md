# Course materials plan (draft, not approved yet)

## Modules (from proposal)
M1 Foundation & Security First · M2 Cowork with files and folders · M3 M365 Connectors · M4 Document Factory & Artifacts
M5 Skills & Plugins · M6 Automation · M7 Capstone · M8 Security recap, quiz, 30-day plan

## Prompt Patterns (lesson in M2)
1. Use your own words: the agent restates the goal before acting.
2. Interview pattern: the agent asks us one question at a time to gather context, then writes a brief for us to confirm.
3. Prototype first: e.g. 3 slide-style samples to choose from before building the full deck.

## Workshops
- A. PowerPoint with Claude: Interview → Use your own words → Explore → Research → Plan → Prototype ×3 → Review → Build (human check between steps).
- B. Analyse scattered Excel files in a folder: explore → find files → align schemas → merge → analyse → insight/dashboard. Its output can feed Workshop A.

## Diagrams
Slide workflow · Scattered Excel → Insight · AI→Connect→Data→Execute · Document Factory → Schedule · Monitoring · Chat/Project/Skill/Agent/Artifact decision tree · Data Traffic Light

## Engagement Artifacts
Workshop Companion (steps, checklist, copy-prompt) · Prompt Playground (before/after) · Data Traffic Light game · Prototype Gallery (vote) · Excel Detective (missions) · Show & Share board

## Build order
1. Lock the TOC  2. Sample Data Pack  3. Prompt templates  4. Lecture slides  5. Workshop guides + diagrams  6. Quiz/checklists/appendix  7. Dry-run on a Claude Team account (usage + timing)

## Checks
Artifact sharing needs company Claude accounts · Artifacts that call AI use up Team plan usage.

## Added requirements (30 Oct)
- Every learner Artifact must have an "Export PDF" option (print-to-PDF with print CSS).
- Page budget: Lecture = 1 slide per minute; Workshop = 1 page per 5 minutes.
- Visuals: infographics/diagrams can be made with the Codex agent, but use real photos/screenshots/references too
  (e.g. Interview pattern → Matt Pocock and his "grill me" skill). Cite every external image/source in materials/SOURCES.md and check usage rights.
- Use stories and real cases where they fit (each module: at least 1 story or case, with its source).

## Agent setup (Claude Code subagents in .claude/agents/)
- Max 1 module agent running at a time besides the leader (sequential: M1 → M8).
- course-orchestrator: delegates 1 module per agent, checks page budgets, keeps style and terminology consistent, merges.
- module-m1 … module-m8: each builds its module's slides + materials (handout, prompts, diagrams, Artifact spec) inside materials/<module>/.

## Page budget per module (from agenda)
| Module | Time | Split (lecture/workshop min) | Slides | Workshop pages |
|---|---|---|---|---|
| M1 Foundation & Security | 60 | 40 / 20 | 40 | 4 |
| M2 Files & Folders + Prompt Patterns | 45 | 15 / 30 | 15 | 6 |
| M3 M365 Connectors | 45 | 15 / 30 | 15 | 6 |
| M4 Document Factory & Artifacts | 40 | 15 / 25 | 15 | 5 |
| M5 Skills & Plugins | 30 | 10 / 20 | 10 | 4 |
| M6 Automation | 35 | 15 / 20 | 15 | 4 |
| M7 Capstone | 75 | 10 / 65 | 10 | 13 |
| M8 Security recap & plan | 45 | 20 / 25 | 20 | 5 |
The split is a first draft; the orchestrator can adjust it but must keep the totals honest.
