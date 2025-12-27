---
description: "Task list for Console Todo App implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Create src/todo_app/ directory with __init__.py
- [X] T003 [P] Create specs-history/ directory
- [X] T004 Create placeholder files: src/todo_app/main.py, src/todo_app/cli.py, src/todo_app/models.py, src/todo_app/store.py, src/todo_app/service.py, src/todo_app/validators.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T005 Create Task model in src/todo_app/models.py with fields: id (int), title (str), description (str | None), completed (bool)
- [X] T006 [P] Create domain exceptions in src/todo_app/models.py: TaskNotFoundError(task_id), ValidationError(message)
- [X] T007 Create in-memory store in src/todo_app/store.py with tasks dict and next_id counter
- [X] T008 Create validator functions in src/todo_app/validators.py: validate_title_required, validate_title_optional, validate_description, validate_positive_int
- [X] T009 Create TaskService class in src/todo_app/service.py with basic method signatures

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: User can add a new task to their todo list with title and optional description

**Independent Test**: User can start the app, select "Add task", enter a title and optional description, and see the task created with a unique ID.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Contract test for add_task endpoint in tests/unit/test_service.py
- [ ] T011 [P] [US1] Integration test for Add Task user journey in tests/integration/test_cli.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement create_task method in src/todo_app/store.py
- [X] T013 [US1] Implement add_task method in src/todo_app/service.py with validation
- [X] T014 [US1] Implement add_task handler in src/todo_app/cli.py with user prompts
- [X] T015 [US1] Add "Add task" option to main menu in src/todo_app/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: User can view all their tasks with proper formatting and status indicators

**Independent Test**: User can start the app, select "View tasks", and see a formatted list of all tasks with their status indicators.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T016 [P] [US2] Contract test for list_tasks endpoint in tests/unit/test_service.py
- [ ] T017 [P] [US2] Integration test for View Task List user journey in tests/integration/test_cli.py

### Implementation for User Story 2

- [X] T018 [P] [US2] Implement list_tasks method in src/todo_app/store.py
- [X] T019 [US2] Implement list_tasks method in src/todo_app/service.py
- [X] T020 [US2] Implement render_tasks helper in src/todo_app/cli.py with proper formatting
- [X] T021 [US2] Implement view_tasks handler in src/todo_app/cli.py with empty list handling
- [X] T022 [US2] Add "View tasks" option to main menu in src/todo_app/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: User can update an existing task's title and description by ID

**Independent Test**: User can select "Update task", enter a task ID, see current values, and modify title or description.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T023 [P] [US3] Contract test for update_task endpoint in tests/unit/test_service.py
- [ ] T024 [P] [US3] Integration test for Update Task user journey in tests/integration/test_cli.py

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement update_task method in src/todo_app/store.py
- [X] T026 [US3] Implement update_task method in src/todo_app/service.py with validation
- [X] T027 [US3] Implement update_task handler in src/todo_app/cli.py with current value display and Enter-to-keep behavior
- [X] T028 [US3] Add "Update task" option to main menu in src/todo_app/cli.py

**Checkpoint**: User Stories 1, 2, and 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: User can delete a task by ID

**Independent Test**: User can select "Delete task", enter a task ID, and confirm deletion.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T029 [P] [US4] Contract test for delete_task endpoint in tests/unit/test_service.py
- [ ] T030 [P] [US4] Integration test for Delete Task user journey in tests/integration/test_cli.py

### Implementation for User Story 4

- [X] T031 [P] [US4] Implement delete_task method in src/todo_app/store.py
- [X] T032 [US4] Implement delete_task method in src/todo_app/service.py
- [X] T033 [US4] Implement delete_task handler in src/todo_app/cli.py
- [X] T034 [US4] Add "Delete task" option to main menu in src/todo_app/cli.py

**Checkpoint**: User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Toggle Task Completion (Priority: P2)

**Goal**: User can toggle a task's completion status by ID

**Independent Test**: User can select "Toggle completion", enter a task ID, and see the status change.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T035 [P] [US5] Contract test for toggle_complete endpoint in tests/unit/test_service.py
- [ ] T036 [P] [US5] Integration test for Toggle Task Completion user journey in tests/integration/test_cli.py

### Implementation for User Story 5

- [X] T037 [P] [US5] Implement toggle_task method in src/todo_app/store.py
- [X] T038 [US5] Implement toggle_complete method in src/todo_app/service.py
- [X] T039 [US5] Implement toggle_complete handler in src/todo_app/cli.py
- [X] T040 [US5] Add "Toggle complete" option to main menu in src/todo_app/cli.py

**Checkpoint**: All core user stories (1-5) should now be independently functional

---

## Phase 8: User Story 6 - Exit Application (Priority: P1)

**Goal**: User can exit the application cleanly

**Independent Test**: User can select "Exit" and the application terminates gracefully.

### Implementation for User Story 6

- [X] T041 [US6] Implement exit functionality in main menu loop in src/todo_app/cli.py
- [X] T042 [US6] Add "Exit" option to main menu in src/todo_app/cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Input Validation & Error Handling (Cross-cutting)

**Goal**: Implement all validation and error handling requirements from spec

- [X] T043 [P] Implement menu choice validation (1-6) in main menu loop
- [X] T044 [P] Implement task ID validation in all CLI handlers
- [X] T045 Implement title validation (1-200 chars) in validators.py and service.py
- [X] T046 Implement description validation (0-1000 chars) in validators.py and service.py
- [X] T047 Implement proper error handling with friendly messages in CLI layer
- [X] T048 Implement "Invalid choice. Please select 1–6." error message
- [X] T049 Implement "Invalid task ID. Please enter a positive number." error message
- [X] T050 Implement "Task not found for ID: <id>" error message
- [X] T051 Implement "Title cannot be empty." error message

---

## Phase 10: Entry Point & CLI Integration

**Goal**: Wire up the complete application

- [X] T052 Create main application loop in src/todo_app/cli.py with TodoCLI class
- [X] T053 Create entry point in src/todo_app/main.py that initializes store, service, and CLI
- [X] T054 Implement proper exception handling in CLI to prevent crashes

---

## Phase 11: Documentation & Setup

**Goal**: Complete setup and documentation

- [X] T055 Create README.md with Windows CMD setup and run instructions
- [X] T056 Update CLAUDE.md with explicit instructions about following Spec-Kit workflow
- [X] T057 Create pyproject.toml or requirements.txt for UV dependency management

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T058 [P] Documentation updates in docs/
- [ ] T059 Code cleanup and refactoring
- [ ] T060 Performance optimization across all stories
- [ ] T061 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T062 Security hardening
- [ ] T063 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Cross-cutting (Phase 9+)**: Depends on user story implementations
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - Basic functionality needed for all stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add_task endpoint in tests/unit/test_service.py"
Task: "Integration test for Add Task user journey in tests/integration/test_cli.py"

# Launch all implementation for User Story 1 together:
Task: "Implement create_task method in src/todo_app/store.py"
Task: "Implement add_task method in src/todo_app/service.py with validation"
```

---

## Implementation Strategy

### MVP First (User Stories 1-2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Task List)
5. **STOP and VALIDATE**: Test User Stories 1-2 independently
6. Run basic smoke test to add and view tasks
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Add functionality!)
3. Add User Story 2 → Test independently → Deploy/Demo (View functionality!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Add validation/error handling → Test all flows → Deploy/Demo
9. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Add Task)
   - Developer B: User Story 2 (View Task List)
   - Developer C: User Stories 3-6 (Update, Delete, Toggle, Exit)
   - Developer D: Validation & Error Handling
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence