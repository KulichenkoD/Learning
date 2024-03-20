def account_change(acc, summa):
    return acc + summa
def bank_account():
    account = 0
    history = []
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
            tick = int(input('Сумма пополнения: '))
            account = account_change(account, tick)
        elif choice == '2':
            tick = int(input('Сумма покупки: '))
            if tick > account:
                print('Недостаточно средств.')
            else:
                account = account_change(account, -tick)
                goods = input('Название товара: ')
                history.append((goods, tick))
        elif choice == '3':
            print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')