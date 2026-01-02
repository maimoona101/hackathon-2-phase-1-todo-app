"""
Task model for the Console Todo App.

This module defines the Task data model with properties, validation rules,
and state transition capabilities as specified in the data model.
"""

class Task:
    """Represents a single todo item with ID, title, description, and completion status."""

    def __init__(self, task_id, title, description="", status=False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Required title of the task
            description (str, optional): Optional description of the task
            status (bool, optional): Completion status (default: False)

        Raises:
            ValueError: If title is empty or exceeds 500 characters
        """
        self.id = task_id
        self.title = self._validate_title(title)
        self.description = description
        self.status = status  # False = incomplete, True = complete

    def _validate_title(self, title):
        """
        Validate the task title according to the specification.

        Args:
            title (str): The title to validate

        Returns:
            str: The validated title

        Raises:
            ValueError: If title is invalid
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        if len(title) > 500:
            raise ValueError("Title must not exceed 500 characters")

        return title.strip()

    def update_details(self, title=None, description=None):
        """
        Update the task details.

        Args:
            title (str, optional): New title for the task
            description (str, optional): New description for the task
        """
        if title is not None:
            self.title = self._validate_title(title)

        if description is not None:
            self.description = description

    def mark_complete(self):
        """Mark the task as complete."""
        self.status = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.status = False

    def to_dict(self):
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

    def __str__(self):
        """String representation of the task."""
        status_str = "Complete" if self.status else "Incomplete"
        return f"ID: {self.id} | Title: {self.title} | Status: {status_str}"

    def __repr__(self):
        """Developer-friendly representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', status={self.status})"