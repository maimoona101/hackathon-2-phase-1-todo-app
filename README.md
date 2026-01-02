# Console Todo App

A simple command-line based todo application that allows users to manage tasks with in-memory storage.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their IDs and completion status
- Update existing tasks by ID
- Delete tasks by ID
- Mark tasks as complete or incomplete
- In-memory storage (no files or databases)

## Requirements

- Python 3.13 or higher

## Usage

1. Run the application:
   ```bash
   python src/main.py
   ```

2. Use the menu system to interact with the application:
   - Option 1: Add a new task
   - Option 2: View all tasks
   - Option 3: Update an existing task
   - Option 4: Delete a task
   - Option 5: Mark a task as complete
   - Option 6: Mark a task as incomplete
   - Option 7: Exit the application

## Architecture

The application follows a clean architecture pattern:

- `src/main.py`: Application entry point
- `src/models/task.py`: Task data model with validation
- `src/services/todo_service.py`: Business logic layer
- `src/cli/menu.py`: Command-line interface

## Data Model

Each task has:
- ID: Unique identifier (auto-generated)
- Title: Required task title (1-500 characters)
- Description: Optional task description
- Status: Boolean indicating completion status

