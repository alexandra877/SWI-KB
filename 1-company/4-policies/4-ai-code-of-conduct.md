# 4.4. AI Code of Conduct

**Version:** 1.0
**Status:** Approved
**Owner:** alexandra877
**Last reviewed:** 2026-04-22
**Review cadence:** Ongoing — living document updated as AI, tooling, and regulations evolve

---

## Overview

Visma is an AI-forward company. Every employee is expected and encouraged to use AI tools to work better — to move faster, think sharper, and spend less time on repetitive tasks.

This document does not list things you cannot do. It guides Visma companies and colleagues to do the right thing confidently. AI well used also means AI used efficiently — that is good for environmental commitments, not just budgets.

---

## 1. Context — Why This Exists

### The Opportunity

- AI productivity tools make us faster, sharper, and more creative.
- Visma has negotiated group agreements giving every employee access to reviewed tools with a conscious assessment of risks.
- Goal: empower everyone to use AI confidently in daily work.

### The Risks If We Get It Wrong

- Leakage of confidential business information from unreviewed tools or private AI accounts connected to company systems.
- Feeding a competitor or a malicious actor with data.
- Breach of customer contracts.
- Regulatory fines under GDPR, local labour laws, and the EU AI Act.
- Harm to Visma colleagues through uncontrolled monitoring or profiling.
- Damage to stakeholder trust and reputation.

---

## 2. Executive Summary — Key Aspects at a Glance

| Topic | Rule |
|-------|------|
| **Reviewed Tools** | Use only Visma-negotiated group agreement tools. Never connect private AI accounts to company systems. Shadow AI compounds risk. |
| **Customer Production Data** | Do not share customer production data with AI tools unless covered by the customer contract. This will often require listing the AI tool as a sub-processor. |
| **Employee Monitoring** | Using AI to profile, rank, or monitor colleagues is subject to strict legislation. No AI-driven employment decisions without genuine human review. |
| **Meeting Tools** | Assess necessity, choose least invasive format, notify in advance, store responsibly, delete when no longer needed. |
| **Security** | Apply least privilege. Protect API keys, enable 2FA, understand prompt injection risks. Treat AI access as temporary and audit regularly. Report incidents to security@visma.com. |
| **Third-Party Risk** | If you share your Google Drive with a third party, it could gain access to everything in Drive. Always verify whether a tool has been reviewed before connecting. |

---

## 3. All Employees — The Essentials

> We want you to use AI. Just use the right tools, protect the right data, and own your output.

### Use Reviewed Tools Only

- Use Visma-reviewed tools or company-reviewed tools. Never use tools, connectors, or plugins without assessing the risk.
- Never connect private AI accounts (free-tier ChatGPT, personal Claude.ai) to Google Drive, Slack, Gmail, or Jira.
- Need a new tool? Request a review via Employee Support or procurement@visma.com.

### AI Is "Just" Another Tool

- Interacting with AI tools potentially means granting broad access to data. Apply the same scepticism as with any other tool. Does the tool deserve your trust given the data to be shared?
- It is not Visma strategy to centrally manage and monitor all tool usage. We rely on your judgement, based on guidance and shared learnings.

### Verify Before You Use

- AI can produce confident-sounding text that is inaccurate, outdated, or biased.
- You must be able to explain how you used AI in your work.
- Do not use output you do not understand.

### Ethics Do Not Disappear

- If you would not ask a human colleague to do something because it is unethical, do not ask an AI either.
- No technical control replaces good judgement.

### Use AI Efficiently

- AI queries consume energy and water. Before running a task: could a shorter prompt achieve the same result? Does this need a frontier model, or would a lighter one do?
- Avoid re-running large prompts unnecessarily.
- Think twice before generating AI images or video where the task does not genuinely require it.
- See also: Visma's Environmentally Sustainable Use of AI Tools guidelines.

---

## 4. AI-Powered Meeting Tools

AI recording and transcription can drive efficiency — but **not** in sensitive conversations.

- **Appropriate for:** project kick-offs, training, all-hands.
- **Not for:** one-to-ones, performance reviews, disciplinary proceedings, redundancy consultations.

### Protocol

1. **Decide if the meeting should be captured** — not every meeting should be recorded.
2. **Choose the least invasive format** — a summary is more proportionate than a full transcript. Capture what you actually need.
3. **Notify participants in advance** — include a clear notice in the meeting invitation that recording or AI functionality will be used.
4. **Confirm at the start** — if any participant objects, do not proceed. For all-hands, let objectors turn off camera and mic.
5. **Store output responsibly** — output contains personal data. Store securely, share only with those who need it, delete when no longer required.

> **Note:** Otter.ai and Fireflies are **not** on the Visma reviewed list. Do not connect personal transcription accounts to company meetings.

---

## 5. Care About What You Share With the AI Model

### Connecting to Workspace Tools

When you connect any tool or integration — including AI tools, third-party apps, plugins, or automation services — to workspace tools (Drive, Slack, Gmail) or other company systems, you are giving it access to everything in scope: internal communications, colleague personal data, confidential information, and potentially customer production data.

### Customer Production Data

- Do not include customer production data unless your customer contract explicitly allows it.
- Connecting your whole Drive, Gmail, or Jira counts as sharing customer production data if those tools contain it.
- You often also have to notify customers of AI tool usage.

### Confidential and Sensitive Information

- Do not enter or connect work tools containing trade secrets, unpublished financials, M&A information, or similar into AI tools unless the vendor contract includes a strong confidentiality clause and prohibits use of data for training.
- See the Visma reviewed tools list for guidance.

---

## 6. Claude and Similar Tools

Claude Enterprise and Team plans (not consumer plans such as Max, Pro) provide sufficient safeguards in terms of legal and security standards, and give Visma the right to commercial usage of Claude output.

Before your company allows connections between Google Workspace and third parties such as Claude:

1. Use a licence plan that protects the data you have access to.
2. Prefer tools and price plans reviewed by Visma to ensure legal and security standards are met.
3. Limit the tool's access to data to the extent necessary to perform the task. Do not connect private AI accounts to company systems.
4. Be curious but also sceptical about connectors and plugins. Treat AI access like any new supplier relationship — start with minimum scope and expand only when trust is established.
5. If you have questions about AI tools, start internally with your IT department, local service owner, security contact, and DPM. For further escalation: group legal, IT, or security.

---

## 7. Security Foundational Principles — Manage Permissions

### Apply Minimum Necessary Access

| Permission Level | What AI Can Do | Guidance |
|-----------------|----------------|----------|
| **Read / View** | See and summarise files | Prefer this — safest option for most tasks. Always select specific folders or individual files. |
| **Write / Edit** | Change content or create new files | Only grant if you need AI to draft documents directly in your Drive. |
| **Manage / Delete** | Organise folders or permanently trash files | Avoid unless strictly necessary. |

### Protect Credentials and Access

- Revoke AI access after each project ends.
- Perform periodic security checks and remove apps you are no longer using (Google Drive: `myaccount.google.com/permissions → Third-party apps → Remove Access`).
- Manage API keys, tokens, or service account credentials appropriately.
- Report any suspected data breach or unintended data exposure to security@visma.com without delay.

---

## 8. Finance and M&A

### The Value

- AI can accelerate financial modelling, reporting, and analysis.
- Summarising large data sets or regulatory documents saves hours.
- Automating routine reconciliation tasks frees your team for higher-value work.

### Specific Obligations

- **Never** enter unpublished financials, M&A information, or trade secrets unless the vendor contract prohibits use for own training purposes and has sufficient confidentiality clauses.
- Finance and M&A data should only be processed in tools reviewed by Visma (e.g. Claude Enterprise, Gemini).
- See the AI Governance Portal for advice on use cases and how to request advice on new ones.

---

## 9. HR and People Operations

### No AI Monitoring or Tracking

Employee monitoring is heavily regulated under GDPR, the EU AI Act, and local employment law.

| Permitted | Not Permitted |
|-----------|---------------|
| Analysis based on aggregated data (similar to Peakon) | Letting AI make decisions about sick leave, salary, warnings, working hours, promotions, hiring, or dismissal without a documented, meaningful human decision |
| | Connecting AI agents to Slack, Drive, or email for the purpose of monitoring employee behaviour, profiling activity patterns, or communication frequency |

Guidelines on what constitutes lawful vs. unlawful analysis are in progress and will be communicated in alignment with People.

---

## 10. Responsible AI and Sustainability

> The transformative power of AI is a key driver of innovation. A comprehensive approach to AI — taking environmental, social, and ethical impacts into consideration — is the foundation for continued innovation and adoption.

### Core Principles

- **Verify output accuracy and accountability:** Always cross-check AI output, and never use results you do not understand or cannot explain, especially if results do not refer to credible sources.
- **Drive environmental efficiency:** Practice sustainable and efficient use and development of AI systems by providing full context in prompts and using the right-sized, most efficient AI tool. See Visma's Environmentally Sustainable Use of AI Tools guidelines.
- **Mitigate biases:** Identify and mitigate biases in AI models and underlying data to ensure all individuals are treated justly and in line with Visma's Code of Conduct.

---

## 11. Developers and Product Teams

### AI in Your Products — What Good Looks Like

- All AI-generated code is included in the CI/CD pipeline with SAST/SCA tools and is enrolled in the Visma Security Program.
- All systems are designed, developed, and deployed according to Privacy and Security by Design principles.
- Specific security risks in generative AI systems must be considered before experimenting with customer or personal datasets, and especially before deploying to production.

| Requirement | Detail |
|-------------|--------|
| **Testing** | Ensure AI functionalities are properly tested. Use the offensive playbook and contact your company CISO for red teaming. |
| **Threat modelling** | Follow Visma Defensive Playbook and SSA AI questions. High-impact actions (e.g. bulk payroll deletes) must be protected by Human-in-the-Loop. |
| **Registering initiatives** | All strategic AI initiatives must be added to the AI Product Initiatives Mapping (AIPM) in Hubble. |
| **Legal & regulatory compliance** | Each strategic AI initiative requires a Legal AI Assessment. |
| **Transparency** | AI systems must identify themselves to customers. Any chatbot, voice agent, or automated response system discloses it is an AI before the customer provides any sensitive information. |
| **Environmental footprint** | Use the most efficient AI model that meets your quality bar. For high-volume AI calls, treat model efficiency as a design criterion alongside latency and cost. |

### AI in Your Daily Workflow

1. AI-generated code must meet the same security standard as human-written code.
2. Do not give AI agents write access to production.
3. AI coding assistants (GitHub Copilot, Claude Code, Cursor, etc.) can see your project files, configuration, terminal history, and anything else in scope. Be careful.
4. Be careful when letting AI control your browser. Use a separate browser profile, or log out of sensitive services before starting a browser agent session.
5. Keep secrets out of AI context. Use `.claudeignore`, `.cursorignore`, or equivalent mechanisms to exclude sensitive files.
6. Use synthetic or anonymized data for AI-assisted debugging.
7. Do not use personal AI coding accounts for work on Visma repositories.

### Competition Law — Customer Data-Based Services

Visma controls large amounts of customer data in accounting, tax, invoicing, HR, and payments, with significant market share in several regions.

Building AI services that aggregate non-public customer data (e.g. a "Virtual CFO" or benchmarking services) creates competition law risk, particularly in markets where Visma has a near-dominant position.

**Visma Legal & Compliance recommends:**

- Use publicly available data (e.g. scraping public sources or expert literature) for training AI.
- When offering AI expert products, use only the individual customer's own data in combination with AI training from public/expert sources.
- If using aggregated customer data for training AI experts, the service must not offer any regional or segment-based granularity.

Every Visma legal unit should consult the Visma Legal & Compliance department before building AI products and services that may touch on competition law.

> Questions? Contact Erich Nøling at erich.nokling@visma.com.

---

## 12. Compliance, Legal and DPMs

### Key Responsibilities

**Vendor and tool governance:**
- Every AI tool should be subject to a review. Check group agreements. Identify additional local AI vendors.
- Verify data processing agreements are in place.
- Flag tools transferring data outside the EU, including Claude, and assess against customer contracts and GDPR sub-processor obligations.
- Understand the Claude tier differences: Enterprise and Team vs. consumer plans (Max, Pro).

**Employee monitoring:**
- Ensure formal risk assessments and employee representative consultations before AI touches HR processes.
- Monitor for scope creep (e.g. Slack AI reports drifting into monitoring territory).
- Ensure compliance with the EU AI Act principles on dignity, discrimination, and respect.

**Ongoing audit and response:**
- Assist in implementing AI guidelines and policies.
- First responder for incidents — report to security@visma.com without delay.
- Track regulatory landscape: GDPR, EU AI Act, and local law.
- Reference VSP AI Playbooks (Defensive v1.0, Offensive v1.0).
- Assist product teams in completing the Legal AI Assessment before deploying to production.

---

## 13. Senior Management and MDs

### Your Role as a Manager

| Responsibility | Detail |
|----------------|--------|
| **Set the culture** | Make AI adoption a positive expectation, not a feared obligation. Teams should feel empowered to use AI — and equally empowered to ask questions when unsure. |
| **Enforce the guardrails** | Ensure every team knows their specific obligations. Managers, HR, finance, and developers each carry additional responsibilities. Ignorance is not a defence. |
| **Stay ahead** | This is a living document. GDPR enforcement is intensifying, the EU AI Act is taking effect, and hackers are exploiting the time it takes for companies to adjust. Competitive advantage comes from being early and correct. |

### Key Actions for Team Leads, Management, and MDs

1. **Bring awareness of the AI Governance Portal** — ensure employees know it exists and where to find it.
2. **Ensure product and development teams are aware** of the requirement to register strategic AI initiatives in Hubble, and of the legal assessments and security testing available before deploying AI features to production.
3. **Acknowledge the environmental impacts** — ask your teams whether they are using the most efficient model for the task. Push back on vendors for better transparency.
4. **Gain overview and make conscious decisions** — review and actively determine which AI tools and connectors are permitted in your company.
5. **Learning to swim rather than closing the pool** — Visma's strategy is not to monitor and approve all AI tool usage. We help companies make decisions and trust colleagues to take ownership of their AI strategy, including the risk side.
6. **Clarify your Claude tier** — know whether your company is on Enterprise, Team, or consumer plans. Enterprise and Team are vetted; consumer plans (Max, Pro) allow Anthropic to use your data and prohibit commercial usage of output.

---

## References and Contacts

| Resource | Link / Contact |
|----------|---------------|
| Full text version | AI Code of Conduct (Visma Space) |
| AI Governance Portal | AI Governance Portal (WIP) |
| Security incidents | security@visma.com |
| Group compliance contact | Available in VOM |
| Competition law questions | erich.nokling@visma.com |
| New AI tool requests | procurement@visma.com |
| Responsible AI Page | Visma intranet |

---

*Source: AI Code of Conduct v1.0 presentation, April 2026 | Extracted and structured for KB: 2026-04-22*
