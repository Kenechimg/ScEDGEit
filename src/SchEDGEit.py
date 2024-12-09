import json
from datetime import datetime

# This class represents a single task
class Task:
    def __init__(self, description, date, priority, completed=False):
        """
        Initialize a Task instance.
        :param description: Task description.
        :param date: Task due date (in YYYY-MM-DD format).
        :param priority: Task priority (1 for high, 3 for low).
        :param completed: Whether the task is completed (default is False).
        """
        self.description = description
        self.date = date
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert Task instance to dictionary for JSON serialization."""
        return {
            "description": self.description,
            "date": self.date,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        """Create a Task instance from a dictionary."""
        return Task(
            description=data["description"],
            date=data["date"],
            priority=data["priority"],
            completed=data["completed"]
        )

    def __str__(self):
        """
        Provide a string representation of the task.
        Example: "Task Description (Due: 2024-01-01, Priority: 1) - Completed/Pending"
        """
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} (Due: {self.date}, Priority: {self.priority}) - {status}"


# This class represents a to-do list
class ToDoList:
    def __init__(self, data_file="tasks.json"):
        """
        Initialize a ToDoList instance.
        :param data_file: File to store task data (default is tasks.json).
        """
        self.tasks = []  # List to store Task instances
        self.data_file = data_file  # File path for task persistence
        self.load_tasks()  # Loads existing tasks from the file

    def add_task(self, description, date, priority):
        """
        Add a new task to the to-do list.
        :param description: Task description.
        :param date: Task due date (YYYY-MM-DD format).
        :param priority: Task priority (1 for high, 3 for low).
        """
        task = Task(description, date, priority)
        self.tasks.append(task)
        self.save_tasks()  # Saves updated task list to file
        print(f"Task '{description}' added.")

    def delete_task(self, description):
        """
        Delete a task from the to-do list by description.
        :param description: Description of the task to delete.
        """
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                self.save_tasks()  # Saves updated task list to file
                print(f"Task '{description}' deleted.")
                return
        print("Task not found.")  # Prints error if task not found

    def complete_task(self, description):
        """
        Mark a task as completed by description.
        :param description: Description of the task to mark as completed.
        """
        for task in self.tasks:
            if task.description == description:
                task.mark_complete()
                self.save_tasks()  # Saves updated task list to file
                print(f"Task '{description}' marked as complete.")
                return
        print("Task not found.")  # Prints error if task not found

    def view_tasks(self, sort_by="priority"):
        """
        Display tasks, optionally sorted by priority or due date.
        :param sort_by: Sorting key ('priority' or 'date').
        """
        if sort_by == "priority":
            sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
        elif sort_by == "date":
            sorted_tasks = sorted(self.tasks, key=lambda x: datetime.strptime(x.date, "%Y-%m-%d"))
        else:
            sorted_tasks = self.tasks 
        print("\nCurrent Tasks:")
        for task in sorted_tasks:
            print(task)  # Uses __str__ method of Task class to print details
        print()

    def save_tasks(self):
        """Save the current list of tasks to a JSON file."""
        with open(self.data_file, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open(self.data_file, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks_data]
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No existing tasks found. Starting with an empty to-do list.")
        except json.JSONDecodeError:
            print("Error loading tasks. Starting with an empty to-do list.")


def main():
    """
    Main program loop for interacting with the to-do list application.
    """
    todo_list = ToDoList()  # Creates a new to-do list instance

    while True:
        # This displays the menu
        print("\n--- SchEDGEit Menu ---")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")

        # This gets the user's choice
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new task
            description = input("Enter task name/description: ")
            date = input("Enter task due date (YYYY-MM-DD): ")
            priority = int(input("Enter task priority (1 for high, 3 for low): "))
            todo_list.add_task(description, date, priority)

        elif choice == "2":
            # Views tasks
            sort_by = input("Sort tasks by 'priority' or 'date': ")
            todo_list.view_tasks(sort_by)

        elif choice == "3":
            # Marks a task as complete
            description = input("Enter task name/description to mark as complete: ")
            todo_list.complete_task(description)

        elif choice == "4":
            # Deletes a task
            description = input("Enter task name/description to delete: ")
            todo_list.delete_task(description)

        elif choice == "5":
            # Exits the program
            print("Exiting the program.")
            break

        else:
            # Invalid input
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
