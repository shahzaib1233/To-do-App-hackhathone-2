# Agent Behavior Rules for Hackathon II — The Evolution of Todo

This document defines the behavior rules and guidelines for AI agents working on the Hackathon II project, in accordance with the project constitution.

## Core Agent Principles

### 1. Spec-Driven Development Compliance
- Agents must only implement features that are defined in the spec/tasks system
- No code generation without corresponding task definitions in `/specs/[feature]/tasks.md`
- All implementations must trace back to specific user stories and requirements in the spec

### 2. No Manual Coding Enforcement
- Agents act as "system architects" - focus on spec refinement and task definition
- Direct code typing is prohibited unless specified in tasks
- Use tooling and automation to generate code from specifications

### 3. Traceability Requirements
- Every code change must reference originating specification sections
- Use format: `[From]: spec §X.Y + plan §A.B` in all commits and comments
- Maintain clear audit trail from user requirements to implementation

### 4. Phase Compliance
- Follow iterative evolution: CLI → Full-stack → AI chatbot → Local K8s → Cloud/event-driven
- No skipping phases - each must be completed before proceeding
- Respect stack constraints for each phase

## MCP Tool Specifications

### Required MCP Tools for Todo Operations
The following MCP tools must be available for AI agents to perform todo operations:

- `add_task`: Add a new task to the todo list
- `list_tasks`: List all tasks for the authenticated user
- `update_task`: Update task details (title, description, etc.)
- `delete_task`: Delete a specific task
- `complete_task`: Mark a task as complete/incomplete

### Tool Contract Requirements
- All tools must accept proper authentication context
- Tools must enforce user_id ownership on all operations
- Return shapes must be consistent and well-defined
- Error handling must be graceful with clear messages

## Quality Gates

### Before Implementation
- All tasks must pass constitution compliance check
- Dependencies must be clearly defined and resolvable
- Acceptance criteria must be explicit and testable

### During Implementation
- No breaking changes without proper versioning
- All user stories must remain independently testable
- Security and user isolation must be maintained

### After Implementation
- All tests must pass (contract, integration, unit)
- Documentation must be updated
- PHR must be created for all significant changes

## Architecture Decisions

### State Management
- Backend services must be stateless
- All conversation and task state persisted in database
- Server restarts must not result in data loss

### Security & Authentication
- All API endpoints require JWT authentication
- User data isolation enforced at database query level
- No hardcoded credentials or secrets in code

### Cloud-Native Requirements
- Container-ready architecture
- Configuration via environment variables/secrets
- Helm chart deployment capability
- Kubernetes readiness (health checks, etc.)

## Development Workflow

### Task Processing
1. Read `/specs/[feature]/tasks.md` for current tasks
2. Process tasks in priority order (P1 → P2 → P3)
3. Complete foundational tasks before user story implementation
4. Maintain independent testability of each user story

### Code Generation Standards
- Follow repository structure as defined in constitution
- Use consistent naming conventions
- Include proper error handling and logging
- Ensure cross-cutting concerns are addressed

## Compliance Verification

Agents must verify:
- Constitution compliance before any implementation
- Spec traceability for all code changes
- Quality gate requirements are met
- Proper documentation and PHR creation