# Acme — BrAIn.D dogfooding itself

This repo is the BrAIn.D workspace for **Acme**, a stand-in for BrAIn.D's own company. The CEO sets
KPIs and outcome contracts here, and BrAIn.D's own feature work is tracked here as work under those
contracts. The repo is public on purpose (build in public): never put real revenue, runway, customer
names or credentials here — Acme figures are illustrative.

## Vision

BrAIn.D is the singularity for the enterprise: the universal knowledge base and knowledge graph, and
the go-to tool to find anything and get answers to anything about the organization — what it intends,
what it invests, what humans and AI agents do, what evidence emerges, and what outcomes actually occur.

## Current wedge (what we build now)

The vision is the direction; **outcome accountability** is the MVP. Anything outside it waits until
after the root objective's window.

- **Root objective:** 3 C-level design partners each maintain 5 live outcome contracts and open the
  exec view weekly for 4 consecutive weeks, by 2026-12-31.
- **BrAIn.D owns** outcome achievement (actual vs target) and outcome-linked execution (work progress
  vs outcome progress). It never computes business KPIs such as revenue or NRR — it references their
  source of truth and stores snapshots.
- **Deferred:** opportunity discovery (beyond an orphan-problem check), connectors, autonomous agents.

## Outcome contracts

A contract has a human owner, metric, metric source, baseline, target, deadline, investment (FTE or $),
and a measurement cadence. It is **live** in a given week only if all four hold:

1. **Complete** — every field above is set.
2. **Measured** — the actual was updated with provenance (link, screenshot or CSV) within 7 days, or
   within 30 days for monthly metrics.
3. **Seen** — a director or above viewed it that week (logged by the exec view).
4. **Linked to work** — at least one work item hangs under it.

Cadence is set at creation from the metric source (monthly only if the source publishes monthly). Only
the approver one level up the node tree may change it later, as a dated decision.

In v1, actuals are entered manually with provenance required; an agent may pre-fill a value for the
owner to confirm.

## Work items

BrAIn.D is the source of truth for work structure: every work item is a BrAIn.D node, either
**native** (tracked fully in BrAIn.D) or **linked** (pointing to an external tracker such as a Jira
epic or issue). BrAIn.D is authoritative for the item's existence, parent contract, owner, status
rollup and decisions; a linked item's detailed content stays in the external system.

- Every feature or work item sits under the outcome contract it is meant to move. One without a parent
  contract is flagged as **orphan work**.
- Work progress comes from item status (open → in-progress → shipped) for native items, and is
  self-reported at each update for linked items in v1.
- Shipped is not done: work counts toward the outcome only through the contract's actual.
- Acme uses native items throughout. BrAIn.D source code lives in the private `braind-enterprise` repo;
  feature nodes link their PRs.

## Milestones

Built by Pradeep plus coding agents. Selling runs in parallel from now, demoing Acme itself.

| Date | Milestone |
|---|---|
| 2026-10-16 | Contract schema (including the work-item node, native or Jira-linked), provenance updates and live-status computation shipped |
| 2026-10-23 | Exec view with view logging shipped; Acme runs 5 live contracts on itself |
| 2026-10-23 → 11-06 | Acme dogfood; fix pain points before partners see it |
| 2026-10-31 | 3 design partners signed, plus 1–2 backups |
| 2026-11-13 | All partners onboarded with 5 contracts each |
| 2026-11-16 → 12-13 | The 4-week window (slack until 2026-12-31) |
