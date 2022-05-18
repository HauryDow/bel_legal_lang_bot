"""
the Bot makes everyday posts with some picture+Belarusial legal word and its definition
"""

#!/usr/bin/python3

import telegram
import time

TOKEN = 'your_token_here'
bot = telegram.Bot(token=TOKEN)
chat_id='your_chat_id_here'
f = open('dictionary.txt', 'r', encoding='UTF-8')
words = f.read().split('\n')
f.close()
temp = ''
num=1
for word in words:
    temp += word + '\n'
    if word[-1] == '*':
        post = "#беларуская_лексіка #родныя_словы" + "\n" + "\n" + temp[:-2:]
        #pictures named 1.jpg, 2.jpg, 3.jpg, etc.
        name='folder_with_pictures'+str(num)+'.jpg'
        with open(name, 'rb') as photo:
            bot.send_photo(chat_id, photo, post)
        temp = ''
        num+=1
        time.sleep(86400)
