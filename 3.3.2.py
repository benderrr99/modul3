import re
s='''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того.
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви'''
e=[]
def list (s):
    a = s.replace('-', '')
    b = re.sub(r'[,|.|\n]', ' ', a)
    c = b.replace('  ', ' ')
    d = c.split(' ')
    for i in d:
        if len(i)<5:
            e.append(i)
    return e
print(list(s))
