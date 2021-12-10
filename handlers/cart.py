"""
Просто функции для проверок бота
"""
from random import randint

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import ADMINS


# async def cart_func_admin(dp: Dispatcher):
#     await dp.bot.send_message(ADMINS, 'ТАНЯ БЛЛЯЯЯЯЯЯЯЯ', reply_markup=types.ReplyKeyboardRemove())


async def cart_func(message: types.Message):
    await message.answer('ТАНЯ Привет', reply_markup=types.ReplyKeyboardRemove())


def register_handlers_cart(dp: Dispatcher):
    dp.register_message_handler(cart_func, Text(equals=".-."), state="*")
