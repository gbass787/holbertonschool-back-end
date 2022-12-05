#!/usr/bin/python3
"""return information employee TODO list progress from an REST API"""
from requests import get
from sys import argv


def get_api():
    """Gather data from an API"""
    emp_id = int(argv[1])
    emp_name = ''
    tasks_done = 0
    tasks_total = 0
    tasks_titles = []

    users_res = get('https://jsonplaceholder.typicode.com/users').json()
    for user in users_res:
        if user['id'] == emp_id:
            emp_name = user['name']
            break

    tasks_res = get('https://jsonplaceholder.typicode.com/todos').json()
    for task in tasks_res:
        if task['userId'] == emp_id:
            if task['completed']:
                tasks_titles.append(task['title'])
                tasks_done += 1
            tasks_total += 1

    print('Employee {} is done with tasks({}/{}):'.format(emp_name,
                                                          tasks_done,
                                                          tasks_total))
    for title in tasks_titles:
        print('\t {}'.format(title))


if __name__ == '__main__':
    get_api()
