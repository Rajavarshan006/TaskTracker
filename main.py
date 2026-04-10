import sys
from operations import add_task, list_tasks, mark_done, delete_task, mark_in_progress

def main():
    args = sys.argv

   

    if len(args) < 2:
        print("No command provided")
        return
    
    command = args[1]

    if command == "add":
        if len(args) < 3:
            print("Please provide a task description")
            return
        description = " ".join(args[2:])
        add_task(description)

    elif command == "list":
        filter_status = args[2] if len(args) > 2 else None
        list_tasks(filter_status)

    elif command == "done":
        if len(args) < 3:
            print("Please provide a task id")
            return
        task_id = args[2]
        mark_done(task_id)
    elif command == "in-progress":
        if len(args) < 3:
            print("Please provide a task id")
            return
        task_id = args[2]
        mark_in_progress(task_id)
    

    elif command == "delete":
        if len(args) < 3:
            print("Please provide a task id")
            return
        task_id = args[2]
        delete_task(task_id)

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()