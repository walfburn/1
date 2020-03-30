import pymorphy2
import re

# data = 'Дай, Джим, на счастье лапу мне, Такую лапу не видал я сроду'


def lab4(data):
    data = re.sub(r'[^\w\s]', '', data)  # удаление пунктуации
    lst = data.split()  # текст разбит по словам

    morph = pymorphy2.MorphAnalyzer()

    countADJ = 0  # подсчет прилагательных
    countADVERB = 0  # подсчет наречий
    countVERB = 0  # подсчет глаголов

    for i in lst:
        l = morph.parse(i)[0]
        if l.tag.POS == ('ADJF' or 'ADJS'):
            countADJ += 1  # подсчет прилагательных
        elif l.tag.POS == 'ADVB':
            countADVERB += 1  # подсчет наречий
        elif l.tag.POS == ('VERB' or 'INFN'):
            countVERB += 1  # подсчет глаголов

    # print('В тексте найдено: '
    #       + str(countADJ) + ' прилагательных, '
    #       + str(countADVERB) + ' наречий, '
    #       + str(countVERB) + ' глаголов')

    return countADJ, countADVERB, countVERB


# print(lab4(data))

