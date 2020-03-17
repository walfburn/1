import pymorphy2

s = "Я люблю красное красивое яблоко."
lst = s.replace('.', '').split()
print(lst)

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

# Из исходников:
# PARTS_OF_SPEECH = frozenset([
#     'NOUN',  # имя существительное
#     'ADJF',  # имя прилагательное (полное)
#     'ADJS',  # имя прилагательное (краткое)
#     'COMP',  # компаратив
#     'VERB',  # глагол (личная форма)
#     'INFN',  # глагол (инфинитив)
#     'PRTF',  # причастие (полное)
#     'PRTS',  # причастие (краткое)
#     'GRND',  # деепричастие
#     'NUMR',  # числительное
#     'ADVB',  # наречие
#     'NPRO',  # местоимение-существительное
#     'PRED',  # предикатив
#     'PREP',  # предлог
#     'CONJ',  # союз
#     'PRCL',  # частица
#     'INTJ',  # междометие
# ])
