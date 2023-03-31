import telebot
from telebot import apihelper
from yt_dlp import YoutubeDL
import os
import time
from threading import Thread

BOT_TOKEN = "6059925047:AAFM40P3XGM74E2jS5-ExGE9W3KjopDABbQ"
bot = telebot.TeleBot(BOT_TOKEN)

def countdown(bot : telebot.TeleBot):
    time.sleep(60*4) # runs 4 minutes before stopping the bot
    bot.stop_bot()
          
# Create and launch a thread
from threading import Thread
t = Thread(target = countdown, args =(bot, ))
t.start() 

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey there,")
    bot.reply_to(message, "You can paste a link, I will send you the video")

@bot.message_handler(regexp='((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$')
def video_download(message):
    try:
        bot.reply_to(message, "Got it, download starting..")
        URLS = [message.text]
        with YoutubeDL() as ydl:
            ydl.download(URLS)
        bot.reply_to(message, "Download complete, sending..")
        filename = ""
        for fname in os.listdir("."):
            if fname.split(".")[-1] == "mp4":
                filename = fname
        bot.send_video( message.chat.id, video=open(filename, 'rb'), supports_streaming=True)
        bot.reply_to(message, "Complete")
        os.unlink(filename)
    except:
        bot.reply_to(message, f"Sorry, there was some error downloading: {message.text}")
bot.infinity_polling()
