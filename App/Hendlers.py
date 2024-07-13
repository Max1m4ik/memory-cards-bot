from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from functions import *

import App.keyboards as kb


router = Router()

update()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет,что хочешь сделать?", reply_markup=kb.main)

@router.callback_query(F.data == "check")
async def check(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали проверить знания")

def edit_menu():
        bot.send_message(message.chat.id, "РЕдактировать")
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton("Добавить карточки"))
        markup.add(types.KeyboardButton("Удалить карточки"))
        markup.add(types.KeyboardButton("Изменить карточки"))
        edit = bot.send_message(message.chat.id, "Что хочешь сделать?", reply_markup=markup)
        bot.register_next_step_handler(message, edit)
        #@bot.callback_query_handler(func=lambda callback: True)
        def edit(message):
            if message.text == "Add":

                bot.send_message(message.chat.id, "Добавить карточки")

                update()

                bot.send_message(message.chat.id, "Вопрос: ")

                bot.register_next_step_handler(message, next)

                #@bot.message_handler(func=lambda message: True)
                def next1(message):
                    global question_for_add
                    question_for_add = message.text

                    bot.send_message(message.chat.id, "Ответ: ")
                @bot.message_handler(func=lambda message: True)
                def message(message): 
                    answer_for_add = message.text

                    with sq.connect('cards.db') as con:
                        cur = con.cursor()
                        cur.execute(f"INSERT INTO cards (quastion, answer) VALUES ({question_for_add}, {answer_for_add})")
            
            elif message.text == "Delete":
                update()

                bot.send_message(message.chat.id, "Удалить карточки")

                text = "" 

                for i in range (1, col_of_q):
                    quest(i)
                    answ(i)
                    text = str(i) + "-" + question + answer
                    bot.send_message(message.chat.id, text)

                bot.send_message(message.chat.id, "Номер карточки которую хотите удалить: ")

                bot.register_next_step_handler(message, for_del)

                #@bot.message_handler(func=lambda message: True)
                def for_del(message):

                    number_question_for_del = message.text

                    with sq.connect('cards.db') as con:
                        cur = con.cursor()
                        cur.execute(f"DELETE FROM cards WHERE number = {number_question_for_del}")
            #else:
                #bot.send_message(message.chat.id, data)

#@bot.callback_query_handler(func=lambda callback: True)
def on_click(message):
    if message.text == "Проверить знания":
        bot.send_message(message.chat.id, "ПРоверить знания")

        update()
        global correct 
        corect = 0
        for i in range(1, col_of_q):
            quest(i)
            bot.send_message(message, f"Вопрос номер {i} {question}")

            #answer = message.text
            #print(f"Вопрос номер {i} {question} ")
            @bot.message_handler(func=lambda message: True)
            def message(message):
                global answer
                global correct
                answer = message.text
                if answer == question:
                    bot.send_message(message, "Правильно")
                    correct += 1
                else:
                    bot.send_message(message, "Не правильно")
                
                if i == col_of_q:
                    bot.send_message(message, f"Правильных ответов: {correct} из {col_of_q}, {correct / col_of_q * 100}% ")


    elif message.text == "Редактировать":
        edit_menu()
