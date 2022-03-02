#имя бота @BelarusianLawLanguageBot, его надо добавить в канал как подписчика и сделать администратором с правом публикации постов
#он у меня в списке ботов телеги теперь (не очень хорошо, что бот-администратор в Беларуси)
#можно Дарине сделать своего бота и наделить его правами
#!/usr/bin/python3.3 - эта строка нужна, чтоб залить на сервер
import telebot
import time
import random
# можно токен, который выдает @botfather, разместить в файле config1, в ту же папку, что и бот
bot = telebot.TeleBot("5295496237:AAHTEcijmhlKZ9lZuy4WQTg5cM0rQ1T1-6E")
channel_name = '@MyTry12'
#вариант рандомного выбора ниже, но мы его уже исключили
#with open('dictionary.txt', 'r', encoding='UTF-8') as file:
#    lines = file.readlines()
#    post = random.choice(lines)
# пока рабочий второй вариант  - сразу загружаем готовый список
f = open('dictionary.txt', 'r', encoding='UTF-8')
words = f.read().split('\n')
f.close()
# Пока не закончатся новые слова из загруженного файла, посылаем их в канал
#как сделать, чтоб можно было менять файл, и не надо было заново запускать?
for word in words:
    post=" "+"\n"+"\n"+word+"\n"+"\n"+"#беларускіюрыст"
    bot.send_message(channel_name, post)
    # Делаем паузу в один день?
    time.sleep(3600)

#    bot.send_message(channel_name, "Наш першы слоўнік скончыўся. Запрашаем у новую рабочую групу!")