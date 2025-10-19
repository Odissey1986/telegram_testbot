import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters  import Command
from aiogram import F

import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("TG_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

pets = {}

main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="🌯Покормить"), types.KeyboardButton(text="⚽Поиграть")],
        [types.KeyboardButton(text="🛏Спать"), types.KeyboardButton(text="📜Статус")],
        [types.KeyboardButton(text="🚪Выход")]
    ]
)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        new_pet = {
            "name": "Pushok 🐱‍👤",
            "hunger": 50,
            "energy": 50,
            "happiness": 50,
        }
        pets[user_id] = new_pet

    await message.answer(
        f"Привет, {message.from_user.first_name}\n"
        f"Познакомся со своим питомцем: {pets[user_id]["name"]}\n"
        f"Позаботься о нём!",
        reply_markup=main_kb
    )

@dp.message(F.text == "🌯Покормить")
async def feed_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["hunger"] = min(pet["hunger"] + 10, 100)
    pet["energy"] = max(pet["energy"] - 5, 0)
    await message.answer(f"{pet['name']} слопал пол холодильника!")

@dp.message(F.text == "⚽Поиграть")
async def play_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100)
    pet["energy"] = max(pet["energy"] - 15, 0)
    await message.answer(f"{pet['name']} классно поиграл!")


def progres_bar(value: int, lenght: int):
    filled = int(value/100 * 10)
    return "🟩" * filled + "⬛" * (lenght - filled)

@dp.message(F.text == "📜Статус")
async def feed_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]

    hun = pet['hunger']
    en = pet['energy']
    hap = pet['happiness']

    status = (
        f"Статус вашего питомца {pet['name']}:\n"
        f"Сытость: {hun}% {progres_bar(hun, 10)}\n"
        f"Энергия: {en}% {progres_bar(en, 10)}\n"
        f"Счастье: {hap}% {progres_bar(hap, 10)}\n"
    )
    await message.answer(status)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())