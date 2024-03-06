import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.enums import ParseMode
from bot.handlers import *
from dispatcher import TOKEN, dp


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())