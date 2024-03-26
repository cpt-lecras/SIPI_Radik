import sqlite3 as sq

db = sq.connect('tg.db')

cur = db.cursor()


async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS accounts(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    group TEXT NOT NULL
                                    
    """)
    db.commit()


