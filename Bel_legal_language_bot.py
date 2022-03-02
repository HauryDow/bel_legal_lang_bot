"""
the Bot makes everyday posts with Belarusial legal words and their definition
"""

import telebot
import time
import random
import config1
bot = telebot.TeleBot(config1.token)
channel_name = config1.channel_name
f = open('dictionary.txt', 'r', encoding='UTF-8')
words = f.read().split('\n')
f.close()
for word in words:
    post=" "+"\n"+"\n"+ "#беларускіюрыст"+"\n"+"\n"+word
    bot.send_message(channel_name, post)
    time.sleep(3600)

