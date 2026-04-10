from datetime import datetime
import json
from tabulate import tabulate
from storage import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "created_at": str(datetime.now()),
        "updated_at": str(datetime.now()),
        "status": "pending"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {new_task['description']}")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task.get("status") == filter_status]
    if not tasks:
        print("No tasks found")
        return
    table_data = [[task['id'], task['description'], task['created_at'], task['updated_at'], task['status']] for task in tasks]
    headers = ["ID", "Description", "Created At", "Updated At", "Status"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def mark_done(task_id):
    tasks = load_tasks()
    try:
        task_id = int(task_id)
    except ValueError:
        print("Invalid task ID")
        return
    
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task_found = True
            print(f"Task with ID {task_id} marked as done")
    save_tasks(tasks)
    
    if not task_found:
        print("Task not found")

def mark_in_progress(task_id):
    tasks = load_tasks()
    try:
        task_id = int(task_id)
    except ValueError:
        print("Invalid task ID")
        return
    
    task_found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task_found = True
            print(f"Task with ID {task_id} marked as in-progress")
    save_tasks(tasks)
    
    if not task_found:
        print("Task not found")
        
def delete_task(task_id):
    tasks = load_tasks()
    try:
        task_id = int(task_id)
    except ValueError:
        print("Invalid task ID")
        return
    
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Task with ID {task_id} deleted")
    save_tasks(tasks)