#creating an empty dictionary
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def delete_task(task_index):
    if task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def mark_as_completed(task_index):
    if task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def display_tasks():
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index + 1}. {task['task']} - {status}")

while True:
    print("\n1. Add Task\n2. Delete Task\n3. Mark Task as Completed\n4. Display Tasks\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task_index = int(input("Enter task index to delete: ")) - 1
        delete_task(task_index)
    elif choice == "3":
        task_index = int(input("Enter task index to mark as completed: ")) - 1
        mark_as_completed(task_index)
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
