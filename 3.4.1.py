import json
data={}
def register (log, pwd):
    data[log] = pwd
    print('Регистрация успешно!')
    with open('1.json', 'w') as f:
        json.dump(data, f)
    return (log, pwd)
log = input('Введите логин: ')
pwd = input('Введите пароль: ')
print (register(log, pwd))