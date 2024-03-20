import os
import sys
import shutil
from f_victory import victorina
from f_account import bank_account

def file_copy(file1, file2):
    if os.path.exists(f'{file1}'):
        shutil.copy(file1, file2)

if '__name__' == '__main__':
    while True:
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('10. мой банковский счет')
        print('11. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            file = input('Название папки: ')
            if not os.path.exists(f'{file}'):
                os.mkdir(f'{file}')
        elif choice == '2':
            file = input('Название папки или файла: ')
            if os.path.exists(f'{file}'):
                if os.path.isdir(f'{file}'):
                    os.rmdir(f"{file}")
                else:
                    os.remove(f'{file}')
        elif choice == '3':
            file1 = input('Имя файла: ')
            file2 = input('Новое имя файла: ')
            if os.path.exists(f'{file1}'):
                shutil.copy(file1, file2)
        elif choice == '4':
            print(os.listdir())
        elif choice == '5':
            print([f for f in os.listdir() if os.path.isdir(f)])
        elif choice == '6':
            print([f for f in os.listdir() if os.path.isfile(f)])
        elif choice == '7':
            print(sys.platform, '(', os.name, ')')
        elif choice == '8':
            print('Дмитрий Куличенко')
        elif choice == '9':
            victorina()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            break
        else:
            print('Неверный пункт меню')
