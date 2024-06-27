class ToDoApp:
    tasks = []

    def add_task():
        task = input("Enter a task: ")
        if task:
            ToDoApp.tasks.append(task)
            print(f"Task {task} is added successfully.")
        else:
            print("You must enter a task.")

    def remove_task():
        add_task()
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if task_index < len(ToDoApp.tasks):
                ToDoApp.tasks.pop(task_index)
                print(f"Task {tasks[task_index]} is removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def mark_complete():
        try:
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            if task_index < len(ToDoApp.tasks):
                ToDoApp.tasks[task_index]["completed"] = True
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def clear_all():
        if input("Do you really want to clear all tasks? (yes/no): ").lower() == "yes":
            ToDoApp.tasks = []
            print("All tasks cleared.")
        else:
            print("Tasks not cleared.")

    def display_tasks():
        for i, task in enumerate(ToDoApp.tasks, 1):
            status = " - Completed" if task["completed"] else ""
            print(f"{i}. {task['task']}{status}")

    def run():
        while True:
            print("\n")
            print("1. Add task")
            print("2. Remove task")
            print("3. Mark task as complete")
            print("4. Clear all tasks")
            print("5. Display tasks")
            print("6. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                ToDoApp.add_task()
            elif choice == "2":
                ToDoApp.remove_task()
            elif choice == "3":
                ToDoApp.mark_complete()
            elif choice == "4":
                ToDoApp.clear_all()
            elif choice == "5":
                ToDoApp.display_tasks()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    ToDoApp.run()