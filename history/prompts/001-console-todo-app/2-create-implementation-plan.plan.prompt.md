---
id: 2
title: Create Implementation Plan
stage: plan
date: 2025-12-27
surface: agent
model: Claude Sonnet 4.5
feature: 001-console-todo-app
branch: 001-console-todo-app
user: Claude Code
command: /sp.plan
labels: [planning, architecture, python, console-app]
links:
  spec: specs/001-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-console-todo-app/plan.md
 - specs/001-console-todo-app/research.md
 - specs/001-console-todo-app/data-model.md
 - specs/001-console-todo-app/contracts/service-contracts.md
 - specs/001-console-todo-app/quickstart.md
 - CLAUDE.md
tests:
 - null
---

## Prompt

```text
Project: Hackathon II — Evolution of Todo
Phase: I — In-Memory Python Console App (UV + Python 3.13+)
Source: /sp.specify (Phase I)

1) Architecture Overview (HOW)

This phase implements a single-process, terminal-based application with in-memory state only.

Design goals:

Keep logic testable and separated from terminal I/O.

Use small, clear modules so Claude Code can implement reliably.

Ensure all behaviors map directly to /sp.specify acceptance criteria.

High-level components:

CLI Layer (Presentation)

Displays menu, prompts for input, prints results/errors.

No business rules except basic formatting and input parsing.

Service Layer (Business Logic)

Implements task CRUD + completion toggle.

Validates domain rules (title length, id validity, etc.).

Repository/Store (In-memory Data)

Stores tasks in a collection (list/dict).

Generates IDs (auto-increment).

Domain Models

Task model (id, title, description, completed).

Optional DTOs for create/update requests (for clean validation boundaries).

2) Data Model & In-Memory Storage
Task

id: int

title: str

description: str | None

completed: bool

Storage Strategy

Store tasks in-memory using:

dict[int, Task] for O(1) lookup by ID, OR

list[Task] + search loop (acceptable but slower).

Recommendation: dict + a simple next_id counter:

next_id starts at 1

On create: assign id = next_id, then increment next_id.

No persistence layer (no files/db). App exit clears tasks.

3) Module & Folder Structure

Target repo structure (minimum):

hackathon-todo-phase1/
├─ specs-history/                 # store spec revisions
├─ src/
│  └─ todo_app/
│     ├─ __init__.py
│     ├─ main.py                  # entrypoint (CLI loop)
│     ├─ cli.py                   # menu + IO helpers (prompts, rendering)
│     ├─ models.py                # Task model / dataclasses
│     ├─ store.py                 # in-memory repo (tasks dict + next_id)
│     ├─ service.py               # business logic (add/update/delete/toggle/list)
│     └─ validators.py            # input/domain validation utilities
├─ README.md
└─ CLAUDE.md


Notes:

main.py should be minimal: initialize store/service and start CLI loop.

Keep service functions pure-ish (no print/input inside service).

4) Control Flow (Runtime Sequence)
App Startup

main.py creates:

TaskStore

TaskService(store)

TodoCLI(service)

Call cli.run() which loops until exit.

Menu Loop (Every Iteration)

Print menu (1–6).

Read user choice.

Dispatch to handler:

Add → prompt title/description → service.add_task()

View → service.list_tasks() → render list

Update → prompt id/title/description → service.update_task()

Delete → prompt id → service.delete_task()

Toggle → prompt id → service.toggle_complete()

Exit → break loop

Render success message or error message.

Continue loop.

5) Service API (Internal Contracts)

The CLI should call service methods like:

add_task(title: str, description: str | None) -> Task

list_tasks() -> list[Task] (sorted by id ascending)

update_task(task_id: int, title: str | None, description: str | None) -> Task

None means "no change" (Enter pressed)

delete_task(task_id: int) -> Task (or return bool)

toggle_complete(task_id: int) -> Task

Errors:

Raise domain exceptions:

TaskNotFoundError(task_id)

ValidationError(message)
CLI catches these and prints friendly messages.

6) Validation Plan

Validation is split:

CLI validation: parse menu choice; parse integer id; handle blank input.

Domain validation (service/validators):

Title required on create (trimmed, non-empty, <= 200)

Title optional on update; if provided must be valid (non-empty, <= 200)

Description max length 1000

Task ID must exist for update/delete/toggle

7) Rendering Plan (CLI Output Formatting)

Rendering rules (from /sp.specify):

Each task prints: "{id} [x| ] {title}"

If description exists: print indented next line.

Empty state: "No tasks found."

Confirmations:

Add: "Created task #{id}"

Update: "Updated task #{id}"

Delete: "Deleted task #{id}"

Toggle: "Task #{id} marked complete/incomplete"

8) Testing Approach (Lightweight, Optional but Recommended)

Even for Phase I, add basic unit tests if feasible:

Service tests (no I/O):

create/list/update/delete/toggle success

invalid title, too long description

not found errors
If tests are included, keep them minimal and fast.

9) UV + Windows CMD Execution Plan (README Expectations)

README should include CMD-friendly commands (no bash-only assumptions), for example:

Install deps and run:

uv sync (if using pyproject)

uv run python -m todo_app.main (or equivalent entry module)

Ensure instructions do not require WSL.

10) Implementation Sequencing (Work Breakdown Guidance)

Recommended implementation order (maps cleanly to tasks):

Define Task model + exceptions

Implement store (add/get/update/remove/list)

Implement validators

Implement service methods with validation + errors

Implement CLI menu loop + renderers

Manual smoke run via CMD and verify acceptance cr
```

## Response snapshot

Created a comprehensive implementation plan for the console todo application with the following artifacts:

1. **Plan Document** (plan.md): Detailed architecture overview with technical context, project structure, and constitution compliance check
2. **Research Document** (research.md): Technical decisions and alternatives considered for all major implementation choices
3. **Data Model** (data-model.md): Entity definitions and validation rules for the Task object
4. **Service Contracts** (contracts/service-contracts.md): API contracts defining internal service interfaces
5. **Quickstart Guide** (quickstart.md): Instructions for running and using the application
6. **Agent Context** (CLAUDE.md): Updated with current technology stack and project information

The plan follows clean architecture principles with separation of concerns between CLI, service, and data layers. All implementation details align with the original specification requirements and constitutional principles.

## Outcome

- ✅ Impact: Complete implementation plan with all required artifacts
- 🧪 Tests: No tests required for planning phase
- 📁 Files: Created 6 documentation files in specs/001-console-todo-app/ and updated CLAUDE.md
- 🔁 Next prompts: Ready to proceed with task generation (/sp.tasks)
- 🧠 Reflection: Plan provides clear roadmap for implementation with proper architecture

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to task generation phase