
import os
from colorama import init, Fore, Style
from display_title import display_rainbow_title 
from note_rest_func.rest_func import (
    loadfile,
    writefile,
    edit_task_collection,
    delete_task_collection,
    add_task_collection,
    view_task_collections,
    view_all_tasks_from_all_collections,
)




def main():
    quit = False
    # Get the directory where the script is located
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    # Build the full path to tasks.json
    TASKS_FILE = os.path.join(SCRIPT_DIR, "tasks.json")
    while not quit:



        messages=[
            "WELCOME TO to-do-y!",
            "A simple task manager that stores tasks in a JSON file. \n",
            "Enter a digit associated with the action you want to perform: \n",
            "1. View all tasks from all collections",
            "2. View task collections",
            "3. Add a new task collection",
            "4. Edit a task collection",
            "5. Delete a task collection",
            "6. Exit the program"
        ]

        for message in messages:
            print(message)

        tasks = loadfile(TASKS_FILE)
        choice = input("Your choice: ")
        print(f"You selected option {choice}")
        if choice == "1":
            view_all_tasks_from_all_collections(tasks)
        elif choice == "2":
            view_task_collections(tasks)
        elif choice == "3":
            add_task_collection(tasks)
            writefile(tasks, TASKS_FILE)  # ← Pass the path
        elif choice == "4":
            collection_name = input("Enter the name of the task collection to edit: ")
            if collection_name in tasks:
                    edit_task_collection(collection_name, tasks)
                    writefile(tasks, TASKS_FILE)  # ← Pass the path
            else:
                print("Collection not found.")
        elif choice == "5":
            collection_name = input("Enter the name of the task collection to delete: ")
            delete_task_collection(collection_name, tasks)
            writefile(tasks, TASKS_FILE)  # ← Pass the path

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
    init(autoreset=True)
    display_rainbow_title()
    main()
