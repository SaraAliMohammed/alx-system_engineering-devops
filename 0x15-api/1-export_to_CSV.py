#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    filename = "{}.csv".format(user_id)
    line = ""
    for todo in todos:
        line += '"{}","{}","{}","{}"\n'.\
                format(user_id, username, todo.get('completed'),
                       todo.get('title'))
    with open(filename, "w")as f:
        f.write(line)
