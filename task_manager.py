import csv
from collections import deque

class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self, file_path="tasks.csv"):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    title, description, status = row
                    self.tasks.append(Task(title, description, status))
        except FileNotFoundError:
            print("No tasks found.")
            pass

    def save_tasks(self):
        with open(self.file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Description", "Status"])
            for task in self.tasks:
                writer.writerow([task.title, task.description, task.status])

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task.title}' added.")

    def complete_task(self):
        task = self.tasks.pop()
        task.status = "Completed"
        self.save_tasks()
        print(f"Task '{task.title}' marked as completed.")

manager = TaskManager()
manager.add_task(Task("Adobe Photoshop", "Learn how to use Photoshop"))
manager.add_task(Task("Logic Pro x", "Learn how to use Logic Pro x"))
manager.add_task(Task("Adobe illustrator", "Learn how to use Adobe Illustrator"))
manager.complete_task()
