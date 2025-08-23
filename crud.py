from datetime import datetime
from sqlalchemy import (
    Connection, 
    insert, select, update, delete
)
from models import tasks

def create_task(
    conn: Connection, 
    title: str, 
    description: str | None = None, due_date: datetime | None = None
    ):
    try:
        query = insert(tasks).values(
            title=title,
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

def get_tasks(conn: Connection):
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

def delete_task(conn: Connection, task_id: int):
    try:
        query = delete(tasks).where(tasks.c.id == task_id)

        conn.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def update_task(
        conn: Connection, 
        task_id: int, 
        title: str | None = None,
        description: str | None = None,
        due_date: datetime | None = None
    ):
    try:
        query = select(tasks).where(tasks.c.id == task_id)

        result = conn.execute(query)
        task = result.fetchone() # (1, title, desc, completed, due-date, created-at)

        query = update(tasks).where(tasks.c.id == task_id).values(
            title=title or task[1],
            description=description or task[2],
            due_date=due_date or task[4],
            updated_at=datetime.now()
        )
        conn.execute(query)

        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def chenge_task_status(conn: Connection, task_id: int,):
    try:
        query = select(tasks).where(tasks.c.id == task_id)

        result = conn.execute(query)
        task = result.fetchone() # (1, title, desc, completed, due-date, created-at)

        query = update(tasks).where(tasks.c.id == task_id).values(
            completed=not task[3],
            updated_at=datetime.now()
        )
        conn.execute(query)

        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()