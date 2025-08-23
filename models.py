from datetime import datetime
from sqlalchemy import (
    Table, Column,
    Integer, String, DateTime, Boolean, Text
)
from database import metadata_obj

tasks = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(length=64), nullable=False),
    Column('description', Text),
    Column('completed', Boolean, nullable=False, default=False),
    Column('due_date', DateTime, default=datetime.now),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now)
)