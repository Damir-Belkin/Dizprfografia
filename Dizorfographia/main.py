import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from os import getenv

from bot.handlers import router
from bot.database import db_start


async def main():
    bot = Bot(token=getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)

    await db_start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('bot stopped')
