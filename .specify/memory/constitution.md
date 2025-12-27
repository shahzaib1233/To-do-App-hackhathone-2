<!--
Sync Impact Report:
Version change: 1.0.0 → 1.0.0 (initial creation)
Added sections: All principles and governance sections
Removed sections: None (initial creation)
Templates requiring updates: ✅ No templates to update (initial creation)
Follow-up TODOs: None
-->
# Hackathon II — The Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development Only
Implementation always driven by specs; spec = single source of truth. All code changes must trace back to specific tasks defined in the spec system. No code implementation without corresponding spec/task definition.

### II. No Manual Coding
Engineer's role is "system architect"; no direct code typing allowed—only spec refinement until Claude Code generates correct output. Human involvement limited to requirements specification, architecture planning, and quality validation.

### III. Traceability
Every feature and change must link to specs (constitution/spec/plan/tasks). Complete audit trail required for all implementations with clear references to originating specifications and design decisions.

### IV. Iterative Evolution
Progress through phases: CLI → Full-stack → AI chatbot → Local K8s → Cloud/event-driven; each phase maintains continuity from previous phase. Sequential progression required—no skipping phases allowed.

### V. Security & User Isolation First
Multi-user system requires authenticated + authorized requests; data isolation is non-negotiable. All API endpoints require JWT authentication, user data must be properly isolated at database level.

### VI. Cloud-Native by Design
Architecture must support containers, Helm, Kubernetes readiness, stateless services, configuration via environment/secrets, and portability across environments.

## Constraints (Non-Negotiables)

### Phase Completion Order
Phases must be completed in sequence: Phase I → II → III → IV → V (no skipping allowed). Each phase has specific stack constraints and functional requirements that must be met before proceeding.

### Stack Constraints
- Phase I: Python 3.13+, UV, console app, in-memory storage
- Phase II: Next.js (App Router), FastAPI, SQLModel, Neon Postgres, Better Auth (JWT)
- Phase III: OpenAI ChatKit UI, OpenAI Agents SDK, Official MCP SDK, stateless chat endpoint with DB-backed conversation state
- Phase IV: Docker, Minikube, Helm, kubectl-ai and/or kagent
- Phase V: Kafka + Dapr, cloud Kubernetes (DigitalOcean DOKS), CI/CD, monitoring/logging

### Authentication + Authorization (Phase II+)
- All API endpoints require valid JWT via Authorization: Bearer <token>
- Backend must verify JWT signature with shared secret (BETTER_AUTH_SECRET) and enforce user_id ownership on every operation
- Requests without token: 401; mismatched user access: 403
- User isolation enforced at DB query level (filter by authenticated user id)

### Stateless Backend Rule (Phase III+)
- Chat endpoint and MCP tools must be stateless
- Conversation/messages persist in DB
- Server restart must not lose state
- MCP tools must match defined names + params + return shapes (add_task, list_tasks, update_task, delete_task, complete_task)

### No Hidden Dependencies
- All secrets via env vars / secret management (K8s Secrets or Dapr secret store)
- No hardcoded credentials or URLs in code
- Configuration via environment variables and secrets only

## Quality Gates (Must Pass)

### Functional Completeness per Phase
- Phase I/II/III: Basic Level (Add, Delete, Update, View, Mark complete)
- Phase V: Intermediate + Advanced features (Priorities/Tags, Search/Filter/Sort, Due dates/reminders, Recurring tasks)
- Acceptance criteria must be explicit in specs and verifiable via tests or demo steps

### Reliability Requirements
- Graceful errors: "task not found", invalid input, auth failures
- Idempotent behaviors where relevant (e.g., toggling completion)
- API contract stability: REST endpoints follow specified routes and behaviors

### Observability (Phase IV/V)
- Clear logs, health checks, readiness probes
- Basic monitoring hooks
- Proper error logging and performance metrics

### Portability
- Works in local dev + container + K8s
- Configuration via env/secrets only
- No local-only assumptions

## Development Workflow

### "No Task = No Code" Rule
Claude Code only implements tasks that exist in the spec/tasks system. No ad-hoc code generation allowed—every implementation must correspond to a defined task in the spec system.

### Code Referencing Standard
All PRs/commits and file headers/comments must use standard referencing:
[From]: spec §X.Y + plan §A.B

### Repository Structure Standard (Monorepo)
- /.spec-kit/config.yaml
- /specs/** (overview, features, api, database, ui, mcp)
- /frontend (Next.js)
- /backend (FastAPI)
- CLAUDE.md (root) forwarding to AGENTS.md
- AGENTS.md (agent behavior rules)
- specs-history/ (or /specs/history) for iteration trail

## Documentation Standards (Required Deliverables)

### Required Documentation
- README: setup + run + deploy + demo steps
- CLAUDE.md: how to run Claude Code in this repo (root + frontend + backend if needed)
- Explicit env var list and examples (.env.example)

## Success Criteria

### Project Completion Requirements
- All 5 phases implemented using Spec-Driven Development with clear spec history and traceability
- Demonstrable working app at each checkpoint (CLI → Web → Chatbot → Minikube → Cloud)
- AI chatbot correctly performs todo operations via MCP tools using natural language and confirms actions
- Deployments are reproducible via documented commands (local and cloud), with Helm charts and environment configuration

### Submission-Ready Artifacts per Phase
- Public GitHub repo link
- Vercel deployed frontend link (where required)
- Backend deployment with proper documentation

## Governance

### Constitution Supremacy
This constitution supersedes all other practices and development guidelines. All development activities must comply with these principles and constraints.

### Amendment Process
Amendments require:
- Documentation of rationale and impact
- Approval from project maintainers
- Migration plan for existing implementations if needed
- Update to all dependent templates and documentation

### Compliance Verification
- All PRs/reviews must verify constitution compliance
- Code generation tools must validate against constitution rules
- Regular compliance audits required during development

**Version**: 1.0.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
