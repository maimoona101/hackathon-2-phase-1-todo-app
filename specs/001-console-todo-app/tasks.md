---
description: "Task list template for feature implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitutional Compliance**: All tasks must comply with constitutional principles:
- Spec-Driven Development: Tasks must be generated from written specifications
- No Manual Coding: No direct code editing allowed; only specification refinement
- Progressive Evolution: Tasks must maintain backward compatibility where specified
- Reusable Intelligence: Tasks must create reusable components across phases
- Deterministic Behavior: Tasks must produce predictable, testable results
- Clean Architecture: Tasks must maintain separation of concerns
- Reusability First: Tasks must ensure components work across all phases

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Create src directory structure: src/, src/models/, src/services/, src/cli/
- [x] T003 [P] Create main application entry point file src/main.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task data model in src/models/task.py
- [x] T005 Create Task List container in src/models/task.py
- [x] T006 Create TodoService in src/services/todo_service.py
- [x] T007 Create CLI menu structure in src/cli/menu.py
- [x] T008 Implement in-memory storage mechanism in src/services/todo_service.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with a unique ID and set status to incomplete

**Independent Test**: Can be fully tested by launching the app, selecting add task, entering a title and description, and verifying that the task appears in the list with a unique ID and incomplete status.

### Implementation for User Story 1

- [x] T009 [P] [US1] Implement Task class with id, title, description, status properties in src/models/task.py
- [x] T010 [P] [US1] Implement validation rules for Task creation in src/models/task.py
- [x] T011 [US1] Implement add_task method in TodoService to create tasks with unique IDs in src/services/todo_service.py
- [x] T012 [US1] Implement CLI function for adding tasks in src/cli/menu.py
- [x] T013 [US1] Add user input validation for add task functionality in src/cli/menu.py
- [x] T014 [US1] Test add task functionality by creating tasks with titles and descriptions

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Enable users to see all their tasks with their IDs and completion status

**Independent Test**: Can be fully tested by adding several tasks, then selecting the view option, and verifying that all tasks are displayed with their IDs, titles, status, and descriptions.

### Implementation for User Story 2

- [x] T015 [P] [US2] Implement get_all_tasks method in TodoService in src/services/todo_service.py
- [x] T016 [P] [US2] Implement get_task_by_id method in TodoService in src/services/todo_service.py
- [x] T017 [US2] Implement CLI function for viewing tasks in src/cli/menu.py
- [x] T018 [US2] Format task display with ID, title, status, and description in src/cli/menu.py
- [x] T019 [US2] Handle empty task list case with appropriate message in src/cli/menu.py
- [x] T020 [US2] Test view tasks functionality with multiple tasks and empty list

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task by ID (Priority: P2)

**Goal**: Enable users to modify an existing task's details by providing the task ID

**Independent Test**: Can be fully tested by adding a task, selecting the update option, providing the correct ID and new details, and verifying that the task is updated while others remain unchanged.

### Implementation for User Story 3

- [x] T021 [P] [US3] Implement update_task method in TodoService in src/services/todo_service.py
- [x] T022 [P] [US3] Add validation for updating task details in src/services/todo_service.py
- [x] T023 [US3] Implement CLI function for updating tasks in src/cli/menu.py
- [x] T024 [US3] Handle invalid task ID case for update operation in src/cli/menu.py
- [x] T025 [US3] Test update functionality by modifying task title and description

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Enable users to update the completion status of a task by providing the task ID

**Independent Test**: Can be fully tested by adding a task, selecting the mark complete option with the task ID, and verifying that the task status changes to complete.

### Implementation for User Story 4

- [x] T026 [P] [US4] Implement mark_complete method in TodoService in src/services/todo_service.py
- [x] T027 [P] [US4] Implement mark_incomplete method in TodoService in src/services/todo_service.py
- [x] T028 [US4] Implement CLI function for marking tasks complete in src/cli/menu.py
- [x] T029 [US4] Implement CLI function for marking tasks incomplete in src/cli/menu.py
- [x] T030 [US4] Test status change functionality by toggling task completion status

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task by ID (Priority: P3)

**Goal**: Enable users to remove a task from their list by providing the task ID

**Independent Test**: Can be fully tested by adding a task, selecting the delete option with the correct ID, and verifying that the task is removed while others remain.

### Implementation for User Story 5

- [x] T031 [P] [US5] Implement delete_task method in TodoService in src/services/todo_service.py
- [x] T032 [P] [US5] Add validation for delete operation in src/services/todo_service.py
- [x] T033 [US5] Implement CLI function for deleting tasks in src/cli/menu.py
- [x] T034 [US5] Handle invalid task ID case for delete operation in src/cli/menu.py
- [x] T035 [US5] Test delete functionality by removing tasks and verifying others remain

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T036 [P] Add main menu interface in src/main.py
- [x] T037 [P] Add error handling for all operations in src/cli/menu.py
- [x] T038 Add input validation across all user inputs in src/cli/menu.py
- [x] T039 [P] Add edge case handling for invalid IDs in src/services/todo_service.py
- [x] T040 Add user feedback messages for all operations in src/cli/menu.py
- [x] T041 Run quickstart validation to ensure all functionality works together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before CLI interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify requirements from spec.md are met with each task
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence