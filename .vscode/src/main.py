import json 
import datetime

#Welcome message
print("Hello, \n Welcome to our personal-growth-trask-tracker \n lets start progressing towards our goals below!")

#Capturing user input
option = int(input("What would you like to do? \n 1) Add Task \n 2) Update Task \n 3) Remove Tasks? \n"))

#Creating task list that will store all of our JSON tasks 
tasks = []
id = 1; 
date = datetime.datetime.now()
print(date)

if option == 1:
    print("Option was 1")
    title = input("Enter the task name: ")
    description = input("Short description of Task: ")
    status = input("Status of tasks ('todo', 'in-progress', 'done'): ")
    priority = input("Enter the priority (low, normal, or high): ")
    dueDate = input("Enter a due date in the format (month/day/year): ")
    category = input("Enter the catgory (Health, Career, Finance, School): ")
    notes = input("Enter any notes regarding this task: ")
    item = {
        "ID": id,
        "Title": title,
        "Description": description,
        "Status": status,
        "Created": date,
        "Updated": None,
        "Priority": priority,
        "Due": dueDate,
        "Category": category, 
        "Notes": notes
        }

#Convert to JSON
y = json.dumps(item, default=str)
print(y)

print(tasks)

