from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                        InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Проверить знания", callback_data = "check")], 
    [InlineKeyboardButton(text = "Редактировать", callback_data = "edit")],
])