"""
Console Todo App - CLI Interface

This module contains the command-line interface for the todo application.
"""
from typing import Optional
from .service import TaskService
from .models import Task


class TodoCLI:
    """
    Command-line interface for the todo application.
    """
    def __init__(self, service: TaskService):
        self._service = service

    def render_menu(self) -> None:
        """
        Render the main menu options.
        """
        print("\n--- Todo App Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Toggle complete")
        print("6. Exit")
        print("---------------------")

    def render_tasks(self, tasks: list) -> None:
        """
        Render a list of tasks.

        Args:
            tasks (list): List of tasks to render
        """
        if not tasks:
            print("\nNo tasks found.")
            return

        for task in tasks:
            print(f"{task.id} {task.status_label} {task.title}")
            if task.description:
                print(f"    {task.description}")

    def render_task(self, task: Task) -> None:
        """
        Render a single task.

        Args:
            task (Task): Task to render
        """
        print(f"{task.id} {task.status_label} {task.title}")
        if task.description:
            print(f"    {task.description}")

    def render_error(self, message: str) -> None:
        """
        Render an error message.

        Args:
            message (str): Error message to render
        """
        print(f"Error: {message}")

    def render_success(self, message: str) -> None:
        """
        Render a success message.

        Args:
            message (str): Success message to render
        """
        print(f"Success: {message}")

    def add_task_handler(self) -> None:
        """
        Handle adding a new task with user prompts.
        """
        try:
            title = input("Enter task title: ").strip()
            if not title:
                self.render_error("Title cannot be empty.")
                return

            description_input = input("Enter task description (optional, press Enter to skip): ")
            description = description_input if description_input.strip() else None

            task = self._service.add_task(title, description)
            self.render_success(f"Created task #{task.id}")
        except ValueError as e:
            self.render_error(str(e))
        except Exception as e:
            self.render_error(str(e))

    def view_tasks_handler(self) -> None:
        """
        Handle viewing all tasks.
        """
        try:
            tasks = self._service.list_tasks()
            self.render_tasks(tasks)
        except Exception as e:
            self.render_error(str(e))

    def update_task_handler(self) -> None:
        """
        Handle updating an existing task.
        """
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input:
                self.render_error("Task ID cannot be empty.")
                return

            try:
                task_id = int(task_id_input)
                if task_id <= 0:
                    self.render_error("Invalid task ID. Please enter a positive number.")
                    return
            except ValueError:
                self.render_error(f"Invalid task ID. Please enter a valid number. Got: '{task_id_input}'")
                return

            # Get the current task to show existing values
            try:
                current_task = self._service.list_tasks()
                current_task_dict = {task.id: task for task in current_task}
                if task_id not in current_task_dict:
                    self.render_error(f"Task not found for ID: {task_id}")
                    return

                current = current_task_dict[task_id]
                print(f"Current title: {current.title}")
                print(f"Current description: {current.description or ''}")

                new_title = input(f"Enter new title (press Enter to keep '{current.title}'): ")
                new_description = input(f"Enter new description (press Enter to keep '{current.description or ''}'): ")

                # Use current values if user pressed Enter without typing anything
                title_to_update = new_title if new_title.strip() else current.title
                description_to_update = new_description if new_description.strip() else current.description

                # Handle empty string case for description specifically
                if new_description == '':
                    description_to_update = current.description

                updated_task = self._service.update_task(task_id, title_to_update, description_to_update)
                self.render_success(f"Updated task #{updated_task.id}")
            except Exception as e:
                self.render_error(str(e))
        except Exception as e:
            self.render_error(str(e))

    def delete_task_handler(self) -> None:
        """
        Handle deleting a task.
        """
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input:
                self.render_error("Task ID cannot be empty.")
                return

            try:
                task_id = int(task_id_input)
                if task_id <= 0:
                    self.render_error("Invalid task ID. Please enter a positive number.")
                    return

                deleted_task = self._service.delete_task(task_id)
                self.render_success(f"Deleted task #{deleted_task.id}")
            except ValueError:
                self.render_error(f"Invalid task ID. Please enter a valid number. Got: '{task_id_input}'")
            except Exception as e:
                self.render_error(str(e))
        except Exception as e:
            self.render_error(str(e))

    def toggle_complete_handler(self) -> None:
        """
        Handle toggling a task's completion status.
        """
        try:
            task_id_input = input("Enter task ID to toggle: ").strip()
            if not task_id_input:
                self.render_error("Task ID cannot be empty.")
                return

            try:
                task_id = int(task_id_input)
                if task_id <= 0:
                    self.render_error("Invalid task ID. Please enter a positive number.")
                    return

                toggled_task = self._service.toggle_complete(task_id)
                status = "complete" if toggled_task.completed else "incomplete"
                self.render_success(f"Task #{toggled_task.id} marked {status}")
            except ValueError:
                self.render_error(f"Invalid task ID. Please enter a valid number. Got: '{task_id_input}'")
            except Exception as e:
                self.render_error(str(e))
        except Exception as e:
            self.render_error(str(e))

    def run(self) -> None:
        """
        Run the main application loop.
        """
        while True:
            try:
                self.render_menu()
                choice = input("Enter your choice (1-6): ").strip()

                if choice == "1":
                    self.add_task_handler()
                elif choice == "2":
                    self.view_tasks_handler()
                elif choice == "3":
                    self.update_task_handler()
                elif choice == "4":
                    self.delete_task_handler()
                elif choice == "5":
                    self.toggle_complete_handler()
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select 1–6.")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                self.render_error(f"An unexpected error occurred: {str(e)}")
                print("Please try again or exit the application.")