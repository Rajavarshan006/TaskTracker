# TaskTracker

A simple and efficient **Command Line Interface (CLI) task manager** built using Python. This project demonstrates core backend concepts such as command parsing, file-based persistence, and CRUD operations using a modular architecture.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Architecture Overview](#architecture-overview)
- [CRUD Operations](#crud-operations)
- [File-Based Persistence](#file-based-persistence)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

**TaskTracker** is a lightweight, terminal-based task management tool that lets you create, view, update, and delete tasks directly from the command line — no GUI, no database setup required.

It was built to showcase fundamental backend engineering principles:

- **Command parsing** — reads and interprets CLI arguments via `sys.argv`
- **CRUD operations** — full Create, Read, Update, Delete support for tasks
- **File-based persistence** — tasks are stored in a local `tasks.json` file
- **Modular architecture** — functionality is cleanly split across dedicated modules

---

## Features

- ✅ Add new tasks with a description
- 📋 List all tasks or filter by status (`pending`, `in-progress`, `done`)
- ✏️ Mark tasks as **in-progress** or **done**
- 🗑️ Delete tasks by ID
- 💾 Persistent storage using a local JSON file — no database required
- 📊 Nicely formatted table output using `tabulate`
- 🧩 Modular, readable codebase — easy to extend

---

## Technology Stack

| Component        | Technology          |
|------------------|---------------------|
| Language         | Python 3            |
| Data Storage     | JSON (flat file)    |
| Table Formatting | `tabulate`          |
| CLI Parsing      | `sys.argv` (stdlib) |
| Date/Time        | `datetime` (stdlib) |

---

## Prerequisites

- Python **3.6+** installed on your system
- `pip` (Python package manager)

Verify your Python installation:

```bash
python --version
```

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Rajavarshan006/TaskTracker.git
   cd TaskTracker
   ```

2. **Install dependencies:**

   ```bash
   pip install tabulate
   ```

   > No virtual environment is required, but one is recommended for clean dependency management:
   > ```bash
   > python -m venv venv
   > source venv/bin/activate   # On Windows: venv\Scripts\activate
   > pip install tabulate
   > ```

3. **You're ready to go!** No additional configuration is needed.

---

## Usage Guide

All commands are run using:

```bash
python main.py <command> [arguments]
```

### Available Commands

| Command                          | Description                              |
|----------------------------------|------------------------------------------|
| `add <description>`              | Add a new task                           |
| `list`                           | List all tasks                           |
| `list <status>`                  | List tasks filtered by status            |
| `done <id>`                      | Mark a task as done                      |
| `in-progress <id>`               | Mark a task as in-progress               |
| `delete <id>`                    | Delete a task by its ID                  |

### Examples

**Add a task:**
```bash
python main.py add "Buy groceries"
# Output: Task added: Buy groceries
```

**List all tasks:**
```bash
python main.py list
```

```
+----+------------------+---------------------+---------------------+-----------+
| ID | Description      | Created At          | Updated At          | Status    |
+====+==================+=====================+=====================+===========+
|  1 | Buy groceries    | 2026-04-10 09:00:00 | 2026-04-10 09:00:00 | pending   |
+----+------------------+---------------------+---------------------+-----------+
```

**Filter tasks by status:**
```bash
python main.py list pending
python main.py list in-progress
python main.py list done
```

**Mark a task as in-progress:**
```bash
python main.py in-progress 1
# Output: Task with ID 1 marked as in-progress
```

**Mark a task as done:**
```bash
python main.py done 1
# Output: Task with ID 1 marked as done
```

**Delete a task:**
```bash
python main.py delete 1
# Output: Task with ID 1 deleted
```

---

## Project Structure

```
TaskTracker/
├── main.py          # Entry point — parses CLI arguments and dispatches commands
├── operations.py    # Business logic — CRUD operations for tasks
├── storage.py       # Persistence layer — load/save tasks to JSON
├── tasks.json       # Auto-generated data file (created on first task add)
└── README.md        # Project documentation
```

---

## Architecture Overview

TaskTracker follows a simple **three-layer architecture**:

```
┌─────────────────────────────────┐
│         main.py                 │
│  (CLI layer — command parsing)  │
└──────────────┬──────────────────┘
               │
┌──────────────▼──────────────────┐
│        operations.py            │
│  (Logic layer — CRUD functions) │
└──────────────┬──────────────────┘
               │
┌──────────────▼──────────────────┐
│         storage.py              │
│  (Data layer — JSON read/write) │
└─────────────────────────────────┘
```

- **`main.py`** — Reads `sys.argv`, identifies the command, validates input, and calls the appropriate function in `operations.py`.
- **`operations.py`** — Contains all business logic: adding, listing, updating status, and deleting tasks. Delegates storage to `storage.py`.
- **`storage.py`** — Handles all file I/O, reading from and writing to `tasks.json`.

---

## CRUD Operations

| Operation | Command             | Function               | Description                            |
|-----------|---------------------|------------------------|----------------------------------------|
| Create    | `add <description>` | `add_task()`           | Creates a new task with a unique ID    |
| Read      | `list [status]`     | `list_tasks()`         | Retrieves and displays all tasks       |
| Update    | `done <id>`         | `mark_done()`          | Updates task status to `done`          |
| Update    | `in-progress <id>`  | `mark_in_progress()`   | Updates task status to `in-progress`   |
| Delete    | `delete <id>`       | `delete_task()`        | Removes a task by its ID               |

Each task record contains:

```json
{
    "id": 1,
    "description": "Buy groceries",
    "created_at": "2026-04-10 09:00:00.000000",
    "updated_at": "2026-04-10 09:00:00.000000",
    "status": "pending"
}
```

---

## File-Based Persistence

TaskTracker stores all task data in a local **`tasks.json`** file in the project directory.

- The file is **automatically created** the first time you add a task.
- Tasks are stored as a **JSON array** of objects.
- The `storage.py` module handles all reads and writes, keeping persistence logic separate from business logic.
- If the file is missing or corrupted, the application gracefully returns an empty task list.

**Example `tasks.json`:**

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "created_at": "2026-04-10 09:00:00.000000",
        "updated_at": "2026-04-10 09:30:00.000000",
        "status": "done"
    },
    {
        "id": 2,
        "description": "Write project report",
        "created_at": "2026-04-10 10:00:00.000000",
        "updated_at": "2026-04-10 10:00:00.000000",
        "status": "in-progress"
    }
]
```

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** against the `main` branch

Please ensure your code follows the existing style and that all existing functionality continues to work.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact

**Rajavarshan**  
GitHub: [@Rajavarshan006](https://github.com/Rajavarshan006)

---

> *TaskTracker — built to make task management as simple as typing a command.*
