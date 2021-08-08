import random
import time
import telebot
from telebot import types
from PIL import Image
from Processors.log import log


bot = telebot.TeleBot('1879041775:AAG14Vz9P4AP4hjOGOOwYKbbFJGFSrWQEgs')
stop = ['все', 'Все', 'ВСЕ', 'ВСе', 'всё', 'ВСё', 'ВСЁ', 'Всё', 'dct', 'Dct', 'DCt', 'DCT', 'dc`', 'Dc`', 'DC`', 'DC~']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    from Processors.user_recognition import user_recognition
    name = user_recognition(message.from_user.id)
    if name == False:
        send_mess = 'Кажется, мы еще не знакомы! Как тебя зовут?'
        bot.send_message(message.chat.id, send_mess)
        log(message.text, message.from_user.username, send_mess)
        def whats_ur_name(message):
            excl = ['меня', 'зовут', 'я', 'а', 'тебя', 'как', 'звать', 'name', 'my', 'зови', 'пускай', 'будет']
            name = ''
            for el in message.text.split():
                if el not in excl:
                    name += el
            from Processors.user_recognition import new_user
            new_user(message.from_user.id, name)
            bot.send_message(message.chat.id, 'Отлично, теперь давай начнем сначала')
            log(message.text, message.from_user.username, send_mess)
            time.sleep(2)
            send_welcome(message)
        bot.register_next_step_handler(message, whats_ur_name)
    else:
        send_mess = f'Привет {name}! Вот что умеет этот бот:\n' \
                    f'\n' \
                    f'/start – включить бота/начать общение с начала\n' \
                    f'/math – разная матиматика' \
                    f'/calc – открыть калькулятор\n' \
                    f'/stuff – всякие штуки\n' \
                    f'/name – изменить свое имя\n' \
                    f'\n' \
                    f'А еще могу говорить.'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)


@bot.message_handler(commands=['stuff', 'reversed', 'popka', 'time', 'pics', 'weather', 'food', 'covid', 'anagramm',
                               'letters', 'timer'])
def staff_handler(message):
    if message.text == '/stuff':
        send_mess = '/reversed – слова наоборот\n' \
                    '/popka – попугай\n' \
                    '/time – узнать время в любом городе\n' \
                    '/weather – узнать погоду\n' \
                    '/food – подскажет что поесть\n' \
                    '/pics – даст случайную картинку\n' \
                    '/covid – даст статистику по ковиду\n' \
                    '/anagramm – поиск анаграмм\n' \
                    '/letters – считает повторы букв'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)

    elif message.text == '/reversed':
        send_mess = 'Все что вы напишите, будет перевернуто.\n' \
                    'Для выхода пиши "все"'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)
        def reversed(message):
            if message.text in stop:
                send_mess = 'reversed остановлен.\n' \
                            '/start для продолжения'
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.chat.id, send_mess)
            else:
                from Processors.stuff import reversed_words
                send_mess = reversed_words(message.text)
                bot.send_message(message.chat.id, send_mess)
                log(message.text, message.from_user.username, send_mess)
                bot.register_next_step_handler(message, reversed)
        bot.register_next_step_handler(message, reversed)

    elif message.text == '/popka':
        def popca_pross(message):
            if message.text in stop:
                send_mess = 'Popka завершен\n' \
                            '/start для продолжения'
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.from_user.id, send_mess)
            else:
                from Processors.stuff import popka_talking
                send_mess = popka_talking(message.text)
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.from_user.id, send_mess)
                bot.register_next_step_handler(message, popca_pross)
        send_mess = 'Пишите что хотите, когда надоест, напишите "все".'
        bot.send_message(message.chat.id, send_mess)
        log(message.text, message.from_user.username, send_mess)
        bot.register_next_step_handler(message, popca_pross)

    elif message.text == '/time':
        send_mess = 'Какой город смотрим?'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)
        def time_get(message):
            from Processors.time import output
            send_mess = output(message.text)
            log(message.text, message.from_user.username, send_mess)
            bot.send_message(message.chat.id, send_mess)
        bot.register_next_step_handler(message, time_get)

    elif message.text == '/pics':
        t = [i for i in range(204)]
        ran = str(random.choice(t))
        name = fr'C:\Users\Аркадий\Pictures\py\1 ({ran}).JPG'
        png = Image.open(name)
        send_mess = 'Вот:'
        bot.send_message(message.chat.id, send_mess)
        log(message.text, message.from_user.username, send_mess)
        bot.send_photo(message.from_user.id, png)

    elif message.text == '/weather':
        send_mess = 'Какой город?'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.from_user.id, send_mess)

        def weather_pros(message):
            from Processors.weather_udvanced import wf_output
            send_mess = wf_output(message.text)
            log(message.text, message.from_user.username, send_mess)
            bot.send_message(message.from_user.id, send_mess)

        bot.register_next_step_handler(message, weather_pros)

    elif message.text == '/food':
        markup = telebot.types.InlineKeyboardMarkup()

        self = types.InlineKeyboardButton(text='Готовим сами', callback_data="self")
        fast = types.InlineKeyboardButton(text='Готовое дома', callback_data="fast")
        outdoor = types.InlineKeyboardButton(text='Сходить в...', callback_data="outdoor")
        markup.add(self, fast, outdoor)

        send_mess = 'Что хочется?'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.from_user.id, send_mess, reply_markup=markup)

    elif message.text == '/covid':
        log(message.text, message.from_user.username)
        from Processors.covid import covid
        covid(message)

    elif message.text == '/anagramm':
        send_mess = 'Дайте текст, а я найду в нем анаграммы.\n' \
                    '\n' \
                    '*поддерживается только английский и русский'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.from_user.id, send_mess)
        def anagramms_pross(message):
            from Processors.stuff import anagrams
            send_mess = anagrams(message.text)
            log(message.text, message.from_user.username, send_mess)
            bot.send_message(message.from_user.id, send_mess)
        bot.register_next_step_handler(message, anagramms_pross)

    elif message.text == '/letters':
        send_mess = 'Дайте текст, а я посчитаю повторы букв'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.from_user.id, send_mess)
        def letters(message):
            from Processors.stuff import letters_counter
            send_mess = letters_counter(message.text)
            log(message.text, message.from_user.username, send_mess)
            bot.send_message(message.from_user.id, send_mess)
        bot.register_next_step_handler(message, letters)

    elif message.text == '/timer':
        send_mess = 'Задайте число секунд, которые таймер будет работать'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.from_user.id, send_mess)
        def timer(message):
            send_mess = 'Ready!'
            log(message.text, message.from_user.username, send_mess)
            tim = int(message.text)
            msq = bot.send_message(message.chat.id, send_mess)
            for i in range(tim + 1):
                def timer(message, i):
                    time.sleep(1)
                    bot.edit_message_text(i, chat_id=message.chat.id, message_id=msq.message_id)
                timer(message, i)
            send_mess = f'Таймер сработал! Прошло {tim} секунд'
            bot.send_message(message.from_user.id, send_mess)
        bot.register_next_step_handler(message, timer)




@bot.message_handler(commands=['math', 'calc', 'area', 'bmi'])
def math_handler(message):
    if message.text == '/math':
        send_mess = 'Это матиматический модуль. Вот что умеет:\n' \
                    '\n' \
                    '/calc – калькулятор\n' \
                    '/area – площадь прямоугольника\n' \
                    '/bmi – рассчет массы тела'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)

    elif message.text == '/calc':
        send_mess = 'Это калькулятор. Вводите выражения "как обычно", а я попробую их посчитать.\n' \
                    'Например: "2*5", "5/5", "5+4" и так далее.\n' \
                    '\n' \
                    'Когда надоест, отправьте мне "все"'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)

        def calc_pros(message):
            if message.text in stop:
                send_mess = 'Калькулятор закрыт.\n' \
                            '/start для продолжения'
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.from_user.id, send_mess)
            else:
                from Processors.calc import calc
                send_mess = calc(message.text)
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.from_user.id, send_mess)
                bot.register_next_step_handler(message, calc_pros)

        bot.register_next_step_handler(message, calc_pros)

    elif message.text == '/area':
        send_mess = 'Тут можно поссчитать площадь прямоугольника.\n' \
                    'Когда надоест, напиши "все"\n' \
                    '\n' \
                    'Введите две стороны'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)
        def area_handler(message):
            if message.text in stop:
                send_mess = 'area остановлен.\n' \
                            '/start для продолжения'
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.chat.id, send_mess)
            else:
                from Processors.math import area
                send_mess = area(message.text)
                bot.send_message(message.chat.id, send_mess)
                log(message.text, message.from_user.username, send_mess)
                bot.register_next_step_handler(message, area_handler)

        bot.register_next_step_handler(message, area_handler)

    elif message.text == '/bmi':
        send_mess = 'Тут можно рассчитать индекс массы тела.'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)
        time.sleep(1.5)
        send_mess = 'Какой у тебя рост?'
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.chat.id, send_mess)
        def height(message):
            height = message.text
            send_mess = 'А какой вес?'
            log(message.text, message.from_user.username, send_mess)
            bot.send_message(message.chat.id, send_mess)
            def weight(message):
                weight = message.text
                from Processors.math import bmi
                send_mess = bmi(height, weight)
                log(message.text, message.from_user.username, send_mess)
                bot.send_message(message.chat.id, send_mess)
            bot.register_next_step_handler(message, weight)
        bot.register_next_step_handler(message, height)


@bot.message_handler(commands=['name'])
def name_change(message):
    send_mess = 'Как мне тебя называть?'
    log(message.text, message.from_user.username, send_mess)
    bot.send_message(message.from_user.id, send_mess)
    def name_change(message):
        from Processors.user_recognition import name_change
        name_change(message.from_user.id, message.text)
        send_mess = 'Готово, теперь я буду звать тебя ' + message.text
        log(message.text, message.from_user.username, send_mess)
        bot.send_message(message.from_user.id, send_mess)
    bot.register_next_step_handler(message, name_change)


@bot.message_handler(content_types=['text'])
def messages(message):
    print(message)
    from Processors.text_respond import respond_processor
    send_mess = respond_processor(message)
    log(message.text, message.from_user.username, send_mess)
    bot.send_message(message.from_user.id, send_mess)


@bot.message_handler(content_types=['photo'])
def photo(message):
    send_mess = 'О, картинка! Что мне с ней делать?'
    log(message.text, message.from_user.username, send_mess)
    bot.send_message(message.from_user.id, send_mess)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    from Processors.food_processor import food_handler
    food_handler(call)




while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        import time
        print(e)
        time.sleep(0.5)