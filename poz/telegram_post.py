#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def post(message,chat_id):
	#subprocess.call("curl --header 'Content-Type: application/json' --request 'POST' --data '{\x22chat_id\x22:\x22-267211915\x22,\x22text\x22:"Одын одын"}' \x22https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage\x22")
	#subprocess.call(["curl", "--header" ,"'Content-Type: application/json'" ,"--request" ,"'POST'" ,"--data" ,"'{'chat_id':'-267211915','text':"Одын одын'}'","https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"])
	subprocess.call(["curl", "-s", "-X", "POST", "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage", "-d", "chat_id="+chat_id, "-d", "text="+message])
#post("О, да","-267211915")

#curl -s -X POST https://api.telegram.org/bot<ТОКЕН>/sendMessage -d chat_id=<ID_ЧАТА> -d text="Hello World"
#curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"-267211915","text":"test message here"}' "https://api.telegram.org/bot885329435:AAHTWnyjFEzy_NMp4Os64Y8V_vmECgdimQA/sendMessage"

#App api_id:24694269
#App api_hash:3cf29c5fed7191044c41ccadb4cf703a
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigvO/vBfqACJLZtS7QMgCGXJ6XIR
# yy7mx66W0/sOFa7/1mAZtEoIokDP3ShoqF4fVNb6XeqgQfaUHd8wJpDWHcR2OFwv
# plUUI1PLTktZ9uW2WE23b+ixNwJjJGwBDJPQEQFBE+vfmH0JP503wr5INS1poWg/
# j25sIWeYPHYeOrFp/eXaqhISP6G+q2IeTaWTXpwZj4LzXq5YOpk4bYEQ6mvRq7D1
# aHWfYmlEGepfaYR8Q0YqvvhYtMte3ITnuSJs171+GDqpdKcSwHnd6FudwGO4pcCO
# j4WcDuXc2CTHgH8gFTNhp/Y8/SpDOhvn9QIDAQAB
# -----END RSA PUBLIC KEY-----
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g
# 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO
# 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/
# +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9
# t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs
# 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB
# -----END RSA PUBLIC KEY-----

# Захотелось как-то мне, чтобы сообщения одного из чатов телеграма сохранялись у меня на диске (не запуская обычного клиента). Не буду раскрывать своих побудительных мотивов, но возможность эта показалась мне нужной и полезной.

# Для этого в телеграме есть боты. На Хабре есть несколько статей, посвященных ботам, например: "Чат-помощник на сайт".

# Бот позволяет читать и посылать сообщения, для регистрации бота не нужен телефон и количество ботов может быть любым. Но название бота включает в себя слово "bot", что может вызвать у хозяина чата ненужные вопросы.

# Но, как говорится, правильно поставленный вопрос — половина ответа.

# Оказывается кроме "API telegram bot" существует еще и "API telegram client", т.е. API для создания собственных клиентов.

# Клиент также может посылать и читать сообщения, но только от зарегестрированного (привязанного к телефону) пользователя, что мне как раз подходит (я уже зарегестрирован в чате).

# На сайте телеграма есть список API для разных платформ: https://telegram.org/apps#source-code

# Однако, самой простой в использовании оказалась библиотека на python: Pure Python 3 MTProto API Telegram client library под названием "telethon"

# Только вот проблема. Я не знаю питон. Ну что ж, есть повод познакомиться.
# Как утверждает мануал по телетону, инсталляция его очень простая. Достаточно запустить команду в командной строке:

# pip3 install telethon

# Подводные камни, встреченные мною при инсталляции:

#     не инсталлирован pip3 (инсталлятор для питона).

# sudo apt-get -y install python3-pip

#     Библиотека работает только на питоне версии >3.5. Так что, возможно, придется его обновить.

# Все установилось. Листаем readme.txt дальше.

# Следущим пунктом идет создание клиента телеграма… Как, уже? Ну да, все просто. Правда, сперва нужно зарегистритровать себя как создателя клиента.

# Заходим на сайт телеграма: https://my.telegram.org
# Вводим телефон и ждем код подтверждения на родном клиенте телеграма. Он довольно длинный (12 символов) и неудобный для ввода.

# Заходим в пункт "API". Ищем "Telegram API" и заходим в "Creating an application" (https://my.telegram.org/apps).

# Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.

# Пришла пора делать клиента.

# from telethon import TelegramClient, sync

# # Вставляем api_id и api_hash
# api_id = 12345
# api_hash = '0123456789abcdef0123456789abcdef'

# client = TelegramClient('session_name', api_id, api_hash)
# client.start()

# session_name — можно вставить любое имя. Вас попросят ввести телефон и пришлют код подтверждения. После этого клиент будет работать без запроса телефона (до тех пор, пока не поменяете session_name). Рядом с вашей программой появится файл session_name.session

# Если ошибок нет, клиент готов. Только вот, ничего не выводит. Попробуем получить полезную инфорфмацию.

# Узнаем немного о себе:

# print(client.get_me().stringify())

# результат выдается в виде:

# User(
#     photo=None,
#     last_name='Pupkin',
#     first_name='Vasya',
#     id=123456789,
#     phone='79041234567',
# .... - что-то еще...
# )

# Можем послать сообщение от себя:

# client.send_message('username', 'Hello! Talking to you from Telethon')

# Можно и картинку

# client.send_file('username', '/home/myself/Pictures/holidays.jpg')

# Как меня видят другие:

# client.download_profile_photo('me')

# Смотрим, на какие чаты мы подписаны:

# print all chats name
# for dialog in client.iter_dialogs():
#     print(dialog.title)

# читаем все сообщения чата "chat_name" (осторожно, сообщений может быть очень много)

# messages = client.get_entity('chat_name')
# print(messages)

# просмотр всех пользователей чата

# participants = client.get_participants('chat_name')
# print(participants)

# Побаловались?
# Теперь, собственно, делаем то, ради чего мы все это затеяли...

# Нам нужна программка, следящая за новыми сообщениями в определенном канале.

# Чтобы клиент не заканчивал работу, после client.start() вставляем строку:

# client.run_until_disconnected()

# Эта конструкция (вставляется перед client.start()) выводит только новые сообщения:

# @client.on(events.NewMessage(chats=('chat_name')))
# async def normal_handler(event):
# #    print(event.message)
#     print(event.message.to_dict()['message'])

# Давайте разберемся.

# @client.on(events.NewMessage(chats=('chat_name')))

# создает событие, срабатывающее при появлении нового сообщения

#  print(event.message)

# выводит сообщение в таком виде:

# Message(edit_date=None, views=None, reply_markup=None, fwd_from=None, id=187, entities=[], post=False, mentioned=False, via_bot_id=None, media_unread=False, out=True, media=None, date=datetime.datetime(2018, 10, 1, 9, 26, 21, tzinfo=datetime.timezone.utc), to_id=PeerChannel(channel_id=123456789), reply_to_msg_id=None, from_id=123456789, silent=False, grouped_id=None, post_author=None, message='hello telegram')

# Из всего этого нам нужно поле: "message='hello telegram'":

#     print(event.message.to_dict()['message'])

# Сообщение получили, но от кого оно, непонятно, т.к. в сообщение только ID пользователя. Чтобы сопоставить ID и имя пользователя, скачиваем всех пользователей чата и помещаем их в словарь (хэш) в виде d[id]="first_name last_name"

# participants = client.get_participants(group)
# users={}

# for partic in client.iter_participants(group):
#     lastname=""
#     if partic.last_name:
#        lastname=partic.last_name
#     users[partic.id]=partic.first_name+" "+lastname

# Теперь мы можем узнать, кто послал сообщение:

# s_user_id=event.message.to_dict()['from_id']
# user_id=int(s_user_id)
# user=d.get(user_id)

# В принципе, можно получить имя пользователя из телеграма напрямую, но если пользователей немного, проще со словарем.

# Вытаскиваем из сообщения дату отправки:

# mess_date=event.message.to_dict()['date']

# Все, все данные у нас есть. Осталось записать их в файл.
# Для этого сначала откроем файл на запись:

# f=open('messages_from_chat', 'a') 

# И запишем сообщение:

# f.write(mess_date.strftime("%d-%m-%Y %H:%M")+"\n")
# f.write(user+"\n")
# f.write(user_mess+"\n\n")
# f.flush()

# Вот и все! Все, что мне было нужно, программка делает. Утилитка, конечно, сыровата, но свою задачу выполняет.

# Python оказался не таким уж и сложным как его малюют, тем более описание и разных библиотек в интернете полным-полно. Написать еще пару утилиток и привыкнув к нему, можно использовать его как скриптовый язык вместо bash.

# Весь текст утилиты:

# from telethon import TelegramClient, sync, events

# api_id = 12345
# api_hash = '0123456789abcdef0123456789abcdef'

# client = TelegramClient('session_name', api_id, api_hash)

# @client.on(events.NewMessage(chats=('chat_name')))
# async def normal_handler(event):
# #    print(event.message)
#     user_mess=event.message.to_dict()['message']

#     s_user_id=event.message.to_dict()['from_id']
#     user_id=int(s_user_id)
#     user=d.get(user_id)

#     mess_date=event.message.to_dict()['date']

#     f.write(mess_date.strftime("%d-%m-%Y %H:%M")+"\n")
#     f.write(user+"\n")
#     f.write(user_mess+"\n\n")

#     f.flush()

# client.start()

# group='group_name'

# participants = client.get_participants(group)
# users={}

# for partic in client.iter_participants(group):
#     lastname=""
#     if partic.last_name:
#        lastname=partic.last_name
#     users[partic.id]=partic.first_name+" "+lastname

# f=open('messages_from_chat', 'a') 

# client.run_until_disconnected()
# f.close()

# Полное описание библиотеки.