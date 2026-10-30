# Spec · M2 Prototype Gallery (vote)

- **Purpose:** practise Prompt Pattern 3 *Prototype first*: compare 3 slide styles built from the same synthetic data before Claude builds the full deck (Workshop A).
- **Users:** whole room; trainer shows the result before the "Build" step.
- **Content:** 3 sample slides — 1 Executive · 2 Visual · 3 Detailed (Budget vs Actual 2568, synthetic sites) with pros/cons.
- **Interactions:** vote for one style, write a reason (≤140 chars), live bar chart of votes and latest reasons.
- **Storage:** uses shared Artifact storage (`window.storage`) when the host provides it, so votes aggregate across the room (label "ผลโหวตรวมทั้งห้อง"); otherwise falls back to this browser only ("เฉพาะเครื่องนี้") — then the trainer counts by show of hands. Shared storage needs company Claude accounts for viewers (PLAN.md checks).
- **Engagement mechanic:** live vote + reasons wall.
- **Export PDF:** prints the 3 styles with the final vote counts.
- **AI calls:** none.
