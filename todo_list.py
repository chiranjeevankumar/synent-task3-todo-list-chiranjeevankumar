
tasks = []

while True:
    print("\n To-Do List ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")

