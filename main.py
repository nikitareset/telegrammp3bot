import telebot
from flask import Flask
import threading
import random
import os

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

REPLIES = [
    "Готово, спасибо бро!",
    "Принял, брат!",
    "Заказ в обработке 👀",
    "Сохранил в нейроархив 🧠",
    "Отличный выбор!",
    "Обязательно добавлю на флешку!",
    "Хороший трек, запомнил!",
    "Окей, кидай ещё если есть!",
    "Артём будет доволен 😎",
    "Супер, у меня как раз уже он есть!",
    "Добавил в плейлист!"
]

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])
def handle_all(message):
    try:
        content_type = message.content_type
        if content_type == 'text':
            bot.send_message(CHANNEL_ID, f"Сообщение от @{message.chat.username or 'пользователь'}:\n{message.text}")
        elif content_type == 'photo':
            file_id = message.photo[-1].file_id
            caption = message.caption or ''
            bot.send_photo(CHANNEL_ID, file_id, caption=f"@{message.chat.username or 'пользователь'}: {caption}")
        elif content_type == 'document':
            bot.send_document(CHANNEL_ID, message.document.file_id, caption=f"Документ от @{message.chat.username or 'пользователь'}")
        elif content_type == 'video':
            bot.send_video(CHANNEL_ID, message.video.file_id, caption=f"Видео от @{message.chat.username or 'пользователь'}")
        elif content_type == 'audio':
            bot.send_audio(CHANNEL_ID, message.audio.file_id, caption=f"Аудио от @{message.chat.username or 'пользователь'}")
        elif content_type == 'voice':
            bot.send_voice(CHANNEL_ID, message.voice.file_id, caption=f"Голосовое от @{message.chat.username or 'пользователь'}")
        bot.reply_to(message, random.choice(REPLIES))
    except Exception as e:
        print(f"Ошибка: {e}")

def run_bot():
    bot.polling()

def run_web():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_bot).start()
threading.Thread(target=run_web).start()

