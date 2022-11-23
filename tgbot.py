from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import keyboards as kb

import weather

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler(commands=['weather'])
async def process_start_command(message: types.Message):
    forecast_str = weather.request_forecast()
    await message.reply("Вот такая погода на сегодня:\n" + forecast_str)

if __name__ == '__main__':
    executor.start_polling(dp)