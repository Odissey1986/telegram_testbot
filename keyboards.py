from aiogram import types

BTN_FEED = "🌯Покормить"
BTN_PLAY = "⚽Поиграть"
BTN_SLEEP = "🛏Спать"
BTN_STATUS = "📜Статус"
BTN_EXIT = "🚪Выход"

main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="🌯Покормить"), types.KeyboardButton(text="⚽Поиграть")],
        [types.KeyboardButton(text="🛏Спать"), types.KeyboardButton(text="📜Статус")],
        [types.KeyboardButton(text="🚪Выход")]
    ],
    resize_keyboard=True
)

remove_kb = types.ReplyKeyboardRemove()

food_kb = types.InlineKeyboardMarkup(
    inline_keyboard= [
        [
            types.InlineKeyboardButton(text="🌯 Шаурма", callback_data="shawarma"),
            types.InlineKeyboardButton(text="🥩 Стейк", callback_data="steak")
            ],
        [
            types.InlineKeyboardButton(text="☕ Дать побулькать", callback_data="water")
        ]
    ]
)