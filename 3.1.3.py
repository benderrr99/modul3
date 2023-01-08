x=int(input('Введите целое число: '))
sum=0
while x!=0:
    sum=sum+x%10
    x=x//10
print('Сумма чисел равна:' + str(sum))