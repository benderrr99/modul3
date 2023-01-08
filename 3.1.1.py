x=float(input('Сумма вклада: '))
p=float(input('Проценты в год: '))
y=float(input('Сумму накопить: '))
year = x * (p / 100)
years = 0
while x < y:
    x = round(x + year, 2)
    years += 1
print(years)