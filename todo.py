tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
    else:
        print("\n=== To-Do List ===")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['title']}")


def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    print("Task added.")


def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nOptions:")
        print("1) Show tasks")
        print("2) Add task")
        print("3) Mark task done")
        print("4) Delete task")
        print("5) Quit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
