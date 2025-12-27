# Feature Specification: Console Todo App

**Feature Branch**: `001-console-todo-app`
**Created**: 2025-12-27
**Status**: Draft
**Input**: User description: "Project: Hackathon II — Evolution of Todo
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

✅ T"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task (Priority: P1)

As a user, I want to add a new task to my todo list so that I can track what I need to do.

**Why this priority**: This is the foundational capability - without being able to add tasks, the app has no purpose.

**Independent Test**: User can start the app, select "Add task", enter a title and optional description, and see the task created with a unique ID.

**Acceptance Scenarios**:

1. **Given** I am on the main menu, **When** I select "Add task", **Then** I am prompted to enter a title and optional description
2. **Given** I have entered a valid title, **When** I submit the form, **Then** a new task is created with a unique auto-incrementing ID and default status of incomplete
3. **Given** I enter an empty title, **When** I try to submit, **Then** I receive an error and am prompted again

---

### User Story 2 - View Task List (Priority: P1)

As a user, I want to view all my tasks so that I can see what I need to do.

**Why this priority**: This is a core capability that allows users to see their tasks.

**Independent Test**: User can start the app, select "View tasks", and see a formatted list of all tasks with their status indicators.

**Acceptance Scenarios**:

1. **Given** I have added tasks to the list, **When** I select "View tasks", **Then** I see all tasks with their ID, status indicator, title, and description (if present)
2. **Given** there are no tasks in the list, **When** I select "View tasks", **Then** I see a friendly "No tasks found" message
3. **Given** I have completed tasks, **When** I view the list, **Then** completed tasks show [x] and incomplete tasks show [ ]

---

### User Story 3 - Update Task (Priority: P2)

As a user, I want to update an existing task so that I can correct mistakes or modify details.

**Why this priority**: Allows users to maintain the accuracy of their task information.

**Independent Test**: User can select "Update task", enter a task ID, see current values, and modify title or description.

**Acceptance Scenarios**:

1. **Given** I have existing tasks, **When** I select "Update task" and enter a valid ID, **Then** I see the current title and description and can modify them
2. **Given** I enter an invalid task ID, **When** I try to update, **Then** I receive a "Task not found" error
3. **Given** I am updating a task, **When** I press Enter without changing a field, **Then** the original value is preserved

---

### User Story 4 - Delete Task (Priority: P2)

As a user, I want to delete a task so that I can remove items I no longer need to track.

**Why this priority**: Allows users to clean up their task list.

**Independent Test**: User can select "Delete task", enter a task ID, and confirm deletion.

**Acceptance Scenarios**:

1. **Given** I have existing tasks, **When** I select "Delete task" and enter a valid ID, **Then** the task is removed from the list
2. **Given** I enter an invalid task ID, **When** I try to delete, **Then** I receive a "Task not found" error
3. **Given** I have deleted a task, **When** I view the list, **Then** the task no longer appears

---

### User Story 5 - Toggle Task Completion (Priority: P2)

As a user, I want to mark tasks as complete/incomplete so that I can track my progress.

**Why this priority**: Essential functionality for task management - marking tasks as done.

**Independent Test**: User can select "Toggle completion", enter a task ID, and see the status change.

**Acceptance Scenarios**:

1. **Given** I have an incomplete task, **When** I select "Toggle completion" and enter the ID, **Then** the task becomes complete
2. **Given** I have a complete task, **When** I select "Toggle completion" and enter the ID, **Then** the task becomes incomplete
3. **Given** I enter an invalid task ID, **When** I try to toggle, **Then** I receive a "Task not found" error

---

### User Story 6 - Exit Application (Priority: P1)

As a user, I want to exit the application cleanly so that I can return to the command line.

**Why this priority**: Basic application lifecycle requirement.

**Independent Test**: User can select "Exit" and the application terminates gracefully.

**Acceptance Scenarios**:

1. **Given** I am in the application, **When** I select "Exit", **Then** the application terminates without errors
2. **Given** I am performing an operation, **When** I select "Exit", **Then** the application returns to the main menu first, then allows exit

### Edge Cases

- What happens when a user enters a very long title or description (over 200/1000 chars)?
- How does the system handle non-numeric input when a number is expected?
- What happens when updating a task with an empty string as the new title?
- How does the system handle negative or zero IDs when a positive number is expected?
- What happens when attempting operations on an empty list (update, delete, toggle)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a main menu loop with options: Add, View, Update, Delete, Toggle complete, Exit
- **FR-002**: System MUST allow users to add tasks with required title (1-200 chars) and optional description (0-1000 chars)
- **FR-003**: System MUST assign auto-incrementing numeric IDs starting from 1 to new tasks
- **FR-004**: System MUST display all tasks with ID, status indicator [x]/[ ], title, and description (if present)
- **FR-005**: System MUST allow users to update task title and description by ID
- **FR-006**: System MUST allow users to delete tasks by ID
- **FR-007**: System MUST allow users to toggle task completion status by ID
- **FR-008**: System MUST validate user input: menu choices (1-6), numeric IDs, title length (1-200), description length (0-1000)
- **FR-009**: System MUST handle invalid input gracefully with appropriate error messages
- **FR-010**: System MUST store tasks in memory only (no persistence to files or database)

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single todo item with id (integer), title (string), description (string), completed (boolean)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, view, update, delete, and toggle task completion within a single session
- **SC-002**: All input validation requirements are enforced (character limits, numeric validation, etc.)
- **SC-003**: Error handling prevents application crashes - invalid inputs return to menu instead of terminating
- **SC-004**: Task operations maintain data integrity (IDs remain unique, status toggles work correctly)
- **SC-005**: Application runs successfully in Windows CMD environment with Python 3.13+