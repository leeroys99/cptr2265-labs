
def main():
    tasks = []

    print("Task Tracker")
    print("Welcome to the Task Tracker!")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter a task name: ").strip()

            if task_name:
                tasks.append(task_name)
                print("Task added successfully!")
            else:
                print("Task name cannot be empty.")
                
                
        elif choice == "2":
            if tasks:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("No tasks have been added yet.")
                
                
                
        elif choice == "3":
            if tasks:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = input("Enter the task number to complete: ")

                if task_number.isdigit():
                    index = int(task_number) - 1

                    if 0 <= index < len(tasks):
                        completed_task = tasks.pop(index)
                        print(f"Completed task: {completed_task}")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")
            else:
                print("No tasks available to complete.")



        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("This feature will be added later.")


if __name__ == "__main__":
    main()
