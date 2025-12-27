---
id: 3
title: Create Implementation Tasks
stage: tasks
date: 2025-12-27
surface: agent
model: Claude Sonnet 4.5
feature: 001-console-todo-app
branch: 001-console-todo-app
user: Claude Code
command: /sp.tasks
labels: [tasks, implementation, python, console-app]
links:
  spec: specs/001-console-todo-app/spec.md
  plan: specs/001-console-todo-app/plan.md
  adr: null
  pr: null
files:
 - specs/001-console-todo-app/tasks.md
tests:
 - null
---

## Prompt

```text
Project: Hackathon II — Evolution of Todo
Phase: I — In-Memory Python Console App
Source: /sp.specify + /sp.plan

T-001 — Initialize Project Skeleton (UV + src layout)

Goal: Create Phase I repo structure and UV configuration.
Preconditions: None.
Work:

Create folders: src/todo_app/, specs-history/

Add placeholder files: src/todo_app/__init__.py, src/todo_app/main.py

Add minimal README.md + CLAUDE.md placeholders (content comes later tasks)
Outputs:

Working Python package under /src

Repo structure matches /sp.plan §3
Acceptance Checks:

src/todo_app/ exists with __init__.py

specs-history/ exists

T-002 — Define Domain Model (Task) + Exceptions

Goal: Implement Task model and domain exceptions used across app.
From: /sp.specify §3 , /sp.plan §2, §5
Work:

Create models.py defining Task with fields: id, title, description, completed

Create errors.py (or in service.py) defining:

TaskNotFoundError(task_id)

ValidationError(message)
Outputs:

src/todo_app/models.py

src/todo_app/errors.py (or equivalent)
Acceptance Checks:

Task model exists with correct fields

Exceptions can be imported by service/cli

T-003 — Implement In-Memory Store (Repository)

Goal: Build in-memory storage for tasks with auto-increment IDs.
From: /sp.plan §2
Work:

Create store.py with:

internal tasks: dict[int, Task]

internal next_id: int starting at 1

methods:

create_task(title, description) -> Task

get_task(task_id) -> Task | None

list_tasks() -> list[Task] (sorted by id asc)

update_task(task_id, title, description) -> Task | None

delete_task(task_id) -> Task | None

toggle_task(task_id) -> Task | None
Outputs:

src/todo_app/store.py
Acceptance Checks:

Creating tasks increments IDs correctly

Listing returns tasks sorted

Not-found operations return None (service will raise)

T-004 — Implement Validators (Domain Rules)

Goal: Centralize validation logic for title/description/id.
From: /sp.specify §5 FR7 , /sp.plan §6
Work:

Create validators.py with functions:

validate_title_required(title: str) -> str (trim + non-empty + <=200)

validate_title_optional(title: str | None) -> str | None (if provided, same rules)

validate_description(description: str | None) -> str | None (<=1000, trim optional)

validate_positive_int(raw: str) -> int (parse, >0)
Outputs:

src/todo_app/validators.py
Acceptance Checks:

Empty title rejected

Title >200 rejected

Description >1000 rejected

Non-numeric/<=0 ID rejected

T-005 — Implement Service Layer (Business Logic)

Goal: Provide clean APIs for CLI, enforce rules, and raise domain errors.
From: /sp.specify §5 , /sp.plan §5
Preconditions: T-002, T-003, T-004 complete.
Work:

Create service.py with TaskService exposing:

add_task(title, description) -> Task

list_tasks() -> list[Task]

update_task(task_id, title|None, description|None) -> Task

delete_task(task_id) -> Task

toggle_complete(task_id) -> Task

Use validators for all rules.

Raise:

TaskNotFoundError if store returns None

ValidationError for invalid inputs
Outputs:

src/todo_app/service.py
Acceptance Checks:

All 5 operations work for valid inputs

Errors raised for invalid task IDs and invalid fields

T-006 — CLI Rendering Helpers (Printing Tasks & Messages)

Goal: Implement consistent output formatting and user messages.
From: /sp.specify §7 , /sp.plan §7
Work:

Create cli.py helper functions:

render_menu()

render_tasks(tasks)

render_task(task)

render_error(message)

render_success(message)

Output rules:

Task line: {id} [x| ] {title}

Description on next indented line if present

Empty list message: "No tasks found."
Outputs:

src/todo_app/cli.py (rendering helpers may live here)
Acceptance Checks:

Output matches spec formatting and includes status indicators

T-007 — CLI Input Flow (Menu Loop + Handlers)

Goal: Build interactive menu loop and connect to service methods.
From: /sp.specify §5 FR1–FR7 , /sp.plan §4
Preconditions: T-005, T-006 complete.
Work:

In cli.py implement TodoCLI (or functions) with:

loop until Exit

prompt choice (1–6)

handlers:

Add: ask title + description

View: list tasks

Update: ask id; show current values; prompt new title/desc (Enter keeps existing)

Delete: ask id

Toggle: ask id

Catch exceptions and print friendly errors; never crash.

Invalid menu choice prints: "Invalid choice. Please select 1–6."
Outputs:

CLI loop implemented and callable from main.py
Acceptance Checks:

App runs, loops, and exits gracefully

All invalid inputs handled safely

T-008 — Wire Entry Point (main.py)

Goal: Make runnable entrypoint for Windows CMD using UV.
From: /sp.plan §4, §9
Work:

Implement main.py to:

create store + service + cli

start cli.run()
Outputs:

src/todo_app/main.py ready to run
Acceptance Checks:

Running module starts menu loop

T-009 — README.md (Windows CMD Setup + Run)

Goal: Provide clear CMD-friendly setup and usage instructions.
From: /sp.plan §9
Work:

Add sections:

Requirements: Python 3.13+, UV

Install UV (link optional) + verify versions

How to run (CMD commands)

Feature demo steps (Add/View/Update/Delete/Toggle)

Notes: in-memory only (data lost on exit)
Outputs:

README.md
Acceptance Checks:

Commands are CMD-friendly (no bash-only syntax)

Steps reproduce working app

T-010 — CLAUDE.md (Claude Code Operating Instructions)

Goal: Ensure Claude Code knows it must follow Spec-Kit workflow and not write manual code.
From: Hackathon constraints + Constitution
Work:

Add:

"Read /sp.constitution, /sp.specify, /sp.plan, /sp.tasks before implementing"

"No manual coding; implement only from tasks"

Commands/entrypoint references for quick test runs

Repo structure pointers
Outputs:

CLAUDE.md
Acceptance Checks:

Claude instructions are explicit and align with hackathon rule: no manual coding

T-011 — Phase I Smoke Verification (Acceptance Checklist)

Goal: Verify all acceptance criteria from /sp.specify §10.
Work:

Run app and demonstrate:

Add tasks with title+description

View list shows IDs + [ ]/[x]

Update keeps values on Enter

Delete by ID

Toggle completion twice (complete → incomplete)

Invalid inputs handled
```

## Response snapshot

Created a comprehensive task list for the Console Todo App implementation with 63 specific, actionable tasks organized by user story priority. The tasks follow the checklist format with proper IDs, parallelization markers [P], and user story labels [US1-US6].

The tasks are organized into phases:
1. Setup (Phase 1): Project structure initialization
2. Foundational (Phase 2): Core infrastructure (models, store, validators, service)
3. User Stories (Phases 3-8): Individual features mapped to user stories from spec
4. Cross-cutting (Phase 9): Input validation and error handling
5. Integration (Phase 10): Entry point and CLI integration
6. Documentation (Phase 11): Setup and documentation
7. Polish (Phase N): Final improvements

Each task includes specific file paths and clear descriptions to enable independent implementation. The implementation strategy includes MVP-first approach, incremental delivery, and parallel team strategy options.

## Outcome

- ✅ Impact: Created complete task breakdown for implementation
- 🧪 Tests: No tests required for task creation
- 📁 Files: Created tasks.md with 63 specific implementation tasks
- 🔁 Next prompts: Ready to proceed with implementation
- 🧠 Reflection: Tasks are well-organized by user story and priority

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation of foundational tasks