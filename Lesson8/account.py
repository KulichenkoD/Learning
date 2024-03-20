import json
import os

def init_account():
    if os.path.exists('acc.json'):
        with open('acc.json', 'r') as f:
            account = json.load(f)
    else:
        account = 0
        with open('acc.json', 'w') as f:
            json.dump(account, f)
    return account

def init_history():
    if os.path.exists('hist.json'):
        with open('hist.json', 'r') as f:
            hist = json.load(f)
    else:
        hist = []
        with open('hist.json', 'w') as f:
            json.dump(hist, f)
    return hist

def close_account(acc, hist):
    with open('acc.json', 'w') as f:
        json.dump(acc, f)
    with open('hist.json', 'w') as f:
        json.dump(hist, f)
def invalid_input():
    print('Введено не число!')

def bank_account():

    account = init_account()
    history = init_history()

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('---------------')
        print(f'На вашем счету: {account}')
        print('---------------')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                tick = int(input('Сумма пополнения: '))
                account += tick
            except:
                invalid_input()
        elif choice == '2':
            try:
                tick = int(input('Сумма покупки: '))
                if tick > account:
                    print('Недостаточно средств.')
                else:
                    account -= tick
                    goods = input('Название товара: ')
                    history.append((goods, tick))
            except:
                invalid_input()
        elif choice == '3':
            print(history)
        elif choice == '4':
            close_account(account, history)
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    bank_account()