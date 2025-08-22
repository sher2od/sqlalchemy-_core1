from database import engine

conn = engine.connect()
print(conn)