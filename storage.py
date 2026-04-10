import os
import json

File_name = "tasks.json"

def load_tasks():
    if not os.path.exists(File_name):
        return []

    with open(File_name, "r") as file:
        try:
            tasks = json.load(file)
            return tasks
        except json.JSONDecodeError:
            return []
def save_tasks(tasks):
    with open(File_name, "w") as file:
        json.dump(tasks, file, indent=4)