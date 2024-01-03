#!/usr/bin/python3
"""You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee
TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks,
which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys


def get_todo_list(employee_id):
    """
    Get the TODO list for a given employee ID from the specified REST API.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        return user_data, todo_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def display_todo_progress(employee_id, user_data, todo_data):
    """
    Display the TODO list progress for the given employee ID.
    """
    employee_name = user_data.get("name")
    completed_tasks = [task for task in todo_data if task.get("completed")]
    total_tasks = len(todo_data)

    print(f"Employee {employee_name}
          is done with tasks({len(completed_tasks)}/{total_tasks}): ")

    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = get_todo_list(employee_id)
    display_todo_progress(employee_id, user_data, todo_data)
