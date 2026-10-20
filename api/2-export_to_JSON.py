#!/usr/bin/python3
"""Export employee TODO list data to JSON.

Uses what was done in 0-gather_data_from_an_API.py and exports all tasks
owned by the given employee to a JSON file named USER_ID.json.
"""
import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def export_to_json(employee_id):
    """Export the employee's TODO list to a JSON file named USER_ID.json."""
    user_url = "{}/users/{}".format(BASE_URL, employee_id)
    todos_url = "{}/todos".format(BASE_URL)

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    username = employee.get("username")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todos
    ]

    with open("{}.json".format(employee_id), "w", encoding="utf-8") as file:
        json.dump({str(employee_id): tasks}, file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee ID must be an integer.")
        sys.exit(1)

    export_to_json(employee_id)
