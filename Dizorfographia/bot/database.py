import sqlite3 as sq


db = sq.connect('database.db')
cur = db.cursor()


async def db_start():
    keys = ''
    for i in range(25):
        keys += f"key{i+1} CHAR DEFAULT ' ',\n"
    answers = ''
    for i in range(25):
        answers += f'answer{i+1} INT DEFAULT 0,\n'

    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        username VARCHAR(32) NOT NULL,
        {keys}
        {answers}
        result INT DEFAULT 0
        )
    ''')
    db.commit()


async def insert_userdata(user_id, username):
    user = cur.execute(f"SELECT * FROM users WHERE user_id == {user_id}").fetchone()
    if not user:
        cur.execute(f"INSERT INTO users (user_id, username) VALUES ({user_id}, '{username}')")
    # else:
    #     cur.execute(f"UPDATE users SET username = '{username}' WHERE user_id == {user_id}")
    db.commit()


async def update_key(user_id, key, number):
    cur.execute(f"UPDATE users SET key{number} = '{key}' WHERE user_id == {user_id}")
    db.commit()


async def get_key(user_id, number):
    return cur.execute(f"SELECT key{number} FROM users WHERE user_id == {user_id}").fetchone()[0]


async def update_answer(user_id, result, number):
    cur.execute(f"UPDATE users SET answer{number} = '{result}' WHERE user_id == {user_id}")
    db.commit()


async def get_answer(user_id, number):
    return cur.execute(f"SELECT answer{number} FROM users WHERE user_id == {user_id}").fetchone()[0]
