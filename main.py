import os
import asyncio
import threading

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT"))

disp = Dispatcher()
app = FastAPI()
tasks = []
@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot is active")


@app.get("/")
async def check():
    return {"status": "bot is running"}


@app.get("/")
async def check():
    return {"status": "bot is running"}

@app.get("/add")
async def add(message: Message):
    text = message.text.replace("/add", "").strip()

    if not text:
        await message.answer("Будь ласка, введи задачу після команди:\n/add купити молоко")
        return
    tasks.append(text)
    await message.answer("Додано задачу: {text}")


@app.get("/show")
async def show(message: Message):
    if not tasks:
        await message.answer("Список задач порожній")
        return

    result = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(tasks)])
    await message.answer("Твої задачі:\n" + result)


@disp.message(Command("delete"))
async def delete_task(message: Message):
    parts = message.text.split()

    if len(parts) < 2 or not parts[1].isdigit():
        await message.answer("Вкажи номер задачі для видалення:\n/delete 2")
        return

    index = int(parts[1]) - 1

    if index < 0 or index >= len(tasks):
        await message.answer("Невірний номер задачі.")
        return

    removed = tasks.pop(index)
    await message.answer(f"Видалено задачу: {removed}")

@app.on_event("startup")
async def startup():
    bot = Bot(token=BOT_TOKEN)
    asyncio.create_task(disp.start_polling(bot))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)

# async def main():
#     bot = Bot(token=BOT_TOKEN)
#
#     await disp.start_polling(bot)
#
#
# async def runner():
#     asyncio.run(main())
#
# if __name__ == "__main__":
#     threading.Thread(target=runner).start()
#     # result = asyncio.get_event_loop()
#     # result.create_task(main())
#     uvicorn.run(app,host = "0.0.0.0", port=PORT)

