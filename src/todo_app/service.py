"""
Console Todo App - Service Layer

This module contains the business logic for the todo application.
"""
from typing import List, Optional
from .models import Task, TaskNotFoundError, ValidationError
from .store import TaskStore
from .validators import validate_title_required, validate_title_optional, validate_description


class TaskService:
    """
    Service layer that implements business logic for task operations.
    """
    def __init__(self, store: TaskStore):
        self._store = store

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with validation.

        Args:
            title (str): Task title (required)
            description (Optional[str]): Task description (optional)

        Returns:
            Task: The created task

        Raises:
            ValidationError: If title validation fails
        """
        validated_title = validate_title_required(title)
        validated_description = validate_description(description)
        return self._store.create_task(validated_title, validated_description)

    def list_tasks(self) -> List[Task]:
        """
        List all tasks.

        Returns:
            List[Task]: List of all tasks sorted by ID
        """
        return self._store.list_tasks()

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """
        Update a task with validation.

        Args:
            task_id (int): ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)

        Returns:
            Task: The updated task

        Raises:
            TaskNotFoundError: If task with given ID is not found
            ValidationError: If title validation fails
        """
        # Check if task exists first
        existing_task = self._store.get_task(task_id)
        if existing_task is None:
            raise TaskNotFoundError(task_id)

        # Validate inputs if provided
        validated_title = validate_title_optional(title)
        validated_description = validate_description(description)

        updated_task = self._store.update_task(task_id, validated_title, validated_description)
        if updated_task is None:
            # This shouldn't happen since we checked existence, but just in case
            raise TaskNotFoundError(task_id)

        return updated_task

    def delete_task(self, task_id: int) -> Task:
        """
        Delete a task.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            Task: The deleted task

        Raises:
            TaskNotFoundError: If task with given ID is not found
        """
        deleted_task = self._store.delete_task(task_id)
        if deleted_task is None:
            raise TaskNotFoundError(task_id)

        return deleted_task

    def toggle_complete(self, task_id: int) -> Task:
        """
        Toggle a task's completion status.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            Task: The updated task

        Raises:
            TaskNotFoundError: If task with given ID is not found
        """
        toggled_task = self._store.toggle_task(task_id)
        if toggled_task is None:
            raise TaskNotFoundError(task_id)

        return toggled_task