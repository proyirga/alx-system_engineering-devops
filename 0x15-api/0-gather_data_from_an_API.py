#!/usr/bin/python3
"""
# Python script that returns information about TODO list progress.
# Requirements:
#
#   You must use urllib or requests module
#   The script must accept an integer as a parameter, which is the employee ID
#   The script must display on the standard output the employee TODO list
#       progress in this exact format:
"""
import requests
import sys


if __name__ == '__main__':

    def get_employees_todo_list(employee_id):
        url = f"https://jsonplaceholder.typicode.com/todos/{employee_id}"
        response = requests.get(url)
        todos = response.json()
        if "name" in todos[0]:
            employee_name = todos[0]["name"]
        else:
            employee_name = "Unknown"
        total_tasks = len(todos)
        done_tasks = sum(todo["completed"] for todo in todos)
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for todo in todos:
            if todo["completed"]:
                print(f"\t{todo['title']}")
