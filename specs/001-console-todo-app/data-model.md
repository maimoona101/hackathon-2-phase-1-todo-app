# Data Model: Console Todo App

**Feature**: Console Todo App
**Date**: 2026-01-02
**Branch**: 001-console-todo-app

## Overview

This document defines the data models for the console Todo application based on the feature specification.

## Entity: Task

### Properties
- **id** (integer/string): Unique identifier assigned automatically when task is created
- **title** (string): Required title of the task (cannot be empty)
- **description** (string): Optional description of the task (can be empty/null)
- **status** (boolean): Completion status of the task (true = complete, false = incomplete)

### Validation Rules
- ID must be unique within the task collection
- Title must be provided and non-empty
- Title must not exceed 500 characters
- Status must be boolean (true/false only)

### State Transitions
- Status can transition from `false` (incomplete) to `true` (complete)
- Status can transition from `true` (complete) to `false` (incomplete)

## Entity: Task List

### Properties
- **tasks** (dictionary): Collection of Task entities keyed by their unique ID
- **next_id** (integer): Counter for generating next unique ID

### Operations
- **add_task(title, description)**: Creates a new Task with unique ID and adds to collection
- **get_all_tasks()**: Returns all tasks in the collection
- **get_task_by_id(id)**: Returns specific task by ID or null if not found
- **update_task(id, title, description)**: Updates existing task properties
- **delete_task(id)**: Removes task from collection
- **mark_complete(id)**: Sets task status to true
- **mark_incomplete(id)**: Sets task status to false

### Constraints
- All operations must maintain data integrity
- Task IDs must remain unique after any operation
- Operations on non-existent tasks must return appropriate error status

## Relationships

### Task List contains Tasks
- One Task List contains zero or more Tasks
- Each Task belongs to exactly one Task List
- Task List provides the container for all Task operations