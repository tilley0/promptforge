# GovRFP Agentic Proposal System

This repository supports a structured, collaboration-ready approach to responding
to U.S. Government RFQs and RFPs using two complementary Custom GPTs and a
repo-backed Proposal Pack.

The system is designed to:
- Enforce elimination-grade compliance
- Enable multi-author collaboration
- Support teaming and partner evaluation
- Prevent common proposal failure modes
- Maintain continuity across days and contributors

---

## System Components

### 1) GovRFP-Collab-Strategist (Core GPT)
**Purpose:** Execution

Use this GPT for:
- Analyzing RFQs/RFPs
- Drafting and rewriting proposal content
- Compliance checks
- Evaluation-factor alignment
- Teaming strategy recommendations
- Kill Shot reviews
- Time-boxed rewrites

This GPT assumes you are actively producing proposal content.

---

### 2) GovRFP-ProposalOps (Companion GPT)
**Purpose:** Governance and workflow

Use this GPT for:
- Setting up a new opportunity
- Defining workflow, roles, and cadence
- Managing collaboration discipline
- Running Red Team reviews
- Enforcing artifact requirements
- Interpreting Proposal Pack structure

This GPT governs *how* the proposal is run.

---

## Authoritative Source of Truth

- The **git repository** is authoritative.
- ChatGPT memory is not.
- Knowledge files are reference-only.

### Anchor File
- `proposal/<SOLICITATION_ID>/STATE.yaml`

If it is not reflected in the repo artifacts, it is not real.

---

## Proposal Pack Structure (High Level)

proposal/<SOLICITATION_ID>/
STATE.yaml
DECISIONS.md
ASSUMPTIONS.md
RISK_REGISTER.md
CURRENT_DRAFT_POINTERS.md
01_sol/
02_compliance/
03_solution/
04_teaming/
05_pastperf/
06_volumes/
07_reviews/


---

## Required Artifacts (Enforced via CI)

Mandatory:
- STATE.yaml
- Compliance Matrix (md OR xlsx OR csv)
- Evaluation Factors
- Solicitation Files Manifest
- Decision / Assumption / Risk logs

Either/Or logic is enforced by CI lint.

---

## Recommended Workflow

1. GO / NO-GO decision
2. Compliance inventory
3. Evaluation factor mapping
4. Gap analysis + teaming strategy
5. Draft volumes
6. Red Team review
7. Kill Shot review
8. Time-boxed rewrite
9. Final compliance + realism check

Skipping steps increases elimination risk.

---

## Discipline Rules

- Compliance failures stop work immediately
- Claims require evidence
- Partner roles must be defensible
- Price realism must align with the solution
- Decisions are logged and locked

This system exists to enforce those rules.

---

## Getting Started

1. Create a new opportunity using `scripts/new-opportunity.sh`
2. Populate STATE.yaml
3. Load required artifacts into the Core GPT
4. Follow the workflow

If unsure where to start, use **GovRFP-ProposalOps** first.
