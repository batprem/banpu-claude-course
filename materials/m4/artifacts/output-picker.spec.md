# Spec · Output Picker (Artifact)

File: `output-picker.html` · Owner: M4 · Used in: slide 11 (quick quiz), workshop page 5 step 2

## Purpose
Practise the decision "Word / Excel / PDF / PowerPoint or Artifact?" and the bonus decision "report too big to attach: shrink, split or summary + SharePoint link?". Covers requirement 11 (when to use Office formats instead of an Artifact) and 7 (workarounds).

## Users
Learners on laptops, solo, ~90 seconds in the lecture or 1 minute at the end of the workshop. Trainer can project it and let the room vote.

## Interactions
1. 10 fictional scenarios in fixed order: 8 format questions (5 buttons) + 2 bonus "too big" questions (3 buttons).
2. One click per question, locked after answering; instant feedback with the reason. Two questions accept an alternative answer (App: Artifact or Excel; Diagram: Artifact or PDF).
3. HUD: question x/10, score, streak, progress bar.
4. Result: badge (≥ 9 🏆 Output Architect, ≥ 7 🥈 Report Builder, else 🛠️ ฝึกอีกนิด), best streak, table of every answer with reason, replay.

## Export PDF
Header button (`materials/_shared/export-pdf.html`). Print hides the game card and shows the rule box plus the result table (if finished).

## Data
Scenarios live in the `Q` array in the HTML. All people and situations are fictional; no Banpu data.

## Engagement mechanic
Quick-fire quiz + streak + badge, with the reasons in the PDF as a take-home cheat sheet.

## Constraints
Self-contained (Google Fonts only), no network/AI calls, no storage, STYLE.md colours, responsive (2 columns of buttons on phones).
