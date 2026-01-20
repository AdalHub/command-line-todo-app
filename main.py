

import json
import os

def loadfile():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    else:
        tasks = []
    return tasks

def writefile(tasks):
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
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
def main():
    quit = False
    while not quit:



        messages=[
            "WELCOME TO file-based-task-manager!",
            "This is a simple task manager that stores tasks in a file.",
            "Enter a digit associated with the action you want to perform:",
            "1. View all tasks from all collections",
            "2. View task collections",
            "3. Add a new task collection",
            "4. Edit a task collection",
            "5. Delete a task collection",
            "6. Exit the program"
        ]

        for message in messages:
            print(message)

        tasks = loadfile()

        choice = input("Your choice: ")
        print(f"You selected option {choice}")
        if choice == "1":
            view_all_tasks_from_all_collections(tasks)
        elif choice == "2":
            view_task_collections(tasks)
        elif choice == "3":
            add_task_collection(tasks)
            writefile(tasks)
        elif choice == "4":
            collection_name = input("Enter the name of the task collection to edit: ")
            if collection_name in tasks:
                edit_task_collection(collection_name, tasks)
                writefile(tasks)
            else:
                print("Collection not found.")
        elif choice == "5":
            collection_name = input("Enter the name of the task collection to delete: ")
            delete_task_collection(collection_name, tasks)
            writefile(tasks)
        elif choice == "6":
            quit = True
            print("Exiting the task manager. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

        cont = input("Do you want to perform another action? (y/n): ")
        if cont.lower() != 'y':
            quit = True
            print("Exiting the task manager. Goodbye!")
if __name__ == "__main__":
    main()
