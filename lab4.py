import pymorphy2
import re

s = "Я люблю красное, красивое яблоко."
s = re.sub(r'[^\w\s]','',s)  # удаление пунктуации
lst = s.split()  # текст разбит по словам

morph = pymorphy2.MorphAnalyzer()

countADJ = 0
countADVERB = 0
countVERB = 0

for i in lst:
    l = morph.parse(i)[0]
    print(l.tag.POS)
    if l.tag.POS == ('ADJF' or 'ADJS'):
        countADJ += 1  # подсчет прилагательных
    elif l.tag.POS == 'ADVB':
        countADVERB += 1  # подсчет наречий
    elif l.tag.POS == ('VERB' or 'INFN'):
        countVERB += 1  # подсчет глаголов

print(countADJ)
