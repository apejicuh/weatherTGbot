from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Покажи погоду!')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)