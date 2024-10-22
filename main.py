import telebot
from telebot import types


bot = telebot.TeleBot('7630092372:AAFr520Sw7AnFoCPPUoJ6SdLggUOGfx6ZxI')


def webAppKeyboard():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	web_app = types.WebAppInfo(url="https://dimagdd.github.io/CardsWebGameTest")
	one_butt = types.KeyboardButton(text="Тестовая страница", web_app=web_app)
	keyboard.add(one_butt)

	return keyboard

@bot.message_handler(func=lambda message: True)
def start(message):
	bot.send_message(message.chat.id, 'Bot is working!', reply_markup=webAppKeyboard()) 


bot.polling(non_stop=True)