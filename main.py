from database import engine, metadata_obj, get_connection
import models
from crud import create_task, get_tasks, delete_task, update_task, chenge_task_status

from datetime import datetime

metadata_obj.create_all(engine)


def add_task():
    title = input("title: ")
    description = input("description: ")
    due_date_text = input("due date (yyyy-mm-dd | hh:mm): ")

    due_date = datetime.strptime(due_date_text, "%Y-%m-%d | %H:%M")

    create_task(get_connection(), title, description=description, due_date=due_date)


def show_tasks():
    result = get_tasks(get_connection())

    for row in result:
        print(row)

def remove_task():
    task_id = int(input("task id: "))
    delete_task(get_connection(), task_id)

def edit_task():
    task_id = int(input("task id: "))

    update_task(get_connection(), task_id, title="Edited Task")

def mark_task():
    task_id = int(input("task id: "))

    chenge_task_status(get_connection(), task_id)

def main():

    while True:
        print(
            "------Menu-------\n" \
            "1. TASK yaratish\n" \
            "2. TASKlarni ko'rish\n" \
            "3. TASK yandilash\n" \
            "4. TASK o'chirish\n" \
            "5. TASK holatini o'zgartish"
        )

        choice = input("> ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            chenge_task_status()
        else:
            print("bunday menu yoq")

main()