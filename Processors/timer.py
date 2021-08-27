import random
import time
import telebot
from telebot import types
from Processors.log import log


bot = telebot.TeleBot('1879041775:AAG14Vz9P4AP4hjOGOOwYKbbFJGFSrWQEgs')


value = ''
old_value = ''
data = ''


def timer_time(call, v):
    global value, old_value, data
    what_is_it = v
    v = v.split(':')
    if len(v) < 2:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='?', reply_markup=markup)
        bot.send_message(call.message.chat.id, f'Используйте формат мм:сс, или м:с, или м:ссссс...\n'
                                               f'В общем добавьте ":" а то ниче непонятно – {what_is_it} чего?')
        value = ''
        old_value = ''
        data = ''
    elif len(v) > 2:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='?',
                              reply_markup=markup)
        bot.send_message(call.message.chat.id, f'Слишком много ::::')
        value = ''
        old_value = ''
        data = ''

    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ready')
        time.sleep(1)

        secs = (int(v[0]) * 60) + int(v[1])
        secs = int(secs)
        m, s = divmod(secs, 60)
        done = '{:02d} минут {:02d} секунд'.format(m, s)
        if secs > 3600:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{done}?')
            time.sleep(2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Чтож, это твой выбор')
            time.sleep(2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Меня уже не остановить')
            time.sleep(2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Поехали!')
            time.sleep(1)

            secs = secs - 7

            while secs != -1:
                m, s = divmod(secs, 60)
                h, m = divmod(m, 60)
                d, h = divmod(h, 24)
                min_sec = 'дни {:02d} часы {:02d} минуты {:02d} секунды {:02d}'.format(d, h, m, s)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=min_sec)
                time.sleep(1)
                secs -= 1

            bot.send_message(call.message.chat.id, f'Готово! Прошло {done}\n'
                                                   f'Еще? /timer')
            value = ''
            old_value = ''
            data = ''
        else:
            while secs != -1:
                m, s = divmod(secs, 60)
                min_sec = '{:02d}:{:02d}'.format(m, s)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=min_sec)
                time.sleep(1)
                secs -= 1

            bot.send_message(call.message.chat.id, f'Готово! Прошло {done}\n'
                                                   f'Еще? /timer')
            value = ''
            old_value = ''
            data = ''


def keyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='1', callback_data="1"),
               telebot.types.InlineKeyboardButton(text='2', callback_data="2"),
               telebot.types.InlineKeyboardButton(text='3', callback_data="3"))
    markup.row(telebot.types.InlineKeyboardButton(text='4', callback_data="4"),
               telebot.types.InlineKeyboardButton(text='5', callback_data="5"),
               telebot.types.InlineKeyboardButton(text='6', callback_data="6"))
    markup.row(telebot.types.InlineKeyboardButton(text='7', callback_data="7"),
               telebot.types.InlineKeyboardButton(text='8', callback_data="8"),
               telebot.types.InlineKeyboardButton(text='9', callback_data="9"))
    markup.row(telebot.types.InlineKeyboardButton(text='0', callback_data="0"))
    markup.row(telebot.types.InlineKeyboardButton(text=':', callback_data=":"),
               telebot.types.InlineKeyboardButton(text='del', callback_data="del"))
    markup.row(telebot.types.InlineKeyboardButton(text='start', callback_data="start"))

    return markup
markup = keyboard()


def timer_step1(message, name):
    send_mess = f'Привет {name}\n' \
                f'Я таймер'
    log(message.text, message.from_user.username, send_mess)
    bot.send_message(message.from_user.id, send_mess, reply_markup=markup)


def timer_pross(call):
    call_data_data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', 'del', 'start']
    if call.data in call_data_data:
        global value, old_value, data
        data = call.data

        if value == '' and data == 'del':
            stop = ['все', 'хватит', 'перестань', 'остановись', 'заебал', 'сука хватит', 'чисто уже', 'да блять', 'пиши',
                    'пиши цифры', 'цифры ставь!', 'едрен батон', 'ОСтоновИсь', ':|', ':(', ':/', 'стой']
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=random.choice(stop),
                                  reply_markup=markup)
            time.sleep(0.2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=':)',
                                  reply_markup=markup)
        else:
            if data != 'start' and data != 'del':
                value += data
            elif data == 'del':
                value = value[0:-1]
                if value == '':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=':)', reply_markup=markup)

            if value != old_value and value != '':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=value, reply_markup=markup)

            old_value = value

            if data == 'start' and value != '':
                timer_time(call, value)

            if data == 'start' and value == '':
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='00:00')
                bot.send_message(call.message.chat.id, f'Готово! Прошло 00 минут 00 секунд. Это было быстро, неправда ли? '
                                                       f'Может теперь по-нормальному? /timer')