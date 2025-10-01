# TASK MANAGER PROJECT
# This project combines concepts from days 1-16 to create a personal task management system

import random
import datetime
from prettytable import PrettyTable

# CLASS DEFINITION (Day 16 - OOP)
class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.datetime.now()
        self.task_id = random.randint(1000, 9999)  # Random ID for each task

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} (Priority: {self.priority})"

# TASK MANAGER CLASS (Day 16 - OOP)
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.categories = {
            "work": [],
            "personal": [],
            "shopping": [],
            "health": []
        }

    def add_task(self, task, category="personal"):
        self.tasks.append(task)
        if category in self.categories:
            self.categories[category].append(task)

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                # Remove from category if present
                for category in self.categories.values():
                    if task in category:
                        category.remove(task)
                return True
        return False

    def list_tasks(self, category=None):
        if category and category in self.categories:
            return self.categories[category]
        return self.tasks

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

# MAIN PROGRAM
def main():
    # Initialize task manager
    manager = TaskManager()
    
    # Welcome message (Day 1 - Basic Python)
    print("=" * 50)
    print("Welcome to Your Personal Task Manager!")
    print("=" * 50)

    while True:
        # Display menu (Day 3 - Conditional Statements)
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View tasks by category")
        print("4. Mark task as completed")
        print("5. Remove a task")
        print("6. View task statistics")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        # Add new task (Day 2 - Data Types)
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            
            # Priority selection (Day 3 - Conditional Statements)
            print("\nSelect priority:")
            print("1. High")
            print("2. Medium")
            print("3. Low")
            priority_choice = input("Enter priority (1-3): ")
            priority_map = {"1": "High", "2": "Medium", "3": "Low"}
            priority = priority_map.get(priority_choice, "Medium")

            # Due date input (Day 4 - Randomization)
            try:
                days = int(input("Enter days until due (1-30): "))
                due_date = datetime.datetime.now() + datetime.timedelta(days=days)
            except ValueError:
                due_date = datetime.datetime.now() + datetime.timedelta(days=7)

            # Category selection (Day 9 - Dictionaries)
            print("\nSelect category:")
            for i, category in enumerate(manager.categories.keys(), 1):
                print(f"{i}. {category.capitalize()}")
            category_choice = input("Enter category number: ")
            category_list = list(manager.categories.keys())
            category = category_list[int(category_choice) - 1] if category_choice.isdigit() and 1 <= int(category_choice) <= len(category_list) else "personal"

            # Create and add task
            new_task = Task(title, description, priority, due_date)
            manager.add_task(new_task, category)
            print(f"\nTask added successfully! Task ID: {new_task.task_id}")

        # View all tasks (Day 14 - Dictionary Operations)
        elif choice == "2":
            if not manager.tasks:
                print("\nNo tasks found!")
            else:
                table = PrettyTable()
                table.field_names = ["ID", "Title", "Priority", "Due Date", "Status"]
                for task in manager.tasks:
                    table.add_row([
                        task.task_id,
                        task.title,
                        task.priority,
                        task.due_date.strftime("%Y-%m-%d"),
                        "Completed" if task.completed else "Pending"
                    ])
                print("\nAll Tasks:")
                print(table)

        # View tasks by category (Day 9 - Dictionaries)
        elif choice == "3":
            print("\nSelect category to view:")
            for i, category in enumerate(manager.categories.keys(), 1):
                print(f"{i}. {category.capitalize()}")
            category_choice = input("Enter category number: ")
            if category_choice.isdigit() and 1 <= int(category_choice) <= len(manager.categories):
                category = list(manager.categories.keys())[int(category_choice) - 1]
                tasks = manager.list_tasks(category)
                if tasks:
                    table = PrettyTable()
                    table.field_names = ["ID", "Title", "Priority", "Due Date", "Status"]
                    for task in tasks:
                        table.add_row([
                            task.task_id,
                            task.title,
                            task.priority,
                            task.due_date.strftime("%Y-%m-%d"),
                            "Completed" if task.completed else "Pending"
                        ])
                    print(f"\nTasks in {category.capitalize()} category:")
                    print(table)
                else:
                    print(f"\nNo tasks found in {category} category!")

        # Mark task as completed (Day 6 - Functions)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            task = manager.get_task_by_id(task_id)
            if task:
                task.mark_completed()
                print(f"\nTask '{task.title}' marked as completed!")
            else:
                print("\nTask not found!")

        # Remove task (Day 8 - Functions)
        elif choice == "5":
            task_id = int(input("Enter task ID to remove: "))
            if manager.remove_task(task_id):
                print("\nTask removed successfully!")
            else:
                print("\nTask not found!")

        # View statistics (Day 5 - Loops)
        elif choice == "6":
            if not manager.tasks:
                print("\nNo tasks to analyze!")
            else:
                total_tasks = len(manager.tasks)
                completed_tasks = sum(1 for task in manager.tasks if task.completed)
                pending_tasks = total_tasks - completed_tasks
                
                # Priority distribution
                priority_count = {"High": 0, "Medium": 0, "Low": 0}
                for task in manager.tasks:
                    priority_count[task.priority] += 1

                print("\nTask Statistics:")
                print(f"Total Tasks: {total_tasks}")
                print(f"Completed: {completed_tasks}")
                print(f"Pending: {pending_tasks}")
                print("\nPriority Distribution:")
                for priority, count in priority_count.items():
                    print(f"{priority}: {count} tasks")

        # Exit program
        elif choice == "7":
            print("\nThank you for using Task Manager!")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main() 