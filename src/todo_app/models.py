"""
Console Todo App - Data Models

This module contains the data models and domain exceptions for the todo application.
"""
from dataclasses import dataclass
from typing import Optional


class TaskNotFoundError(Exception):
    """
    Exception raised when a task is not found by ID.
    """
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task not found for ID: {task_id}")


class ValidationError(Exception):
    """
    Exception raised when input validation fails.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


@dataclass
class Task:
    """
    Represents a single todo task.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Task title (required, 1-200 characters)
        description (Optional[str]): Task description (optional, 0-1000 characters)
        completed (bool): Completion status (default False)
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    @property
    def status_label(self) -> str:
        """
        Returns the status indicator for the task.

        Returns:
            str: "[x]" if completed, "[ ]" if not completed
        """
        return "[x]" if self.completed else "[ ]"