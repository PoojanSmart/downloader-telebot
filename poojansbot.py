import telebot
from telebot import apihelper
from yt_dlp import YoutubeDL
import os

BOT_TOKEN = "6059925047:AAFM40P3XGM74E2jS5-ExGE9W3KjopDABbQ"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey there,")
    bot.reply_to(message, "You can paste a link, I will send you the video")

@bot.message_handler(regexp='((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$')
def video_download(message):
    URLS = [message.text]
    with YoutubeDL() as ydl:
        ydl.download(URLS)
    filename = ""
    for fname in os.listdir("."):
        if fname.split(".")[-1] == "mp4":
            filename = fname
    bot.send_video( message.chat.id, video=open(filename, 'rb'), supports_streaming=True)
    os.unlink(filename)

bot.infinity_polling()




