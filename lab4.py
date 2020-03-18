import pymorphy2
import re


handle = open("text.txt", "r")
data = handle.read()
data = re.sub(r'[^\w\s]','', data)  # удаление пунктуации
lst = data.split()  # текст разбит по словам

morph = pymorphy2.MorphAnalyzer()

countADJ = 0
countADVERB = 0
countVERB = 0

for i in lst:
    l = morph.parse(i)[0]
    if l.tag.POS == ('ADJF' or 'ADJS'):
        countADJ += 1  # подсчет прилагательных
    elif l.tag.POS == 'ADVB':
        countADVERB += 1  # подсчет наречий
    elif l.tag.POS == ('VERB' or 'INFN'):
        countVERB += 1  # подсчет глаголов

print('В тексте найдено: '
      + str(countADJ) + ' прилагательных, '
      + str(countADVERB) + ' наречий, '
      + str(countVERB) + ' глаголов')

handle.close()

