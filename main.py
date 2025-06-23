import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from config import TOKEN
from aiogram.enums.parse_mode import ParseMode
from middleware import SubscriptionMiddleware
from routers import start


bot = Bot(token=TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
dp.message.middleware(SubscriptionMiddleware())



async def main() -> None:
    dp.include_router(start.router)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())