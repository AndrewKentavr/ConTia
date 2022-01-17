from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData

from data_b.dp_control import problem_category_random, finding_categories_table
from handlers.keyboards.inline import math_menu_inline

callback_problems_math = CallbackData("problems", "category")
callback_problems_info_math = CallbackData("values", "info", "translate")


async def tasks_category_math_start(message: types.Message):
    await message.answer('Выберите категорию заданий:',
                         reply_markup=math_menu_inline.get_inline_math_problems_category())


async def tasks_category_math_print(call: types.CallbackQuery, callback_data: dict):
    category = callback_data["category"]
    list_info_problem = problem_category_random(category, 'math')
    title = list_info_problem[0]
    href = list_info_problem[1]
    subcategory = list_info_problem[2]
    complexity, classes = list_info_problem[3], list_info_problem[4]
    condition = list_info_problem[5]
    info_problem = list_info_problem[6:]
    global problems_info_data_math
    problems_info_data_math = info_problem

    await call.message.answer(
        f'Название задания или его ID: {title}\nСсылка на задание: {href}\nПодкатегория: {subcategory}\n{complexity}, {classes}',
        reply_markup=types.ReplyKeyboardRemove())
    await call.message.answer(f'{condition}',
                              reply_markup=math_menu_inline.get_inline_math_problems_category_info(info_problem))

    await call.answer()


async def tasks_category_math_print_info(call: types.CallbackQuery, callback_data: dict):
    translate = callback_data['translate']

    for i in range(len(problems_info_data_math)):
        if translate in problems_info_data_math[i]:
            await call.message.answer(f'{problems_info_data_math[i]}')
            break
    await call.answer()


def register_handlers_tasks_math_category(dp: Dispatcher):
    dp.register_message_handler(tasks_category_math_start, Text(equals="Задания по категориям Математики"))

    all_files_names = [i[0] for i in finding_categories_table('math')]
    dp.register_callback_query_handler(tasks_category_math_print,
                                       callback_problems_math.filter(category=all_files_names), state='*')

    info = ['Solution 1', 'Solution 2', 'Decision', 'Answer', 'Hint', 'Remarks']
    dp.register_callback_query_handler(tasks_category_math_print_info,
                                       callback_problems_info_math.filter(info=info), state='*')
