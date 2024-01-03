#!/usr/bin/python3
"""Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()

    data_to_export = {user_id: []}

    for todo in todos:
        task_info = {
                "task": todo.get("title")
                "completed": todo.get("completed"),
                "username": username
        }
        data_to_export[user_id]append(task_info)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
