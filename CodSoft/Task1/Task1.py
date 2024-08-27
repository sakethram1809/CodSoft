class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def update_task(self, task_number, new_task):
        try:
            self.tasks[task_number - 1] = new_task
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo.update_task(task_number, new_task)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()