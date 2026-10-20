#!/usr/bin/python3
"""Export all employees' TODO list data to JSON.

Uses what was done in 0-gather_data_from_an_API.py and exports every task
from every employee to a JSON file named todo_all_employees.json.
"""
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def export_all_to_json():
    """Export all employees' TODO lists to todo_all_employees.json."""
    users = requests.get("{}/users".format(BASE_URL)).json()
    todos = requests.get("{}/todos".format(BASE_URL)).json()

    usernames = {user.get("id"): user.get("username") for user in users}

    all_tasks = {}
    for task in todos:
        user_id = task.get("userId")
        all_tasks.setdefault(str(user_id), []).append({
            "username": usernames.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed"),
        })

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_to_json()
