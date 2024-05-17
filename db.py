import psycopg2 as ps

dbname = 'postgres'
user = 'postgres'
password = 'root'
host = 'localhost'
port = '5432'


try:
    db = ps.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )
    cur = db.cursor()
    print("Connection access")
except ps.OperationalError as e:
    print('Error while connecting to db',e)




async def db_start():

    """
    Start the database connection
    :return:
    """

    cur.execute("""CREATE TABLE IF NOT EXISTS accounts(
                        tg_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        is_elder INTEGER DEFAULT 0,
                        is_admin INTEGER DEFAULT 0,
                        id_group TEXT DEFAULT NULL,
                        FOREIGN KEY (id_group) REFERENCES all_groups (id_group),
                    )                                    
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS all_groups(
                        id_group INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                    )
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS subjects(
                            id_subject INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                        )
            """)
    cur.execute("""CREATE TABLE IF NOT EXISTS teachers(
                                id_teacher INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                            )
                """)
    cur.execute("""CREATE TABLE IF NOT EXISTS SubTech(
                                    id_subject INTEGER,
                                    id_teacher INTEGER,
                                    PRIMARY KEY (id_subject, id_teacher),
                                    FOREIGN KEY (id_subject) REFERENCES subjects (id_subject),
                                    FOREIGN KEY (id_teacher) REFERENCES teachers (id_teacher),
                                )
                    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS Schedule(
                                        id_schedule INTEGER PRIMARY KEY AUTOINCREMENT,
                                        day_of_week INTEGER,
                                        num_lesson INTEGER,
                                        id_group INTEGER,
                                        id_subject INTEGER,
                                        id_teacher INTEGER,
                                        FOREIGN KEY (id_subject) REFERENCES SubTech (id_subject),
                                        FOREIGN KEY (id_group) REFERENCES all_groups (id_group),
                                        FOREIGN KEY (id_teacher) REFERENCES SubTech (id_teacher),
                                    )
                    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS Calendar(
                                        dates DATETIME PRIMARY KEY,
                                        id_schedule INTEGER,
                                        FOREIGN KEY (id_schedule) REFERENCES Schedule (id_schedule),
                                    )
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


