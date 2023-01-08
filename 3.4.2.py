import json
def register (log, pwd):
    with open('1.json', 'r') as f:
        data=json.load(f)
    if log in data.keys():
        print('Логин занят!')
    else:
        data[log] = pwd
        print('Регистрация успешно!')
    with open('1.json', 'w') as f:
        json.dump(data, f)
    return (log, pwd)
log = input('Введите логин: ')
pwd = input('Введите пароль: ')
print (register(log, pwd))