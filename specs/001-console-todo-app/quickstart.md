# Quickstart Guide: Console Todo App

**Feature**: Console Todo App
**Date**: 2026-01-02
**Branch**: 001-console-todo-app

## Overview

This quickstart guide provides instructions for running and using the console Todo application.

## Prerequisites

- Python 3.11 or higher installed on your system
- Basic command-line knowledge

## Setup

1. Navigate to the project directory containing the source code
2. Ensure you have the following files in place:
   - `src/main.py` - Main application entry point
   - `src/models/task.py` - Task data model
   - `src/services/todo_service.py` - Business logic for task operations
   - `src/cli/menu.py` - Command-line interface

## Running the Application

1. Open your terminal/command prompt
2. Navigate to the project directory
3. Run the application using Python:
   ```bash
   python src/main.py
   ```

## Using the Application

### Main Menu Options

Once the application starts, you will see a menu with the following options:

1. **Add Task** - Create a new task
   - Enter a title for the task (required)
   - Optionally enter a description
   - The system will assign a unique ID automatically
   - Task will be marked as incomplete by default

2. **View Tasks** - Display all tasks
   - Shows all tasks with their ID, title, description, and completion status
   - Completed tasks will be marked with a checkmark or similar indicator

3. **Update Task** - Modify an existing task
   - Enter the task ID you want to update
   - Provide the new title (or press enter to keep current title)
   - Provide the new description (or press enter to keep current description)

4. **Delete Task** - Remove a task
   - Enter the task ID you want to delete
   - Confirm the deletion when prompted

5. **Mark Complete** - Mark a task as complete
   - Enter the task ID you want to mark as complete

6. **Mark Incomplete** - Mark a task as incomplete
   - Enter the task ID you want to mark as incomplete

7. **Exit** - Quit the application

### Example Usage

```
Welcome to the Todo App!
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit

Choose an option: 1
Enter task title: Buy groceries
Enter task description (optional): Get milk, bread, and eggs
Task added successfully with ID: 1

Choose an option: 2
ID: 1 | Title: Buy groceries | Status: Incomplete
Description: Get milk, bread, and eggs

Choose an option: 5
Enter task ID to mark complete: 1
Task 1 marked as complete!

Choose an option: 2
ID: 1 | Title: Buy groceries | Status: Complete ✓
Description: Get milk, bread, and eggs

Choose an option: 7
Goodbye!
```

## Troubleshooting

- If you get a "module not found" error, ensure you're running the command from the correct directory
- If the application crashes, check that you're entering valid task IDs for operations
- If you enter an invalid menu option, the application will prompt you to try again