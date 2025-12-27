---
id: 1
title: Create Initial Constitution
stage: constitution
date: 2025-12-27
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: Claude Code
command: /sp.constitution
labels: [constitution, spec-driven-development, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

```text
Project: Hackathon II — The Evolution of Todo (Spec-Driven, AI-Native, Cloud-Native Todo → Chatbot → Kubernetes → Event-Driven)

Core principles:

Spec-Driven Development Only: Implementation hamesha specs se drive hogi; spec = single source of truth.

No Manual Coding: Engineer ka role "system architect" hai; code directly type nahi karna—sirf spec refine karni hai jab tak Claude Code correct output generate na kare.

Traceability: Har feature aur change ka link specs (constitution/spec/plan/tasks) se hona لازمی hai.

Iterative Evolution: CLI → Full-stack → AI chatbot → Local K8s → Cloud/event-driven; har phase previous phase ki continuity maintain kare.

Security & User Isolation First: Multi-user system mein har request authenticated + authorized ho; data isolation non-negotiable hai.

Cloud-Native by Design: Containers, Helm, Kubernetes readiness, stateless services, config via env/secrets, portability.

Testability & Reliability: Acceptance criteria pass, regression-safe, predictable behavior; errors graceful hon.

Key standards:

Constitution hierarchy: Constitution > Specify > Plan > Tasks > Implement.

Spec artifacts required: Har phase/feature ke liye:

Markdown Constitution (yeh file)

Feature specs (WHAT + acceptance criteria)

Plan (HOW/architecture)

Tasks (atomic, testable units)

Specs history maintained (spec revisions versioned)

"No task = no code": Claude Code sirf us task ko implement kare jo speckit.tasks mein present ho.

Code referencing standard (mandatory in PRs/commits or file headers/comments):

[From]: spec §X.Y + plan §A.B

Repository structure standard (monorepo preferred):

/.spec-kit/config.yaml

/specs/** (overview, features, api, database, ui, mcp)

/frontend (Next.js)

/backend (FastAPI)

CLAUDE.md (root) forwarding to AGENTS.md

AGENTS.md (agent behavior rules)

specs-history/ (or /specs/history) for iteration trail

Documentation standard (required deliverables):

README: setup + run + deploy + demo steps

CLAUDE.md: how to run Claude Code in this repo (root + frontend + backend if needed)

Explicit env var list and examples (.env.example)

Constraints (Non-Negotiables):

Phase completion order: Phase I → II → III → IV → V (skip allowed nahi).

Stack constraints:

Phase I: Python 3.13+, UV, console app, in-memory

Phase II: Next.js (App Router), FastAPI, SQLModel, Neon Postgres, Better Auth (JWT)

Phase III: OpenAI ChatKit UI, OpenAI Agents SDK, Official MCP SDK, stateless chat endpoint with DB-backed conversation state

Phase IV: Docker, Minikube, Helm, kubectl-ai and/or kagent (plus Gordon if available)

Phase V: Kafka + Dapr, cloud Kubernetes (DigitalOcean DOKS as primary target per brief), CI/CD, monitoring/logging

Authentication + Authorization (Phase II+):

All API endpoints require valid JWT via Authorization: Bearer <token>

Backend must verify JWT signature with shared secret (BETTER_AUTH_SECRET) and enforce user_id ownership on every operation

Requests without token: 401; mismatched user access: 403

Stateless backend rule (Phase III+):

Chat endpoint and MCP tools must be stateless; conversation/messages persist in DB; server restart must not lose state.

API contract stability:

REST endpoints must follow specified routes and behaviors.

MCP tools must match defined names + params + return shapes (add_task, list_tasks, update_task, delete_task, complete_task).

Deployment constraints:

Phase IV: Must run locally on Minikube with Helm charts

Phase V: Must run on cloud Kubernetes with event-driven architecture (Kafka) and Dapr building blocks

No hidden dependencies:

All secrets via env vars / secret management (K8s Secrets or Dapr secret store)

No hardcoded credentials or URLs in code

Quality gates (Must Pass):

Functional completeness per phase:

Phase I/II/III: Basic Level (Add, Delete, Update, View, Mark complete)

Phase V: Intermediate + Advanced features (Priorities/Tags, Search/Filter/Sort, Due dates/reminders, Recurring tasks)

Acceptance criteria must be explicit in specs and verifiable via tests or demo steps.

Reliability:

Graceful errors: "task not found", invalid input, auth failures

Idempotent behaviors where relevant (e.g., toggling completion)

Security:

User isolation enforced at DB query level (filter by authenticated user id)

JWT verification mandatory

Observability (Phase IV/V):

Clear logs, health checks, readiness probes; basic monitoring hooks.

Portability:

Works in local dev + container + K8s; config via env/secrets; no local-only assumptions.

Success criteria:

All 5 phases implemented using Spec-Driven Development with clear spec history and traceability.

Demonstrable working app at each checkpoint (CLI → Web → Chatbot → Minikube → Cloud).

AI chatbot correctly performs todo operations via MCP tools using natural language and confirms actions.

Deployments are reproducible via documented commands (local and cloud), with Helm charts and environment configuration.

Submission-ready artifacts per phase:

Public GitHub repo link

Vercel deployed frontend link (where required)

Backend
```

## Response snapshot

Created the project constitution file `.specify/memory/constitution.md` with all the specified principles, constraints, and governance rules for the Hackathon II project. The constitution includes:

1. Core principles for spec-driven development, no manual coding, traceability, iterative evolution, security-first approach, and cloud-native design
2. Detailed constraints for each phase of development
3. Quality gates and requirements for each phase
4. Development workflow and documentation standards
5. Success criteria and governance procedures

The constitution follows the template structure but replaces all placeholder tokens with the specific requirements for the Hackathon II project.

## Outcome

- ✅ Impact: Created initial project constitution with comprehensive governance rules
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with project-specific governance
- 🔁 Next prompts: Ready to proceed with feature specification and planning
- 🧠 Reflection: Constitution properly captures all specified requirements and constraints

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification process