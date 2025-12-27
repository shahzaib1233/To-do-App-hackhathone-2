---
id: 1
title: Create Console Todo App Spec
stage: spec
date: 2025-12-27
surface: agent
model: Claude Sonnet 4.5
feature: 001-console-todo-app
branch: 001-console-todo-app
user: Claude Code
command: /sp.specify
labels: [specification, todo-app, console-app, python]
links:
  spec: specs/001-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-console-todo-app/spec.md
 - specs/001-console-todo-app/checklists/requirements.md
tests:
 - null
---

## Prompt

```text
Project: Hackathon II — Evolution of Todo
Phase: I — In-Memory Python Console App (UV + Python 3.13+)

1) Purpose

Build a command-line todo application that stores tasks in memory (no DB, no files). The app supports the 5 basic features:

Add Task

View Task List

Update Task

Delete Task

Mark as Complete/Incomplete (toggle)

The app must be implemented using Spec-Driven Development with Claude Code + Spec-Kit Plus (no manual coding).

2) Users & Use Context

Primary user: A single local user running the app from terminal.

Environment: Windows CMD (also compatible with other terminals, but CMD is the target).

Data lifetime: Only during runtime. When the app exits, tasks are lost.

3) Core Entities (Domain Model)
Task

Fields:

id (integer, unique, auto-increment)

title (string, required, 1–200 chars)

description (string, optional, 0–1000 chars)

completed (boolean, default: false)

Computed/Display fields (optional):

status_label (string): "[x]" if completed else "[ ]"

4) User Journeys
J1: Add a Task

User selects "Add task"

User enters title

User optionally enters description

App confirms task was created and shows its ID

J2: View Task List

User selects "View tasks"

App prints all tasks in a readable list with ID and status indicators

If list is empty, app prints "No tasks found."

J3: Update a Task

User selects "Update task"

User enters task ID

App shows current title/description and prompts for new values

User can skip updating a field (keep existing)

App confirms update

J4: Delete a Task

User selects "Delete task"

User enters task ID

App confirms deletion (or shows error if not found)

J5: Toggle Complete

User selects "Toggle completion"

User enters task ID

App flips completion status (complete ↔ incomplete)

App confirms new status

J6: Exit

User selects "Exit"

App terminates gracefully

5) Functional Requirements
FR1 — Main Menu Loop

The application must run in a loop until user exits.

Menu must display available commands:

Add

View

Update

Delete

Toggle complete

Exit

FR2 — Add Task

Title is required.

Description optional.

Auto-assign incrementing numeric ID starting from 1.

New tasks start as completed = false.

FR3 — View Tasks

Show all tasks.

Each task line must show:

ID

status indicator [x] or [ ]

title

On a separate line (or indented) show description if present.

If no tasks, show a friendly empty message.

FR4 — Update Task

User supplies ID.

If task not found, show a clear error and return to menu.

Allow updating:

title

description

User may press Enter to keep existing value.

FR5 — Delete Task

User supplies ID.

If task not found, show a clear error.

If found, remove it from list.

FR6 — Toggle Complete

User supplies ID.

If found, toggle completion status.

If not found, show a clear error.

FR7 — Input Validation

Reject invalid menu choice (non-existent option).

Reject invalid ID input:

non-numeric

negative or zero

Title validation:

must be non-empty after trimming

<= 200 characters

Description validation:

<= 1000 characters

6) Non-Functional Requirements
NFR1 — Clean Project Structure

Repository must contain:

/src for python source

README.md for setup/run on Windows CMD

CLAUDE.md for Claude Code instructions

Constitution + specs history folder (per hackathon requirement)

NFR2 — Code Quality

Clean code principles:

small functions

clear naming

separation of concerns (UI vs logic)

Avoid global mutable state except a single in-memory store object if needed.

NFR3 — Compatibility (Windows CMD Target)

Must run on Windows CMD with Python 3.13+.

Use UV for environment and running commands.

Do not rely on Linux-only commands in README instructions.

NFR4 — Usability

Clear prompts and confirmations.

Errors should never crash the app; it should return to menu.

7) CLI Interaction Specification
Menu (illustrative)

Add task

View tasks

Update task

Delete task

Toggle complete

Exit

User enters a number (1–6).

Output Formatting Rules

Task list format:

1 [ ] Buy groceries

Milk, eggs, bread

Completed tasks show [x].

Error Messages (minimum)

"Invalid choice. Please select 1–6."

"Invalid task ID. Please enter a positive number."

"Task not found for ID: <id>"

"Title cannot be empty."

8) Edge Cases

Updating title to empty string: reject and keep prompting or abort update with error.

Deleting from empty list: show "No tasks found."

Toggle completion on empty list: show "No tasks found."

Very long input: enforce max length constraints.

9) Out of Scope (Phase I Non-Goals)

Persistent storage (files/DB)

Multi-user auth

Search/filter/sort

Due dates, reminders, recurring tasks

Any AI chatbot features

10) Acceptance Criteria Checklist

✅ Add task creates task with unique ID, required title, optional description, completed=false.

✅ View tasks displays all tasks with ID and status indicators.

✅ Update task can change title/description; Enter keeps existing values.

✅ Delete task removes task by ID; not found errors handled.

✅ T
```

## Response snapshot

Created a comprehensive feature specification for the console todo application. The specification includes:

1. Six user stories covering all core functionality (Add, View, Update, Delete, Toggle, Exit)
2. Detailed functional requirements (FR-001 through FR-010)
3. Key entity definition for the Task object
4. Success criteria with measurable outcomes (SC-001 through SC-005)
5. Edge cases and error handling requirements
6. Quality checklist validation

The spec follows the template structure and maintains focus on user value without implementation details, making it technology-agnostic as required.

## Outcome

- ✅ Impact: Created complete feature specification for console todo app
- 🧪 Tests: No tests required for specification creation
- 📁 Files: Created spec.md and requirements checklist in specs/001-console-todo-app/
- 🔁 Next prompts: Ready to proceed with planning phase (/sp.plan)
- 🧠 Reflection: Specification covers all required functionality with clear acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to planning phase