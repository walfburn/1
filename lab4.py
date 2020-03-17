import pymorphy2

s = "Я люблю яблоко."
lst = s.replace('.', '').split()
print(lst)

morph = pymorphy2.MorphAnalyzer()

for i in lst:
    l = morph.parse(i)[0]
    print(l.tag.POS)

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
