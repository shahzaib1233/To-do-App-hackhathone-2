"""
Console Todo App - Main Entry Point

This module serves as the entry point for the console todo application.
"""
from .store import TaskStore
from .service import TaskService
from .cli import TodoCLI


def main():
    """
    Main entry point for the console todo application.
    Initializes all components and starts the CLI loop.
    """
    # Initialize the in-memory store
    store = TaskStore()

    # Initialize the service layer with the store
    service = TaskService(store=store)

    # Initialize the CLI with the service
    cli = TodoCLI(service=service)

    # Start the main application loop
    cli.run()


if __name__ == "__main__":
    main()