"""
To-Do List Manager
-------------------
A simple text-based To-Do List application.

Features:
- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks
- Input validation
"""

# List to store tasks
# Each task will be stored as a dictionary:
# {"title": "Task name", "completed": False}
tasks = []


def display_menu():
    """Displays the main menu options."""
    print("\n====== TO-DO LIST MANAGER ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    """Adds a new task to the list."""
    title = input("Enter task name: ").strip()

    if title == "":
        print("⚠ Task name cannot be empty.")
        return

    task = {"title": title, "completed": False}
    tasks.append(task)
    print(f"✅ Task '{title}' added successfully!")


def view_tasks():
    """Displays all tasks."""
    if not tasks:
        print("📌 No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "✘ Pending"
        print(f"{index}. {task['title']} [{status}]")


def mark_task_completed():
    """Marks a selected task as completed."""
    if not tasks:
        print("📌 No tasks available to mark.")
        return

    view_tasks()

    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print("🎉 Task marked as completed!")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")


def delete_task():
    """Deletes a selected task."""
    if not tasks:
        print("📌 No tasks available to delete.")
        return

    view_tasks()

    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"🗑 Task '{removed_task['title']}' deleted successfully!")
        else:
            print("⚠ Invalid task number.")
    except ValueError:
        print("⚠ Please enter a valid number.")


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please select a number between 1 and 5.")


# Entry point of the program
if __name__ == "__main__":
    main()