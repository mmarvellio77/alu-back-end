#!/usr/bin/python3
"""Gather data from an API.

Fetches an employee's TODO list progress from the JSONPlaceholder API
using the requests module, then prints it in a specific format.
"""
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def gather_data_for_employee(employee_id):
    """Return the employee's name, completed tasks and total task count."""
    user_url = "{}/users/{}".format(BASE_URL, employee_id)
    todos_url = "{}/todos".format(BASE_URL)

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    name = employee.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    return name, done_tasks, total_tasks


def display_todo_progress(employee_id):
    """Display the employee TODO list progress on standard output."""
    name, done_tasks, total_tasks = gather_data_for_employee(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee ID must be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)
