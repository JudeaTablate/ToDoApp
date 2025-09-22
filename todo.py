# toDoApp.py
# A simple to-do list application

tasks = []

def add_task(task=None):
    """Add a task to the global tasks list.
    If `task` is None, prompt the user for input.
    """
    if task is None:
        task = input("Enter task: ").strip()
    else:
        task = str(task).strip()

    if not task:
        print("Task cannot be blank.")
        return

    tasks.append(task)
    print(f"Task added: '{task}'")


def show_tasks():
    """Display all tasks with numbering."""
    if not tasks:
        print("There are no existing tasks.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task(tasknumber=None):
    """Remove a task by number.
    If `tasknumber` is None, prompt the user for which task to remove.
    `tasknumber` is treated as 1-based.
    """
    if not tasks:
        print("No existing tasks.")
        return

    if tasknumber is None:
        show_tasks()
        try:
            num = int(input("Enter task number to remove: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            return

        if 1 <= num <= len(tasks):
            confirm = input(f"Delete '{tasks[num-1]}'? (y/n): ").strip().lower()
            if confirm == "y":
                removed = tasks.pop(num-1)
                print(f"Removed: {removed}")
            else:
                print("Cancelled.")
        else:
            print("Task number is invalid.")
    else:
        try:
            num = int(tasknumber)
        except Exception:
            print("Invalid task number argument.")
            return

        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Task number is invalid.")


def main():
    """Main menu loop."""
    while True:
        print("\n+------------------+")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("+------------------+")
        ch = input("Enter choice: ").strip()

        if ch == "1":
            t = input("Enter task: ").strip()
