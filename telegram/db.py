import aiosqlite

DATABASE = "db.sqlite3"

async def create_db():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER UNIQUE,
                message_start_id INTEGER
            )
        ''')
        await db.commit()


async def add_user(chat_id, message_start_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(''' 
            INSERT OR IGNORE INTO users (chat_id, message_start_id) VALUES (?, ?)
        ''', (chat_id, message_start_id))
        await db.commit()


async def update_message_start_id(chat_id, message_start_id):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute('''
            UPDATE users SET message_start_id = ? WHERE chat_id = ?
        ''', (message_start_id, chat_id))
        await db.commit()


async def get_all_users():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute('''SELECT chat_id, message_start_id FROM users''') as cursor:
            users = await cursor.fetchall()
            return [{"chat_id": user[0], "message_start_id": user[1]} for user in users]