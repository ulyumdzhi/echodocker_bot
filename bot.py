import os
import logging

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

# Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из под docker контейнера

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# admin_id = 123456789


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}!"
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)
    
@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f"{user_name=} {user_id=} sent message: {text}")
    await bot.send_message(user_id, text)
    # await bot.send_message(admin_id, text)
    

if __name__ == '__main__':
    executor.start_polling(dp)