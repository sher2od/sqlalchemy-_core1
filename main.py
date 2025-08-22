from database import engine,metadata_odj,get_connection
import models
from crud import create_task,get_tasks

from datetime import datetime
metadata_odj.create_all(engine)

def add_tasks():
    title = input("title: ")
    description = input("description ")
    due_date_text = input("due date (yyyy-mm-dd): ")

    due_date = datetime.strptime(due_date_text, "%Y-%m-%d | %H:%M")

    create_task(get_connection(),title,description=description,due_date=due_date)


def show_tasks():
    result = get_tasks(get_connection())

    for row in result:
        print(row)

