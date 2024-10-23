from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# main = ReplyKeyboardMarkup(keyboard=[
# 	[KeyboardButton(text='Play', web_app=WebAppInfo(url='https://dimagdd.github.io/CardsWebGameTest'))]
# ], 
# 	resize_keyboard=True, 
# 	input_field_placeholder='Выберите пунк меню!')


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Play', web_app=WebAppInfo(url='https://d63a-78-24-102-65.ngrok-free.app'))]
])


# https://dimagdd.github.io/CardsWebGameTest
# https://github.com/DimaGDD/CardsWebGameTest