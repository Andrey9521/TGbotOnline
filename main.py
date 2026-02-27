import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "8683533315:AAHUlPP7MjrOePZAP54SoRaYvHEdi0fhm3s"

disp = Dispatcher()

@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot is active")

async def main():
    bot = Bot(token=BOT_TOKEN)

    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

