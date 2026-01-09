# Multi-Cloud Secure Solutions Architect AI Agent  
*(Azure + AWS for DoD and National Security)*

This repository defines and supports a **Multi-Cloud Secure Solutions Architect AI Agent** that helps U.S. Department of Defense (DoD) and national-security organizations design, compare, and migrate workloads across **Microsoft Azure** and **Amazon Web Services (AWS)**.

The agent focuses on:

- DoD Cloud Computing SRG (IL2–IL6)  
- FedRAMP Moderate/High  
- NIST SP 800-53 Rev 5 and NIST SP 800-171 Rev 2  
- DoD Zero Trust Strategy and CISA Zero Trust Maturity Model  
- Azure Government, AWS GovCloud, and hybrid/on-premise environments  

---

## Repository Layout

```text
.
├── README.md
├── docs/
│   ├── multicloud-secure-architect-agent.md
│   ├── gpt-builder-system-prompt.md
│   └── CHANGELOG.md                (optional)
├── prompts/
│   ├── system/
│   │   └── multicloud-architect-system.txt
│   ├── user/
│   │   ├── discovery-workshop-user-prompt.md
│   │   ├── migration-planning-user-prompt.md
│   │   └── security-architecture-user-prompt.md
│   └── examples/
│       └── sample-conversations.md
├── iac-samples/
│   ├── azure/
│   │   ├── landing-zone/
│   │   │   ├── bicep/
│   │   │   └── terraform/
│   │   └── security-baseline/
│   ├── aws/
│   │   ├── landing-zone/
│   │   │   ├── cloudformation/
│   │   │   └── terraform/
│   │   └── security-baseline/
│   └── shared/
│       ├── policies/
│       └── pipelines/
└── diagrams/
    ├── drawio/
    └── exports/

```

You can adjust folder names to match your existing conventions, but this layout is designed to:

- Keep design and documentation in /docs
- Keep prompt artifacts cleanly separated in /prompts
- Keep IaC examples in /iac-samples
- Keep architectural diagrams in /diagrams

---

## Key Files

'/docs/multicloud-secure-architect-agent.md'

Primary design specification for the AI agent:

- Role and scope
- Knowledge domains (Azure, AWS, compliance, Zero Trust)
- Architecture comparison framework
- Migration & 6 Rs framework
- Mission-aligned prioritization framework
- Output and deliverable standards
- Conversation flow and activation protocol

This is the source of truth for how the agent should behave and what it should produce.

---

'/docs/gpt-builder-system-prompt.md'

System prompt text optimized for GPT Builder (or equivalent tools).

Recommended usage:

- Copy the full contents into the “System Instructions” or “What should this GPT do?” field.
- Use the user prompts from /prompts/user as starting points for typical interactions (e.g., discovery, migration planning, security architecture).

---

/docs/CHANGELOG.md (optional but recommended)

Track changes to:

- DoD SRG alignment
- NIST / FedRAMP mappings
- Azure or AWS guidance that drives updates to the agent’s design
- Prompt refinements and major behavior changes

Suggested entry format:

> ## 2025-11-19
> - Initial import of multicloud-secure-architect-agent design.
> - Added GPT Builder system prompt.
> - Created initial repo structure and README.

---

## Prompts

The '/prompts' folder exists so you can keep prompt engineering artifacts versioned and reviewable.

'/prompts/system/multicloud-architect-system.txt'

- A direct, text-only version of the system instructions used by the agent.
- Should be logically consistent with /docs/multicloud-secure-architect-agent.md and /docs/gpt-builder-system-prompt.md.

You can:

- Use this file for programmatic agents (e.g., API-based)
- Generate language-model config from CI/CD pipelines

---

'/prompts/user'

Contains reusable user prompt templates. Suggested files:

- 'discovery-workshop-user-prompt.md'
  - Used to kick off a requirements and mission discovery workshop.
  - Focused on mission context, classification, connectivity, and existing environments.
- 'migration-planning-user-prompt.md'
  - Used for portfolio analysis and application-by-application migration guidance using the 6 Rs and prioritization scoring.
- 'security-architecture-user-prompt.md'
  - Used to generate Zero Trust architectures, SSP content, and control mappings.

These templates help standardize how different users within your organization invoke the agent.

---

'/prompts/examples/sample-conversations.md'

- Contains curated example conversations that demonstrate:
  - Multi-cloud comparison (Azure vs AWS)
  - Applying the 6 Rs to a legacy portfolio
  - Designing an IL5 landing zone in Azure and AWS
- Useful for onboarding new stakeholders or testing behavior after prompt updates.

---

IaC Samples

The /iac-samples directory is reserved for illustrative Infrastructure-as-Code assets referenced by the agent or used as starting points in solution design.

> These are not meant to be full production templates by default; treat them as reference patterns and expand as needed.

'/iac-samples/azure'
'/landing-zone/bicep' and '/landing-zone/terraform'

- Skeleton implementations of:
- Azure Landing Zone / Mission Landing Zone patterns
- Management groups, policy assignments, logging, and connectivity scaffolding

'/security-baseline'

- Example Azure Policy definitions or initiatives

- Bicep/Terraform for:
  - Log Analytics workspaces
  - Security Center / Defender for Cloud configuration
  - Sentinel workspace setup (if desired)

---

'/iac-samples/aws'
'/landing-zone/cloudformation' and '/landing-zone/terraform'

- Skeleton multi-account setup:
  - AWS Organizations, Control Tower-style layout
  - Guardrails via SCPs and Config rules
  - Centralized logging accounts and security account patterns

'/security-baseline'

- Example:
  - CloudTrail configuration
  - GuardDuty/Security Hub enabling
  - Config rules for core compliance checks

---

'/iac-samples/shared'

- '/policies'
  - Shared OPA/Conftest policies
  - Policy-as-code examples for validation of Terraform/CloudFormation/Bicep

'/pipelines'
- Example CI/CD workflows:
  - Linting
  - Security scanning
  - Static analysis and policy enforcement
- GitHub Actions, Azure DevOps Pipelines, or GitLab CI templates

---

## Diagrams

The /diagrams directory collects architecture visuals.

'/diagrams/drawio'

- Source .drawio files generated from or referenced by the agent.
- Keep one file per major pattern (e.g., il5-azure-landing-zone.drawio, il5-aws-landing-zone.drawio, multi-cloud-hub-spoke.drawio).

'/diagrams/exports'

- Exported PNG/SVG/PDF versions used in:
  - White papers
  - Stakeholder presentations
  - Internal documentation and training

  ---

 ## How to Use This Repo

1. Review the Design
  - Start with /docs/multicloud-secure-architect-agent.md.
  - Confirm alignment with your current DoD SRG, NIST, and internal policy interpretations.
2. Configure the GPT
  - Use /docs/gpt-builder-system-prompt.md in GPT Builder or your LLM orchestration platform as system instructions.
  - Optionally, load /prompts/system/multicloud-architect-system.txt for API-driven agents.
3. Standardize Interactions
  - Use the user prompt templates under /prompts/user for repeatable workflows:
    - Discovery workshops
    - Migration portfolio analysis
    - Security and Zero Trust reviews
4. Extend IaC and Policies
  - Use /iac-samples as a seed for organization-specific IaC libraries.
  - Align IaC samples with your preferred CI/CD pipelines, scanning tools, and policy gates.
5. Maintain and Evolve
  - Log significant design and prompt updates in /docs/CHANGELOG.md.
  - When cloud providers or DoD guidance changes, update:
    - Design spec
    - System prompt
    - Any IaC or policy references that are impacted

---

## Contribution Guidelines

- Issues: Use GitHub Issues to track:
  - Design gaps
  - New DoD/Cloud SRG or NIST requirements
  - Needed IaC examples or patterns
- Pull Requests:
  - Keep changes small and focused (e.g., “Add IL6 AWS GovCloud landing zone sketch”).
  - Update /docs/CHANGELOG.md for material changes to behavior or scope.
- Reviews:
  - Ensure at least one cloud security/architecture SME reviews significant changes.
  - Validate proposals against cloud provider documentation and DoD/NIST guidance.

  ---

 ## Next Steps

- Populate the initial prompts under /prompts.
- Add minimal IaC samples to /iac-samples to align with the patterns the agent will recommend.
- Add your own organization-specific guidance layered on top of this baseline (e.g., naming standards, tagging, logging destinations, and accreditation workflows).
