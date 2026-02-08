Below is an **operator training table** you can drop directly into **Confluence** under the Quick-Start Guide.
It is intentionally blunt. This is how you **train behavior** and reduce rework.

---

# DoD Zero Trust GPT — Bad Prompt Training Table

## Purpose

This table shows **common operator mistakes**, how the GPT will respond, and how to fix the input so work can proceed.

Use this in onboarding and refresh training.

---

## ❌ Bad Prompts vs ✅ Corrected Prompts

| ❌ Bad Prompt                                              | GPT Response (Expected)                                             | Why It Fails                            | ✅ Correct Prompt                                                                                                             |
| --------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| “Can you help us think about Zero Trust?”                 | **MISALIGNED** — The request is undefined and not actionable.       | No scope, no COA reference, no outcome. | “Start a new DoD Zero Trust engagement. Assess current state against COA1 Target objectives.”                                |
| “Are we mostly Zero Trust?”                               | **VAGUE / UNSUPPORTED** — No measurable criteria or evidence.       | “Mostly” is meaningless under COA.      | “Assess our current maturity against COA1. Identify capabilities below Target.”                                              |
| “What tools should we buy?”                               | **MISALIGNED** — Tool acquisition is not justified without gaps.    | Skips assessment and remediation logic. | “Identify capability gaps that cannot be met with existing tools and justify any required new capabilities.”                 |
| “We already have MFA everywhere, so User pillar is done.” | **INFLATED** — MFA alone does not satisfy User pillar capabilities. | Capability coverage ≠ single control.   | “Assess User pillar capabilities. Validate MFA enforcement, attribute quality, and PDP integration with evidence.”           |
| “Let’s just mark this as Target for now.”                 | **NON-COMPLIANT** — Target maturity requires evidence.              | Falsifies compliance posture.           | “List required evidence to support Target maturity for this capability.”                                                     |
| “Skip Device and Network for now.”                        | **MISALIGNED** — Dependencies not addressed.                        | Deferral without risk tracking.         | “Defer Device and Network pillars. Document risks, dependencies, and mitigation timeline.”                                   |
| “We’re using Vendor X’s Zero Trust platform.”             | **IRRELEVANT** — Vendor naming does not establish capability.       | COA evaluates outcomes, not branding.   | “Map existing tools to COA capabilities and identify enforcement gaps.”                                                      |
| “Can you summarize our environment?”                      | **UNSUPPORTED** — No authoritative inputs provided.                 | GPT cannot infer environment.           | “Summarize the current engagement state based on recorded artifacts and evidence pointers.”                                  |
| “Just give us an executive summary.”                      | **VAGUE** — No reporting scope or timeframe defined.                | Lacks reporting criteria.               | “Generate a quarterly Zero Trust progress report showing pillar and capability advancement, risks, and compliance forecast.” |
| “We need to move faster—don’t ask so many questions.”     | **NON-COMPLIANT** — Missing inputs block defensible assessment.     | Speed without inputs increases risk.    | “Identify minimum required inputs to advance User and Device pillars within 60 days.”                                        |

---

## Operator Rules of Thumb

**If your prompt includes:**

* “think about”
* “mostly”
* “basically”
* “just”
* “for now”

It will likely be rejected.

**If your prompt includes:**

* COA capability IDs
* pillars
* timelines
* evidence
* constraints

It will move forward.

---

## How to Use This Table in Practice

* Include it in **operator onboarding**
* Review before major milestones
* Use it to coach junior staff
* Reference it when the GPT “pushes back”

If the GPT rejects your prompt, **check this table before escalating**.

---
Below is an **operator training table** you can drop directly into **Confluence** under the Quick-Start Guide.
It is intentionally blunt. This is how you **train behavior** and reduce rework.

---

# DoD Zero Trust GPT — Bad Prompt Training Table

## Purpose

This table shows **common operator mistakes**, how the GPT will respond, and how to fix the input so work can proceed.

Use this in onboarding and refresh training.

---

## ❌ Bad Prompts vs ✅ Corrected Prompts

| ❌ Bad Prompt                                              | GPT Response (Expected)                                             | Why It Fails                            | ✅ Correct Prompt                                                                                                             |
| --------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| “Can you help us think about Zero Trust?”                 | **MISALIGNED** — The request is undefined and not actionable.       | No scope, no COA reference, no outcome. | “Start a new DoD Zero Trust engagement. Assess current state against COA1 Target objectives.”                                |
| “Are we mostly Zero Trust?”                               | **VAGUE / UNSUPPORTED** — No measurable criteria or evidence.       | “Mostly” is meaningless under COA.      | “Assess our current maturity against COA1. Identify capabilities below Target.”                                              |
| “What tools should we buy?”                               | **MISALIGNED** — Tool acquisition is not justified without gaps.    | Skips assessment and remediation logic. | “Identify capability gaps that cannot be met with existing tools and justify any required new capabilities.”                 |
| “We already have MFA everywhere, so User pillar is done.” | **INFLATED** — MFA alone does not satisfy User pillar capabilities. | Capability coverage ≠ single control.   | “Assess User pillar capabilities. Validate MFA enforcement, attribute quality, and PDP integration with evidence.”           |
| “Let’s just mark this as Target for now.”                 | **NON-COMPLIANT** — Target maturity requires evidence.              | Falsifies compliance posture.           | “List required evidence to support Target maturity for this capability.”                                                     |
| “Skip Device and Network for now.”                        | **MISALIGNED** — Dependencies not addressed.                        | Deferral without risk tracking.         | “Defer Device and Network pillars. Document risks, dependencies, and mitigation timeline.”                                   |
| “We’re using Vendor X’s Zero Trust platform.”             | **IRRELEVANT** — Vendor naming does not establish capability.       | COA evaluates outcomes, not branding.   | “Map existing tools to COA capabilities and identify enforcement gaps.”                                                      |
| “Can you summarize our environment?”                      | **UNSUPPORTED** — No authoritative inputs provided.                 | GPT cannot infer environment.           | “Summarize the current engagement state based on recorded artifacts and evidence pointers.”                                  |
| “Just give us an executive summary.”                      | **VAGUE** — No reporting scope or timeframe defined.                | Lacks reporting criteria.               | “Generate a quarterly Zero Trust progress report showing pillar and capability advancement, risks, and compliance forecast.” |
| “We need to move faster—don’t ask so many questions.”     | **NON-COMPLIANT** — Missing inputs block defensible assessment.     | Speed without inputs increases risk.    | “Identify minimum required inputs to advance User and Device pillars within 60 days.”                                        |

---

## Operator Rules of Thumb

**If your prompt includes:**

* “think about”
* “mostly”
* “basically”
* “just”
* “for now”

It will likely be rejected.

**If your prompt includes:**

* COA capability IDs
* pillars
* timelines
* evidence
* constraints

It will move forward.

---

## How to Use This Table in Practice

* Include it in **operator onboarding**
* Review before major milestones
* Use it to coach junior staff
* Reference it when the GPT “pushes back”

If the GPT rejects your prompt, **check this table before escalating**.

---
Below is a **Jira / Confluence Usage Addendum** designed to bolt cleanly onto the **Operator Quick-Start Guide**.

This is written for **execution discipline**, auditability, and multi-team consistency.
No fluff. No “how Jira works” basics.

---

# DoD Zero Trust GPT

## Jira & Confluence Usage Addendum

### Purpose

This addendum defines **how the GPT is to be used with Jira and Confluence** during DoD Zero Trust (ZT) engagements to ensure:

* Traceability to COA capabilities
* Accurate execution tracking
* Audit-ready documentation
* Controlled handling of CUI and sensitive data

Jira and Confluence are **systems of execution and record**, not brainstorming spaces.

---

## 1. Jira Usage Model

### Jira Is Used For

* Executing approved remediation work
* Tracking progress at **capability level**
* Recording status, blockers, and risk
* Supporting reporting and oversight

### Jira Is NOT Used For

* Storing raw evidence (logs, screenshots, exports)
* Narrative assessments
* Vendor marketing material
* Informal design discussions

---

### 1.1 Required Jira Hierarchy

**MANDATORY STRUCTURE**

```
Epic
  └── ZT Pillar (or Pillar Group)

Story
  └── COA Capability Remediation

Task / Sub-task
  └── Discrete technical, policy, or integration action
```

**Example**

```
Epic: ZT – User & ICAM Pillar
Story: USER-3 – Privileged Access Enforcement
Task: Enforce MFA + device compliance for privileged roles
Task: Integrate PAM telemetry into SIEM
```

Do not create Jira items without a COA capability reference.

---

### 1.2 Required Fields (Per Story)

Each **Story** MUST include:

* **COA Capability ID**
* **Current Maturity** (NONE / PARTIAL / TARGET / ADVANCED)
* **Target Maturity**
* **Evidence Pointer ID(s)**
  (Links or IDs referencing GCC High SharePoint or approved evidence systems)
* **Acceptance Criteria** (objective, testable)
* **Dependencies** (other capabilities or systems)
* **Risk if Deferred**

If any field is missing, the GPT will treat the work as **UNSUPPORTED**.

---

### 1.3 Status Updates and Comments

When updating Jira:

* Comments must be **factual and outcome-oriented**
* No speculation or optimism language
* No sensitive data

**Acceptable**

> “Conditional Access policy enforced for privileged roles. Sign-in logs confirm MFA and device compliance. Evidence pointer EV-USER-003 updated.”

**Unacceptable**

> “Looks good.”
> “We think this is done.”
> “Vendor says this covers it.”

---

### 1.4 GPT Interaction with Jira

When enabled, the GPT may:

* Draft Jira stories/tasks
* Update descriptions and acceptance criteria
* Add status comments
* Propose transitions (e.g., In Progress → Blocked)

The GPT will **not**:

* Close issues without acceptance criteria met
* Remove risk or dependency fields
* Mask incomplete work

---

## 2. Confluence Usage Model

### Confluence Is Used For

* Authoritative documentation
* Assessment artifacts
* Roadmaps and reports
* Architecture and policy narratives

### Confluence Is NOT Used For

* Raw evidence storage
* Draft notes
* Chat transcripts
* Working scratchpads

---

### 2.1 Required Confluence Artifacts

At minimum, each engagement must maintain:

* Zero Trust Assessment Summary
* Pillar-by-Pillar Capability Matrix
* Gap Register
* Phased Remediation Roadmap
* Periodic Progress Reports
* Decision Log (architectural and risk decisions)

These are **living documents**, updated as the engagement progresses.

---

### 2.2 Content Rules

All Confluence content must be:

* COA-aligned
* Capability-specific
* Evidence-referenced (by pointer)
* Sanitized for audience and classification

**Do not embed:**

* Screenshots of logs
* Config exports
* IP addresses, usernames, tenant IDs
* CUI unless the space is explicitly approved

---

### 2.3 GPT Interaction with Confluence

When enabled, the GPT may:

* Generate or update pages using approved templates
* Insert assessment results and status tables
* Update progress reports and roadmaps

The GPT will:

* Flag missing evidence
* Refuse to assert compliance without support
* Preserve prior approved content unless directed otherwise

---

## 3. Evidence Handling (Critical)

### Evidence Location

* **Authoritative evidence lives outside Jira/Confluence**
* Preferred system: **GCC High SharePoint**

### What Jira/Confluence May Contain

* Evidence **pointers**
* Evidence **summaries**
* Classification labels

### What They Must NOT Contain

* Raw logs
* Screenshots
* Exports
* Sensitive identifiers

Violation of this rule is a **process failure**, not a tooling issue.

---

## 4. Reporting and Oversight

### Periodic Reports (Monthly / Quarterly)

Generated via Confluence and supported by Jira data.

Reports must include:

* Pillar-level maturity changes
* Capability-level advancement
* Deferred work and associated risk
* Blockers and dependencies
* Forecast against COA Target timelines

The GPT will refuse to generate reports that:

* Omit deferred risk
* Use narrative-only claims
* Conflict with Jira execution data

---

## 5. Common Failure Modes (Avoid These)

* Creating Jira tasks without COA references
* Marking stories “Done” without evidence pointers
* Using Confluence as a dumping ground
* Treating Jira status as proof of compliance
* Allowing vendors to define completion criteria

The GPT is designed to detect and challenge these behaviors.

---

## Bottom Line

* **Jira = execution and tracking**
* **Confluence = authoritative narrative**
* **SharePoint = evidence**
* **GPT = enforcement and coherence**

If these roles blur, compliance collapses.

---

### Optional Next Artifacts

If useful, I can also generate:

* Jira issue templates (JSON / YAML)
* Confluence page templates (ready to import)
* A reporting dashboard schema
* A RACI model for ZT execution across teams

Say which one.
