# Data Model: Console Todo App

**Date**: 2025-12-27
**Feature**: 001-console-todo-app
**Input**: Feature specification and implementation plan

## Core Entities

### Task

The primary entity representing a single todo item.

**Fields**:
- `id` (int): Unique identifier, auto-incremented starting from 1
- `title` (str): Required task title, 1-200 characters
- `description` (str | None): Optional task description, 0-1000 characters
- `completed` (bool): Task completion status, default False

**Validation Rules**:
- `id` must be unique and positive integer
- `title` must be 1-200 characters when provided
- `title` is required on creation, optional on update (but if provided must be valid)
- `description` can be None or 0-1000 characters
- `completed` is boolean, default False on creation

**State Transitions**:
- New task: `completed = False`
- Toggle operation: `completed = not completed`

### TaskStore

In-memory storage for tasks.

**Structure**:
- `tasks` (dict[int, Task]): Dictionary mapping task IDs to Task objects
- `next_id` (int): Counter for auto-incrementing ID assignment, starts at 1

**Operations**:
- Add task: assign `id = next_id`, increment `next_id`
- Get task: lookup by ID in `tasks` dictionary
- Update task: modify fields of existing Task object
- Delete task: remove from `tasks` dictionary
- List tasks: return all Task objects in `tasks` dictionary

## Data Relationships

### Task Relationships
- No relationships to other entities (standalone entity)

## Validation Rules

### Title Validation
- Required on task creation
- Optional on task update (but if provided, must be valid)
- Must be trimmed string of 1-200 characters
- Cannot be empty or whitespace-only after trimming

### Description Validation
- Optional on both creation and update
- Maximum length of 1000 characters
- Can be None or string of 0-1000 characters

### ID Validation
- Must be positive integer
- Must exist in the task store for update/delete/toggle operations
- Auto-assigned on creation starting from 1 and incrementing

## Data Lifecycle

### Creation
1. User provides title and optional description
2. System assigns next available ID
3. System sets completed status to False
4. Task is stored in the task dictionary

### Reading
1. All tasks are retrieved from the task dictionary
2. Tasks are typically sorted by ID for display

### Update
1. User provides task ID and new field values
2. System validates new field values
3. System updates the existing task in the dictionary

### Deletion
1. User provides task ID
2. System removes the task from the dictionary

### Toggle Completion
1. User provides task ID
2. System flips the completed status of the task in the dictionary