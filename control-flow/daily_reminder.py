# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
Reminder = f"Reminder: You have a task - '{task}' with priority level '{priority}'."

# Process the task based on priority using match-case
match priority:
    case "high":
        Reminder += " This task is of high priority!"
    case "medium":
        Reminder += " This task is of medium priority."
    case "low":
        Reminder += " This task is of low priority."
    case _:
        Reminder += " Invalid priority level provided."

# Check if the task is time-bound
if time_bound == "yes":
    Reminder += " This requires immediate attention today!"
else:
    if priority == "low":
        Reminder += " Consider completing it when you have free time."

# Print the final reminder
print(Reminder)
