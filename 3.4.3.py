import json
def login_function (log, pwd):
    with open('1.json', 'r') as f:
        data=json.load(f)
    if log in data.keys():
        if data[log] == pwd:
            print('Успешный вход!!! Добро пожаловать!')
    else:
        print('Неверный логин или пароль!')
    return (log, pwd)
log = input('Введите логин: ')
pwd = input('Введите пароль: ')
print (login_function(log, pwd))
