"""
CLI Menu for the Console Todo App.

This module provides the command-line interface with user menu options
for all required operations.
"""

from services.todo_service import TodoService


class TodoMenu:
    """Command-line interface for the Todo application."""

    def __init__(self):
        """Initialize the TodoMenu with a TodoService instance."""
        self.service = TodoService()
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*40)
        print("TODO APP MENU")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Mark Incomplete")
        print("7. Exit")
        print("="*40)

    def get_user_choice(self):
        """
        Get and validate user's menu choice.

        Returns:
            str: The user's choice
        """
        try:
            choice = input("Choose an option (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            return "7"

    def add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Title cannot be empty.")
            return

        description = input("Enter task description (optional): ").strip()

        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- View Tasks ---")
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print(f"Found {len(tasks)} task(s):")
        for task in tasks:
            status_icon = "✓" if task.status else "○"
            print(f"{status_icon} {task}")

            if task.description:
                print(f"   Description: {task.description}")
            print()

    def update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        task_id = self.get_task_id("update")

        if not task_id:
            return

        task = self.service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Current task: {task}")
        if task.description:
            print(f"Current description: {task.description}")

        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()

        # Use None to indicate no change, empty string to clear description
        title_to_update = new_title if new_title else None
        description_to_update = new_description if new_description != task.description else ("" if new_description == "" else None)

        if self.service.update_task(task_id, title_to_update, description_to_update):
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Error: Failed to update task {task_id}.")

    def delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        task_id = self.get_task_id("delete")

        if not task_id:
            return

        task = self.service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            if self.service.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Error: Failed to delete task {task_id}.")
        else:
            print("Deletion cancelled.")

    def mark_complete(self):
        """Handle marking a task as complete."""
        print("\n--- Mark Task Complete ---")
        task_id = self.get_task_id("mark complete")

        if not task_id:
            return

        if self.service.mark_complete(task_id):
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def mark_incomplete(self):
        """Handle marking a task as incomplete."""
        print("\n--- Mark Task Incomplete ---")
        task_id = self.get_task_id("mark incomplete")

        if not task_id:
            return

        if self.service.mark_incomplete(task_id):
            print(f"Task {task_id} marked as incomplete.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def get_task_id(self, action):
        """
        Get and validate a task ID from user input.

        Args:
            action (str): The action being performed (for error messages)

        Returns:
            int or None: The task ID if valid, None otherwise
        """
        try:
            task_id_input = input(f"Enter task ID to {action}: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return None

            task_id = int(task_id_input)
            return task_id
        except ValueError:
            print("Error: Task ID must be a number.")
            return None

    def exit_app(self):
        """Handle exiting the application."""
        print("Goodbye!")
        self.running = False

    def handle_choice(self, choice):
        """
        Handle the user's menu choice.

        Args:
            choice (str): The user's menu choice
        """
        actions = {
            "1": self.add_task,
            "2": self.view_tasks,
            "3": self.update_task,
            "4": self.delete_task,
            "5": self.mark_complete,
            "6": self.mark_incomplete,
            "7": self.exit_app
        }

        action = actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    def run(self):
        """Run the main application loop."""
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()
            self.handle_choice(choice)