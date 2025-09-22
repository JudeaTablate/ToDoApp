# toDoApp.py

tasks=[]

def add_task():
    """_summary_

    Args:
        task (_type_): _description_
    """
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be blank.")
    else:
        tasks.append(task)
        print("Task has been added.")

def show_tasks( ):
    """_summary_
    """
    if not tasks:
        print("There are no existing tasks.")
    else:
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")

def remove_task():
    """_summary_

    Args:
        tasknumber (_type_): _description_
    """
    if not tasks:
        print("No existing tasks.")
        return
    
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            confirm = input(f"Delete '{tasks[num-1]}'? (y/n): ")
            if confirm == "y" or confirm == "Y":
                remove = tasks.pop(num-1)
                print(f"Removed: {remove}")
            else:
                print("Cancelled.")
        else:
            print("Task number is invalid.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """_summary_
    """
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("Enter choice : ")
        if ch == "1": 
            add_task()
        elif ch=="2": 
            show_tasks()
        elif ch=="3": 
            remove_task()
        elif ch=="4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")
main()
