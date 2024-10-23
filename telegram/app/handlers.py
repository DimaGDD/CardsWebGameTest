from contextlib import ExitStack
from aiogram import F, Router
from aiogram.types import Message, chat, message
from aiogram.filters import CommandStart

import app.keaboards as kb
from db import add_user, get_all_users, update_message_start_id

router = Router()

async def on_startup(bot):
    all_users = await get_all_users()

    for user in all_users:
        chat_id = user['chat_id']
        message_start_id = user['message_start_id']

        try:
            await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_start_id, reply_markup=kb.main)
        except Exception as e:
            print(f"Ошибка при обновлении клавиатуры для chat_id {chat_id}: {e}")


@router.message(CommandStart())
async def cmd_start(message: Message):
    chat_id = message.chat.id

    sent_message = await message.answer('Привет!', reply_markup=kb.main)
    message_start_id = sent_message.message_id

    all_users = await get_all_users()
    previous_message_id = None

    if chat_id in [user['chat_id'] for user in all_users]:
        previous_user = next(user for user in all_users if user['chat_id'] == chat_id)
        previous_message_id = previous_user['message_start_id']

        if previous_message_id:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=previous_message_id)
            except Exception as e:
                print(f"Ошибка при удалении предыдущего сообщения для chat_id {chat_id}: {e}")

            try:
                await update_message_start_id(chat_id, message_start_id)
            except Exception as e:
                print(f'Ошибка замены старого nessgae_start_id на новый {e}')

    else:
        await add_user(chat_id, message_start_id)