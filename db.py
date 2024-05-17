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

    cur.execute("""
        CREATE TABLE IF NOT EXISTS all_groups (
            id_group SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id_subject SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id_teacher SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            tg_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            is_elder INTEGER DEFAULT 0,
            is_admin INTEGER DEFAULT 0,
            id_group INTEGER,
            FOREIGN KEY (id_group) REFERENCES all_groups (id_group)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS SubTech (
            id_subject INTEGER,
            id_teacher INTEGER,
            PRIMARY KEY (id_subject, id_teacher),
            FOREIGN KEY (id_subject) REFERENCES subjects (id_subject),
            FOREIGN KEY (id_teacher) REFERENCES teachers (id_teacher)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Schedule (
            id_schedule SERIAL PRIMARY KEY,
            day_of_week INTEGER,
            num_lesson INTEGER,
            id_group INTEGER,
            id_subject INTEGER,
            id_teacher INTEGER,
            FOREIGN KEY (id_subject) REFERENCES subjects (id_subject),
            FOREIGN KEY (id_group) REFERENCES all_groups (id_group),
            FOREIGN KEY (id_teacher) REFERENCES teachers (id_teacher)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Calendar (
            dates TIMESTAMP PRIMARY KEY,
            id_schedule INTEGER,
            FOREIGN KEY (id_schedule) REFERENCES Schedule (id_schedule)
        )
    """)

    db.commit()


async def registrate(id,name):
    cur.execute("SELECT * FROM accounts WHERE tg_id=%s", (id,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id, name) VALUES (%s, %s)", (id, name))
        db.commit()

async def set_group(id,group):
    #добавить проверку на корректность группы
    cur.execute("UPDATE accounts SET groupname=%s WHERE tg_id=%s", (group, id))
    db.commit()

async def get_group(id):
    cur.execute("SELECT groupname FROM accounts WHERE tg_id=%s", (id,))
    gr=cur.fetchone()[2]
    return gr


