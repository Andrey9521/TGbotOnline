import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from fastapi import FastAPI
import uvicorn

BOT_TOKEN = "8683533315:AAHUlPP7MjrOePZAP54SoRaYvHEdi0fhm3s"
PORT = 8080

disp = Dispatcher()
app = FastAPI()

@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot is active")


@app.get("/")
async def check():
    return {"status": "bot is running"}

async def main():
    bot = Bot(token=BOT_TOKEN)

    await disp.start_polling(bot)

if __name__ == "__main__":
    result = asyncio.get_event_loop()
    result.create_task(main())
    uvicorn.run(app,host = "0.0.0.0", port=PORT)

