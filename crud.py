from datetime import datetime
from sqlalchemy import(
    Connection,
    insert,select,update,delete
)

from models import tasks

def create_task(
    conn:Connection,
    title:str,
    description:str | None = None,due_date:datetime | None = None
    ):
    try:
        query = insert(tasks).values(
            title = title,
            description=description,
            due_date=due_date
        )

        conn.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

def get_tasks(conn:Connection):
    result = []
    try:
        query = select(tasks)

        result = conn.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

    return result