import random as rd

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards import *
from bot.states import Tasks
from bot.tasks import *
from bot.database import *


router = Router()


@router.message(Command('start'))
async def cmd_start(msg: Message):
    await insert_userdata(user_id=msg.from_user.id, username=msg.from_user.username)

    await msg.answer(
        f'Привет {msg.from_user.full_name}!\n'
        'Это бот для выявления дизорфографии,\n'
        'Предлагаю тебе пройти простой тест на грамотность.',
        reply_markup=kb_start_test
    )


@router.message(Command('start_test'))
@router.message(F.text == 'Начать тест')
async def question_1(msg: Message, state: FSMContext):
    await state.set_state(Tasks.task_1)

    key = rd.choice(list(task1))
    await update_key(user_id=msg.from_user.id, key=key, number=1)
    await msg.answer(
        'Задание 1:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task1[key][1][0], task1[key][1][1]])
    )


@router.message(Tasks.task_1)
async def question_2(msg: Message, state: FSMContext):
    await state.update_data(task_1=msg.text)
    await state.set_state(Tasks.task_2)

    old_key = await get_key(user_id=msg.from_user.id, number=1)
    right_answer = task1[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=1)

    key = rd.choice(list(task2))
    await update_key(user_id=msg.from_user.id, key=key, number=2)
    await msg.answer(
        'Задание 2:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task2[key][1][0], task2[key][1][1]])
    )


@router.message(Tasks.task_2)
async def question_3(msg: Message, state: FSMContext):
    await state.update_data(task_2=msg.text)
    await state.set_state(Tasks.task_3)

    old_key = await get_key(user_id=msg.from_user.id, number=2)
    right_answer = task2[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=2)

    key = rd.choice(list(task3))
    await update_key(user_id=msg.from_user.id, key=key, number=3)
    await msg.answer(
        'Задание 3:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task3[key][1][0], task3[key][1][1]])
    )


@router.message(Tasks.task_3)
async def question_4(msg: Message, state: FSMContext):
    await state.update_data(task_3=msg.text)
    await state.set_state(Tasks.task_4)

    old_key = await get_key(user_id=msg.from_user.id, number=3)
    right_answer = task3[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=3)

    key = rd.choice(list(task4))
    await update_key(user_id=msg.from_user.id, key=key, number=4)
    await msg.answer(
        'Задание 4:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task4[key][1][0], task4[key][1][1]])
    )


@router.message(Tasks.task_4)
async def question_5(msg: Message, state: FSMContext):
    await state.update_data(task_4=msg.text)
    await state.set_state(Tasks.task_5)

    old_key = await get_key(user_id=msg.from_user.id, number=4)
    right_answer = task4[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=4)

    key = rd.choice(list(task5))
    await update_key(user_id=msg.from_user.id, key=key, number=5)
    await msg.answer(
        'Задание 5:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task5[key][1][0], task5[key][1][1]])
    )


@router.message(Tasks.task_5)
async def question_6(msg: Message, state: FSMContext):
    await state.update_data(task_5=msg.text)
    await state.set_state(Tasks.task_6)

    old_key = await get_key(user_id=msg.from_user.id, number=5)
    right_answer = task5[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=5)

    key = rd.choice(list(task6))
    await update_key(user_id=msg.from_user.id, key=key, number=6)
    await msg.answer(
        'Задание 6:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task6[key][1][0], task6[key][1][1]])
    )


@router.message(Tasks.task_6)
async def question_7(msg: Message, state: FSMContext):
    await state.update_data(task_6=msg.text)
    await state.set_state(Tasks.task_7)

    old_key = await get_key(user_id=msg.from_user.id, number=6)
    right_answer = task6[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=6)

    key = rd.choice(list(task7))
    await update_key(user_id=msg.from_user.id, key=key, number=7)
    await msg.answer(
        'Задание 7:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task7[key][1][0], task7[key][1][1]])
    )


@router.message(Tasks.task_7)
async def question_8(msg: Message, state: FSMContext):
    await state.update_data(task_7=msg.text)
    await state.set_state(Tasks.task_8)

    old_key = await get_key(user_id=msg.from_user.id, number=7)
    right_answer = task7[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=7)

    key = rd.choice(list(task8))
    await update_key(user_id=msg.from_user.id, key=key, number=8)
    await msg.answer(
        'Задание 8:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task8[key][1][0], task8[key][1][1]])
    )


@router.message(Tasks.task_8)
async def question_9(msg: Message, state: FSMContext):
    await state.update_data(task_8=msg.text)
    await state.set_state(Tasks.task_9)

    old_key = await get_key(user_id=msg.from_user.id, number=8)
    right_answer = task8[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=8)

    key = rd.choice(list(task9))
    await update_key(user_id=msg.from_user.id, key=key, number=9)
    await msg.answer(
        'Задание 9:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task9[key][1][0], task9[key][1][1]])
    )


@router.message(Tasks.task_9)
async def question_10(msg: Message, state: FSMContext):
    await state.update_data(task_9=msg.text)
    await state.set_state(Tasks.task_10)

    old_key = await get_key(user_id=msg.from_user.id, number=9)
    right_answer = task9[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=9)

    key = rd.choice(list(task10))
    await update_key(user_id=msg.from_user.id, key=key, number=10)
    await msg.answer(
        'Задание 10:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task10[key][1][0], task10[key][1][1]])
    )


@router.message(Tasks.task_10)
async def question_11(msg: Message, state: FSMContext):
    await state.update_data(task_10=msg.text)
    await state.set_state(Tasks.task_11)

    old_key = await get_key(user_id=msg.from_user.id, number=10)
    right_answer = task10[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=10)

    key = rd.choice(list(task11))
    await update_key(user_id=msg.from_user.id, key=key, number=11)
    await msg.answer(
        'Задание 11:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task11[key][1][0], task11[key][1][1]])
    )


@router.message(Tasks.task_11)
async def question_12(msg: Message, state: FSMContext):
    await state.update_data(task_11=msg.text)
    await state.set_state(Tasks.task_12)

    old_key = await get_key(user_id=msg.from_user.id, number=11)
    right_answer = task11[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=11)

    key = rd.choice(list(task12))
    await update_key(user_id=msg.from_user.id, key=key, number=12)
    await msg.answer(
        'Задание 12:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task12[key][1][0], task12[key][1][1]])
    )


@router.message(Tasks.task_12)
async def question_13(msg: Message, state: FSMContext):
    await state.update_data(task_12=msg.text)
    await state.set_state(Tasks.task_13)

    old_key = await get_key(user_id=msg.from_user.id, number=12)
    right_answer = task12[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=12)

    key = rd.choice(list(task13))
    await update_key(user_id=msg.from_user.id, key=key, number=13)
    await msg.answer(
        'Задание 13:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task13[key][1][0], task13[key][1][1]])
    )


@router.message(Tasks.task_13)
async def question_14(msg: Message, state: FSMContext):
    await state.update_data(task_13=msg.text)
    await state.set_state(Tasks.task_14)

    old_key = await get_key(user_id=msg.from_user.id, number=13)
    right_answer = task13[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=13)

    key = rd.choice(list(task14))
    await update_key(user_id=msg.from_user.id, key=key, number=14)
    await msg.answer(
        'Задание 14:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task14[key][1][0], task14[key][1][1]])
    )


@router.message(Tasks.task_14)
async def question_15(msg: Message, state: FSMContext):
    await state.update_data(task_14=msg.text)
    await state.set_state(Tasks.task_15)

    old_key = await get_key(user_id=msg.from_user.id, number=14)
    right_answer = task14[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=14)

    key = rd.choice(list(task15))
    await update_key(user_id=msg.from_user.id, key=key, number=15)
    await msg.answer(
        'Задание 15:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task15[key][1][0], task15[key][1][1]])
    )


@router.message(Tasks.task_15)
async def question_16(msg: Message, state: FSMContext):
    await state.update_data(task_15=msg.text)
    await state.set_state(Tasks.task_16)

    old_key = await get_key(user_id=msg.from_user.id, number=15)
    right_answer = task15[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=15)

    key = rd.choice(list(task16))
    await update_key(user_id=msg.from_user.id, key=key, number=16)
    await msg.answer(
        'Задание 16:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task16[key][1][0], task16[key][1][1]])
    )


@router.message(Tasks.task_16)
async def question_17(msg: Message, state: FSMContext):
    await state.update_data(task_16=msg.text)
    await state.set_state(Tasks.task_17)

    old_key = await get_key(user_id=msg.from_user.id, number=16)
    right_answer = task16[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=16)

    key = rd.choice(list(task17))
    await update_key(user_id=msg.from_user.id, key=key, number=17)
    await msg.answer(
        'Задание 17:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task17[key][1][0], task17[key][1][1]])
    )


@router.message(Tasks.task_17)
async def question_18(msg: Message, state: FSMContext):
    await state.update_data(task_17=msg.text)
    await state.set_state(Tasks.task_18)

    old_key = await get_key(user_id=msg.from_user.id, number=17)
    right_answer = task17[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=17)

    key = rd.choice(list(task18))
    await update_key(user_id=msg.from_user.id, key=key, number=18)
    await msg.answer(
        'Задание 18:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task18[key][1][0], task18[key][1][1]])
    )


@router.message(Tasks.task_18)
async def question_19(msg: Message, state: FSMContext):
    await state.update_data(task_18=msg.text)
    await state.set_state(Tasks.task_19)

    old_key = await get_key(user_id=msg.from_user.id, number=18)
    right_answer = task18[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=18)

    key = rd.choice(list(task19))
    await update_key(user_id=msg.from_user.id, key=key, number=19)
    await msg.answer(
        'Задание 19:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task19[key][1][0], task19[key][1][1]])
    )


@router.message(Tasks.task_19)
async def question_20(msg: Message, state: FSMContext):
    await state.update_data(task_19=msg.text)
    await state.set_state(Tasks.task_20)

    old_key = await get_key(user_id=msg.from_user.id, number=19)
    right_answer = task19[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=19)

    key = rd.choice(list(task20))
    await update_key(user_id=msg.from_user.id, key=key, number=20)
    await msg.answer(
        'Задание 20:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task20[key][1][0], task20[key][1][1]])
    )


@router.message(Tasks.task_20)
async def question_21(msg: Message, state: FSMContext):
    await state.update_data(task_20=msg.text)
    await state.set_state(Tasks.task_21)

    old_key = await get_key(user_id=msg.from_user.id, number=20)
    right_answer = task20[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=20)

    key = rd.choice(list(task21))
    await update_key(user_id=msg.from_user.id, key=key, number=21)
    await msg.answer(
        'Задание 21:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task21[key][1][0], task21[key][1][1]])
    )


@router.message(Tasks.task_21)
async def question_22(msg: Message, state: FSMContext):
    await state.update_data(task_21=msg.text)
    await state.set_state(Tasks.task_22)

    old_key = await get_key(user_id=msg.from_user.id, number=21)
    right_answer = task21[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=21)

    key = rd.choice(list(task22))
    await update_key(user_id=msg.from_user.id, key=key, number=22)
    await msg.answer(
        'Задание 22:\n'
        f'Раскрой скобки: "{key}"',
        reply_markup=await create_buttons([task22[key][1][0], task22[key][1][1]])
    )


@router.message(Tasks.task_22)
async def question_23(msg: Message, state: FSMContext):
    await state.update_data(task_22=msg.text)
    await state.set_state(Tasks.task_23)

    old_key = await get_key(user_id=msg.from_user.id, number=22)
    right_answer = task22[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=22)

    key = rd.choice(list(task23))
    await update_key(user_id=msg.from_user.id, key=key, number=23)
    await msg.answer(
        'Задание 23:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task23[key][1][0], task23[key][1][1]])
    )


@router.message(Tasks.task_23)
async def question_24(msg: Message, state: FSMContext):
    await state.update_data(task_23=msg.text)
    await state.set_state(Tasks.task_24)

    old_key = await get_key(user_id=msg.from_user.id, number=23)
    right_answer = task23[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=23)

    key = rd.choice(list(task24))
    await update_key(user_id=msg.from_user.id, key=key, number=24)
    await msg.answer(
        'Задание 24:\n'
        f'Раскрой скобки: "{key}"',
        reply_markup=await create_buttons([task24[key][1][0], task24[key][1][1]])
    )


@router.message(Tasks.task_24)
async def question_25(msg: Message, state: FSMContext):
    await state.update_data(task_24=msg.text)
    await state.set_state(Tasks.task_25)

    old_key = await get_key(user_id=msg.from_user.id, number=24)
    right_answer = task24[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=24)

    key = rd.choice(list(task25))
    await update_key(user_id=msg.from_user.id, key=key, number=25)
    await msg.answer(
        'Задание 25:\n'
        f'Вставь пропуск в слове "{key}"',
        reply_markup=await create_buttons([task25[key][1][0], task25[key][1][1], task25[key][1][2]])
    )


@router.message(Command('results'))
@router.message(Tasks.task_25)
async def _result(msg: Message, state: FSMContext):
    await state.update_data(task_25=msg.text)
    await state.set_state(Tasks.results)

    old_key = await get_key(user_id=msg.from_user.id, number=25)
    right_answer = task25[old_key][0]
    result = 1 if msg.text == right_answer else 0
    await update_answer(user_id=msg.from_user.id, result=result, number=25)

    results = 0
    mistakes = []
    for i in range(25):
        answer = await get_answer(user_id=msg.from_user.id, number=i+1)
        if answer == 0:
            mistakes.append(task_types[f'task{i+1}'])
        else:
            results += 1

    themes = ''
    for i in mistakes:
        themes += f' • {i}\n'

    if results == 25:
        themes = '  Ошибок нет!'

    await msg.answer(
        'Результаты теста:\n\n'
        f'Решено заданий: {results}/25\n\n'
        f'Темы и задания, в которых были допущены ошибки:\n{themes}',
        reply_markup=ReplyKeyboardRemove()
    )
