
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

        if choice == "4":
            print("Goodbye!")
            break
        else:
            print("This feature will be added later.")


if __name__ == "__main__":
    main()
