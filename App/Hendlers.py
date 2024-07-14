from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from functions import *
import sqlite3 as sq

import App.keyboards as kb

router = Router()
correct = 0
stage = 'null' 
update()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет,что хочешь сделать?", reply_markup=kb.main)

@router.message(F.text)
async def answer_from_user(message: Message):
    global stage
    if stage == 'chek':
        for i in range(1, col_of_q):
            quest(i)
            await message.answer(f"Карточка номер {i}: {question}")
            await message.answer("Ваш ответ: ")
            global answer
            global correct
            correct = 0
            answer = F.text
            if answer == question:
                await message.answer("Правильно")
                correct += 1
            else:
                await message.answer("Не правильно")
            
        await message.answer(f"Правильных ответов: {correct} из {col_of_q}, {correct / col_of_q * 100}% ")
        stage = 'null'
    
    elif stage == 'change1':

        global question_for_add
        question_for_add = F.text
        await message.answer("Ответ: ")
        stage = 'change2'

    elif stage == 'change2':

        answer_for_add = F.text
        with sq.connect('cards.db') as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO cards VALUES (5, {question_for_add}, {answer_for_add})")
            #cur.execute(f"INSERT INTO cards (answer) VALUES ({answer_for_add})")
        await message.answer("Карточка успешно добавлена!")
        stage = 'null'
    
    elif stage == 'del':
        number_question_for_del = F.text

        with sq.connect('cards.db') as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM cards WHERE number = {number_question_for_del}")
        stage = 'null'
    else:
        await message.answer("Что-то пошло не так")

@router.callback_query(F.data == "check")
async def check(callback: CallbackQuery):
    global stage
    await callback.answer("Вы решили проверить знания")
    update()
    global correct
    correct = 0
    stage = 'check'



@router.callback_query(F.data == "edit")
async def check(callback: CallbackQuery):
    await callback.answer("Вы решили редактировать карточки")
    await callback.message.edit_text("Выберите что вы будите делать: ", reply_markup=kb.edit_menu)

    #@bot.callback_query_handler(func=lambda callback: True)
@router.callback_query(F.data == "add")
async def check(callback: CallbackQuery):
    global stage
    await callback.answer("Вы решили добавить карточки")

    update()

    await callback.message.answer("Вопрос: ")
    stage = 'change1'

@router.callback_query(F.data == "delite")
async def check(callback: CallbackQuery):
    global stage
    await callback.answer("Вы решили удалить карточки")
    update()

    text = "" 

    for i in range (1, col_of_q):
        quest(i)
        answ(i)
        text += f"{i} - {question} - {answer}\n"
    await callback.message.answer(text)

    await callback.message.answer("Номер карточки которую хотите удалить: ")
    stage = 'del'