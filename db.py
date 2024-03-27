import sqlite3 as sq

db = sq.connect('tg.db')

cur = db.cursor()


async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS accounts(
                    tg_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    groupname TEXT DEFAULT NULL)
                                    
    """)
    db.commit()


async def registrate(id,name):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id=={key}".format(key=id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id, name) VALUES (?, ?)", (id, name))
        db.commit()

async def set_group(id,group):
    #добавить проверку на корректность группы
    cur.execute("UPDATE accounts SET groupname=? WHERE tg_id=?",(group,id))
    db.commit()

async def get_group(id):
    return cur.execute("SELECT * FROM accounts WHERE tg_id=?",(id,)).fetchone()[2]


