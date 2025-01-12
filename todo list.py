tasks = []

def add_task(title, description):
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} - {task['description']} [{status}]")

def mark_task_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

# Main Menu
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter task number to mark complete: ")) - 1
        mark_task_completed(index)
    elif choice == "4":
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")