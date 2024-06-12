from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.types import KeyboardButton,\
    ReplyKeyboardMarkup
# from config import token

token='6504532305:AAHC74qLTDnGt6G4btYdMBaxBzEMrscDxD0'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('tosh')
btn2 = types.KeyboardButton('qaychi')
btn3 = types.KeyboardButton('qogoz')
btn4 = types.KeyboardButton('tosh')
btn5 = types.KeyboardButton('qaychi')

kb.add(btn1, btn2, btn3, btn4, btn5)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Assalomu aleykum {message.from_user.first_name}', reply_markup=kb)

@dp.message_handler()
async def handle_text(message: types.Message):
    if message.text == 'tosh':
        await bot.send_message(message.from_user.id, 'tosh\nsiz yutdiz')
    elif message.text == 'qaychi':
        await bot.send_message(message.from_user.id, 'qogoz\nsiz yutqazdingiz')
    elif message.text == 'qogoz':
        await bot.send_message(message.from_user.id, 'tosh\nsiz yutqazdingiz')
    elif message.text == 'qaychi':
        await bot.send_message(message.from_user.id, 'tosh\nsiz yutqazdingiz')
    elif message.text == 'qogoz':
        await bot.send_message(message.from_user.id, 'qogoz\nsiz yutqazdingiz')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
