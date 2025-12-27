# Service Contracts: Console Todo App

**Date**: 2025-12-27
**Feature**: 001-console-todo-app
**Input**: Feature specification and implementation plan

## Service Interface

### TaskService

The primary service for task operations with defined method signatures and behaviors.

#### add_task(title: str, description: str | None) -> Task

**Purpose**: Create a new task with the provided title and optional description.

**Input Validation**:
- `title` must be 1-200 characters (non-empty after trimming)
- `description` must be 0-1000 characters if provided

**Behavior**:
- Assigns the next available auto-incremented ID
- Sets `completed` to `False`
- Stores the task in the in-memory store
- Returns the created Task object

**Exceptions**:
- `ValidationError` if title validation fails

#### list_tasks() -> list[Task]

**Purpose**: Retrieve all tasks sorted by ID in ascending order.

**Behavior**:
- Returns all tasks from the store
- Results are sorted by ID (ascending)
- Returns empty list if no tasks exist

**Exceptions**: None

#### update_task(task_id: int, title: str | None, description: str | None) -> Task

**Purpose**: Update an existing task's title and/or description.

**Input Validation**:
- `task_id` must exist in the store
- If `title` is provided, it must be 1-200 characters
- If `description` is provided, it must be 0-1000 characters
- `title` parameter of `None` means "no change"

**Behavior**:
- Updates only the fields that are not `None`
- Preserves existing values for `None` parameters
- Returns the updated Task object

**Exceptions**:
- `TaskNotFoundError` if task_id does not exist
- `ValidationError` if provided title validation fails

#### delete_task(task_id: int) -> Task

**Purpose**: Remove a task from the store.

**Input Validation**:
- `task_id` must exist in the store

**Behavior**:
- Removes the task from the store
- Returns the deleted Task object

**Exceptions**:
- `TaskNotFoundError` if task_id does not exist

#### toggle_complete(task_id: int) -> Task

**Purpose**: Flip the completion status of a task.

**Input Validation**:
- `task_id` must exist in the store

**Behavior**:
- Changes `completed` status from `True` to `False` or `False` to `True`
- Returns the updated Task object

**Exceptions**:
- `TaskNotFoundError` if task_id does not exist

## Domain Exceptions

### TaskNotFoundError(task_id: int)

**Purpose**: Thrown when an operation is requested on a task that does not exist.

**Fields**:
- `task_id`: The ID of the task that was not found

### ValidationError(message: str)

**Purpose**: Thrown when input validation fails.

**Fields**:
- `message`: Human-readable description of the validation error

## CLI Interface Contracts

### Menu Display

**Behavior**:
- Display menu options as numbered list (1-6)
- Options: Add, View, Update, Delete, Toggle complete, Exit
- Prompt user for selection

### Input Validation

**Behavior**:
- Validate menu choice is integer 1-6
- Validate task IDs are positive integers
- Handle blank input appropriately (Enter to keep existing values)

### Output Formatting

**Task Display Format**:
- `{id} [x| ] {title}` (e.g., "1 [ ] Buy groceries")
- If description exists: print indented on next line
- Empty state: "No tasks found."

**Confirmation Messages**:
- Add: "Created task #{id}"
- Update: "Updated task #{id}"
- Delete: "Deleted task #{id}"
- Toggle: "Task #{id} marked {complete|incomplete}"