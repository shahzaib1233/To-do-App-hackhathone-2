"""
Console Todo App - In-Memory Store

This module contains the in-memory storage for tasks.
"""
from typing import Dict, List, Optional
from .models import Task


class TaskStore:
    """
    In-memory storage for tasks with auto-incrementing IDs.
    """
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Create a new task with auto-incremented ID.

        Args:
            title (str): Task title
            description (Optional[str]): Task description

        Returns:
            Task: The created task with assigned ID
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks, sorted by ID in ascending order.

        Returns:
            List[Task]: List of all tasks sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda task: task.id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task's title and/or description.

        Args:
            task_id (int): ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)

        Returns:
            Optional[Task]: Updated task if found, None otherwise
        """
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return task

    def delete_task(self, task_id: int) -> Optional[Task]:
        """
        Delete a task by ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            Optional[Task]: The deleted task if found, None otherwise
        """
        if task_id not in self._tasks:
            return None

        return self._tasks.pop(task_id)

    def toggle_task(self, task_id: int) -> Optional[Task]:
        """
        Toggle a task's completion status.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]
        task.completed = not task.completed
        return task