from db import pets

from aiogram import Dispatcher, types, F
from aiogram.filters import Command

from keyboards import (
    main_kb,
    food_kb,
    BTN_FEED, 
    BTN_PLAY, 
    BTN_SLEEP, 
    BTN_STATUS, 
    BTN_EXIT
)

def progres_bar(value: int, lenght: int):
    filled = int(value/100 * 10)
    return "🟩" * filled + "⬛" * (lenght - filled)

async def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler, Command("start"))
    dp.message.register(feed_pet, F.text == "🌯Покормить")
    dp.message.register(play_pet, F.text == "⚽Поиграть")
    dp.message.register(status_pet, F.text == "📜Статус")
    dp.message.register(sleep_pet, F.text == "🛏Спать")

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

async def feed_pet(message: types.Message):
    user_id = message.from_user.id

    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    await message.answer(
        f"Чем вы хотите покормить {pet['name']}?", 
        reply_markup=food_kb
    )

    # pet["hunger"] = min(pet["hunger"] + 10, 100)
    # pet["energy"] = max(pet["energy"] - 5, 0)
    # await message.answer(f"{pet['name']} слопал пол холодильника!")

async def play_pet(message: types.Message):
    user_id = message.from_user.id

    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100)
    pet["energy"] = max(pet["energy"] - 15, 0)
    await message.answer(f"{pet['name']} классно поиграл!")

async def status_pet(message: types.Message):
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

async def sleep_pet(message: types.Message):
    user_id = message.from_user.id

    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100)
    pet["hunger"] = min(pet["hunger"] - 5, 100)
    pet["energy"] = max(pet["energy"] + 15, 0)
    await message.answer(f"{pet['name']} славно выспался!")