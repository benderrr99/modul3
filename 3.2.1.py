l = [1,4,1,6,'hello','a',5,'hello']
b = []
for item in l:
    count = 0
    for x in l:
        if x == item:
            count += 1
    b.append(count)
dubble = set()
index = 0
while index < len(l) :
    if b[index] != 1 :
        dubble.add(l[index])
    index += 1
print('Основной список: ', l)
print('Дубликаты в списке: ', dubble)
