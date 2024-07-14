from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                        InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Проверить знания", callback_data = "check")], 
    [InlineKeyboardButton(text = "Редактировать", callback_data = "edit")],
])

edit_menu = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Добавить карточки", callback_data = "add")], 
    [InlineKeyboardButton(text = "Удалить карточки", callback_data = "delite")],
    [InlineKeyboardButton(text = "Изменить карточки", callback_data = "change")],
])