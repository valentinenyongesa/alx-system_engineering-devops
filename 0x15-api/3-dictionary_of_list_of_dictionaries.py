#!/usr/bin/python3
"""Records all tasks from all employees
Format must be: { "USER_ID": [ {"username":
"USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, ... ], "USER_ID":
[ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username":
"USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""

import json
import requests


def fetch_user_data():
    """Fetch user information and to do lists"""
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    data_to_export = {}

    for user in users:
        user_id = user["id"]

        todo_response = requests.get(url + f"todos?userId={user_id}")

        todo_list = todo_response.json()

        data_to_export[user_id] = []

        for todo in todo_list:
            task_info = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
            }
            data_to_export[user_id].append(task_info)

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
