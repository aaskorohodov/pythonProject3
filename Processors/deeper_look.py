import random
import pandas as pd


def deeper_responde(message):
    df = pd.read_excel(r'C:\Users\Аркадий\Downloads\good2.xls', header=None)

    first = df[0]
    second = df[1]
    third = df[2]
    repl = df[3]

    keys = list(
        map(lambda a, b, c: str(a) + ' ' + str(b) + ' ' + str(c) + str(random.randint(1, 500)), first, second, third))

    my_dict = dict(zip(keys, repl))

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    for el in message:
        if el not in alphabet:
            message = message.replace(el, '')


    def first_look(message):
        result = []
        for el in my_dict.keys():
            if message in el:
                result.append(my_dict[el])
                if len(result) > 3:
                    print(result)
                    return random.choice(result)

        if len(result) == 0:
            res = trying(message)
            return res
        else:
            return (random.choice(result))


    def trying(message):
        mes_list = list(message.split())
        string = ''
        for i in range(len(mes_list) - 1):
            del mes_list[0]
            for el in mes_list:
                string += el + ' '
                trying = second_look(string)
                if trying != None:
                    return trying
            string = ''


    def second_look(mes):
        result = []
        for el in my_dict.keys():
            if mes in el:
                result.append(my_dict[el])
                if len(result) > 4:
                    return random.choice(result)
                else:
                    pass

        if len(result) == 0:
            pass
        else:
            return (random.choice(result))


    res = first_look(message)
    return res