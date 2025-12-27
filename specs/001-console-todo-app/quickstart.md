# Quickstart Guide: Console Todo App

**Date**: 2025-12-27
**Feature**: 001-console-todo-app
**Input**: Feature specification and implementation plan

## Getting Started

This guide provides instructions to run the console todo application on Windows CMD and other platforms.

### Prerequisites

- Python 3.13+ installed
- UV package manager installed
- Windows CMD, PowerShell, or compatible terminal

### Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies using UV:

```cmd
uv sync
```

### Running the Application

To run the application using UV:

```cmd
uv run python -m src.todo_app.main
```

Alternatively, if you have the project set up with a proper entry point:

```cmd
uv run src/todo_app/main.py
```

### Using the Application

Once the application starts, you'll see a menu with the following options:

```
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Toggle complete
6. Exit
```

Enter the number corresponding to the action you want to perform.

#### Adding a Task
1. Select option 1
2. Enter a title (required, 1-200 characters)
3. Optionally enter a description (0-1000 characters)
4. The system will confirm creation with the assigned task ID

#### Viewing Tasks
1. Select option 2
2. All tasks will be displayed with ID, status indicator ([x] or [ ]), and title
3. If a task has a description, it will be shown indented on the next line
4. If no tasks exist, "No tasks found." will be displayed

#### Updating a Task
1. Select option 3
2. Enter the task ID
3. Enter the new title (or press Enter to keep the current title)
4. Enter the new description (or press Enter to keep the current description)
5. The system will confirm the update

#### Deleting a Task
1. Select option 4
2. Enter the task ID
3. The system will confirm deletion

#### Toggling Task Completion
1. Select option 5
2. Enter the task ID
3. The system will flip the completion status and confirm the change

#### Exiting
1. Select option 6
2. The application will terminate gracefully

### Error Handling

The application handles various error conditions gracefully:

- Invalid menu choices: Shows "Invalid choice. Please select 1-6."
- Invalid task IDs: Shows "Invalid task ID. Please enter a positive number."
- Non-existent task IDs: Shows "Task not found for ID: <id>"
- Empty titles: Shows "Title cannot be empty."

### Troubleshooting

#### Common Issues

1. **Python not found**: Ensure Python 3.13+ is installed and in your PATH
2. **UV not installed**: Install UV with `pip install uv`
3. **Module not found**: Ensure you're running from the project root directory
4. **Permission errors**: Ensure you have read/write permissions to the project directory

#### Verifying Installation

Run the following command to verify UV is working:

```cmd
uv --version
```

### Development Setup

For development, you can run the application directly with Python:

```cmd
python -m src.todo_app.main
```

Or set up a virtual environment:

```cmd
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix
pip install -e .
python -m src.todo_app.main
```

### Windows CMD Specific Notes

- The application is designed to work in Windows CMD environment
- Character encoding should work correctly with UTF-8
- Terminal colors (if used) will be compatible with modern Windows terminals
- Command history and arrow keys should work for input editing