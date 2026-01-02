"""
TodoService for the Console Todo App.

This module provides the business logic for task operations including
add, view, update, delete, and status change operations.
"""

from models.task import Task


class TodoService:
    """Business logic layer for managing tasks."""

    def __init__(self):
        """Initialize the TodoService with an empty task collection."""
        self._tasks = {}  # Dictionary to store tasks with ID as key
        self._next_id = 1  # Counter for generating unique IDs

    def add_task(self, title, description=""):
        """
        Create a new task with a unique ID and add it to the collection.

        Args:
            title (str): Title of the task
            description (str, optional): Description of the task

        Returns:
            Task: The newly created task
        """
        task = Task(self._next_id, title, description, False)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self):
        """
        Get all tasks in the collection.

        Returns:
            list: List of all Task objects
        """
        return list(self._tasks.values())

    def get_task_by_id(self, task_id):
        """
        Get a specific task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id, title=None, description=None):
        """
        Update an existing task's properties.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if task was updated, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.update_details(title, description)
            return True
        return False

    def delete_task(self, task_id):
        """
        Remove a task from the collection.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task was not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def mark_complete(self, task_id):
        """
        Mark a task as complete.

        Args:
            task_id (int): ID of the task to mark complete

        Returns:
            bool: True if task was marked complete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_complete()
            return True
        return False

    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete.

        Args:
            task_id (int): ID of the task to mark incomplete

        Returns:
            bool: True if task was marked incomplete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_incomplete()
            return True
        return False

    def get_next_id(self):
        """
        Get the next available ID (for internal use).

        Returns:
            int: The next available ID
        """
        return self._next_id