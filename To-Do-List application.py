class TodoApp:
    def __init__(self):
        self.tasks = []
    def display_menu(self):
        print("\n------ To-Do List Menu ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
    def add_task(self):
        task = input("Enter the task: ")
        if task:
            self.tasks.append(task)
            print(f"Task '{task}' added successfully!")
        else:
            print("Task cannot be empty. Please enter a valid task.")
    def view_tasks(self):
        if self.tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty.")
    def update_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the task number you want to update: "))
            if 1 <= task_num <= len(self.tasks):
                new_task = input("Enter the new task: ")
                if new_task:
                    self.tasks[task_num - 1] = new_task
                    print(f"Task {task_num} updated successfully!")
                else:
                    print("Updated task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    def delete_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the task number you want to delete: "))
            if 1 <= task_num <= len(self.tasks):
                deleted_task = self.tasks.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    self.update_task()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    print("Exiting the To-Do List application.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
todo_app = TodoApp()
todo_app.run()
