

import json
import os

def loadfile():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            print(tasks)
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
def main():
    quit = False
    while not quit:
        messages=[
            "WELCOME TO file-based-task-manager!",
            "This is a simple task manager that stores tasks in a file.",
            "Enter a digit associated with the action you want to perform:",
            "1. Add a task",
            "2. View tasks",
            "3. Remove a task"
        ]
        for message in messages:
            print(message)

        tasks = loadfile()
        print("current tasks:", tasks)
        choice = input("Your choice: ")
        print(f"You selected option {choice}")

        if choice == "1":
            task = input("Please enter the task you want to add: ")
            tasks.append(task)
            writefile(tasks)
            print(f"Task '{task}' added.")
        elif choice == "2":
            if tasks:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks found.")
        elif choice == "3":
            if tasks:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start = 1):
                    print(f"{idx}. {task}")
                task_num = int(input("Enter the number of the task you want to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    writefile(tasks)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to remove.")
        else:
            print("Invalid choice. Please select a valid option.")
        cont = input("Do you want to perform another action? (y/n): ")
        if cont.lower() != 'y':
            quit = True
            print("Exiting the task manager. Goodbye!")
if __name__ == "__main__":
    main()
