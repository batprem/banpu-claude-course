# M3 · Setup notes for IT (test tenant) — synthetic data only

Goal: a safe sandbox so learners never practise on real mailboxes or shared files. Everything in `pack/` is fictional (`@example.com`, fictional sites).

## What to prepare (≥ 3 working days before training)
1. **Claude Team org:** an Owner enables the Microsoft 365 connector; an Entra **Global Administrator** grants the one-time consent (see Help Center "Set up the Microsoft 365 connector", SOURCES #1). Keep **write tools off** for the training cohort — the workshop is read-only; edits happen on local copies in Cowork.
2. **Test accounts:** one test account per learner (or per pair), e.g. `m3.learner01@<test-domain>`, licensed for Outlook + SharePoint.
3. **Test mailbox content:** import the 20 emails from `pack/outlook/*.eml` (or `mailbox_index.csv`) into each test mailbox (or one shared test mailbox all learners can open — the connector can search shared mailboxes the user can open).
4. **SharePoint site `M3-Training`:** upload `Project_Tracker.csv`, `Issue_Log.csv` (optionally also create them as SharePoint Lists from the CSVs) and `Shared_Capex_Tracker_2569.xlsx`. Turn on **Version history** for the library.
5. **Scope warning:** the connector searches **all** SharePoint content the account can access (site-specific restriction isn't supported). Test accounts must have access to `M3-Training` only — no real company sites.
6. **Restrict who can authenticate** (optional): Entra admin center → the Claude M365 enterprise application → *Assignment required = Yes* → assign the test accounts.

## Fallback (no test tenant)
Distribute `M3_SamplePack.zip` = the `pack/` folder (outlook/ + sharepoint/). Learners use Cowork on that folder with prompt M3-P08. No IT setup needed.

## Regenerate
`python3 materials/m3/data/gen_m3_data.py` (deterministic, seed 303).
