import requests, bs4, time, telebot


bot = telebot.TeleBot('1879041775:AAG14Vz9P4AP4hjOGOOwYKbbFJGFSrWQEgs')


def covid(message):
    html = requests.get('https://xn--80aesfpebagmfblc0a.xn--p1ai/')
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    class_all = soup.find_all(class_='cv-countdown__item-value _accent')
    cases_today = class_all[1].getText()
    cases_all = class_all[0].getText()


    send_mess = f'Всего случаев заражения в России: {cases_all}\n' \
                f'Случаи заражения за сегодня: {cases_today}\n' \
                f'Данный предосталенны сайтом стопкоронавирус.рф'


    msq = bot.send_message(message.chat.id, 'Получаю статистику...')
    time.sleep(0.5)
    bot.edit_message_text("Получаю статистику....", chat_id=message.chat.id, message_id=msq.message_id)
    time.sleep(0.5)
    bot.edit_message_text("Получаю статистику.....", chat_id=message.chat.id, message_id=msq.message_id)
    time.sleep(0.5)
    bot.edit_message_text("Получаю статистику......", chat_id=message.chat.id, message_id=msq.message_id)
    time.sleep(0.5)
    bot.edit_message_text("Получаю статистику.......", chat_id=message.chat.id, message_id=msq.message_id)
    time.sleep(0.5)
    bot.edit_message_text("Получаю статистику.........", chat_id=message.chat.id, message_id=msq.message_id)
    time.sleep(0.5)
    bot.edit_message_text("Получаю статистику..........", chat_id=message.chat.id, message_id=msq.message_id)
    bot.send_message(message.chat.id, send_mess)