from functions import *
from config import TOKEN
from App.Hendlers import *
import asyncio
from aiogram import Bot, Dispatcher


#https://t.me/Cards_for_memory_bot

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")