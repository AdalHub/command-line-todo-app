
import json
from colorama import init, Fore, Style
import os

# Initialize colorama for cross-platform support
init(autoreset=True)

def loadfile(TASKS_FILE):
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
            return tasks
    else:
        tasks = {}
    return tasks

def writefile(tasks, filepath):
    try:
        with open(filepath, "w") as file:
            json.dump(tasks, file, indent=2)  # indent for readability
    except Exception as e: 
        print(f"An error occurred while writing to the file: {e}")
        return False
    return True

def edit_task_collection(collection_name, tasks):
    print("Currently editing task collection:", collection_name)
    print("Tasks in this collection:")
    for idx, task in enumerate(tasks[collection_name], start=1):
        print(f"{idx}. {task}")
    action = input("Do you want to add or remove a task? (add/remove): ")
    if action == "add":
        new_task = input("Enter the new task: ")
        tasks[collection_name].append(new_task)
        print(f"Task '{new_task}' added to collection '{collection_name}'.")
    elif action == "remove":
        task_num = int(input("Enter the number of the task to remove: "))
        if 1<=task_num <=len(tasks[collection_name]):
            removed_task= tasks[collection_name].pop(task_num-1)
            print(f"Task '{removed_task}' removed from collection '{collection_name}'.")
        else:
            print("Invalid task number.")
    else:
        print("Invalid action.")

def delete_task_collection(collection_name, tasks):
    if collection_name in tasks:
        del tasks[collection_name]
        print(f"Task collection '{collection_name}' deleted.")
    else:
        print("Collection not found.")

def add_task_collection(tasks):
    new_collection_name = input("Enter the name of the new task collection: ")
    tasks[new_collection_name] = []
    print(f"Task collection '{new_collection_name}' added.")

def view_task_collections(tasks):
    print("Task Collections:")
    for collection in tasks:
        print(f"- {collection}")
def view_all_tasks_from_all_collections(tasks):
    print("All Tasks from All Collections:")
    for collection in tasks:
        print(f"Collection: {collection}")
        for task in tasks[collection]:
            print(f" - {task}")
