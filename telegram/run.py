import asyncio
import aiogram
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from db import create_db
from app.handlers import router, on_startup

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await on_startup(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')