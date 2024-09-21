#Prompt for a Single Task:
task = input("Enter your task")
priority = input("Priority (high, medium, low)")
time_bound = input("is time-bound? (yes or no)")

# Initialize the reminder and Note message
reminder_message = f"Reminder: You have a task - '{task}' with priority level '{priority}'."
Note = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder_message += " This task is of high priority!"
    case "medium":
        reminder_message += " This task is of medium priority."
    case "low":
        reminder_message += " This task is of low priority."
    case _:
        reminder_message += " Invalid priority level provided."

# Check if the task is time-bound
        if time_bound == "yes":
            reminder_message += " This requires immediate attention today!"

# Print the final reminder
        print(reminder_message)

        else:
        print(Note)
