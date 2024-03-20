import os
import sys
import shutil
from victory import victorina
from account import bank_account

def mk_dir(file):
    if not os.path.exists(f'{file}'):
        os.mkdir(f'{file}')

def del_file_dir(file):
    if os.path.exists(f'{file}'):
        os.rmdir(f"{file}") if os.path.isdir(f'{file}') else os.remove(f'{file}')

def file_copy(file1, file2):
    if os.path.exists(f'{file1}'):
        shutil.copy(file1, file2)

def list_dirs_files(files=False):
    if files:
        return [f for f in os.listdir() if os.path.isfile(f)]
    else:
        return [f for f in os.listdir() if os.path.isdir(f)]
def save_listdir():
    spisok = 'files: ' + ', '.join(str(s) for s in list_dirs_files(files=True))
    spisok += '\ndirs: '+ ', '.join(str(s) for s in list_dirs_files())
    with open('listdir.txt', 'w') as f:
        f.write(spisok)

def console_manager():
    while True:
        print('-' * 20)
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. сохранить содержимое рабочей директории в файл')
        print('6. посмотреть только папки')
        print('7. посмотреть только файлы')
        print('8. просмотр информации об операционной системе')
        print('9. создатель программы')
        print('10. играть в викторину')
        print('11. мой банковский счет')
        print('12. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            file = input('Название папки: ')
            mk_dir(file)
        elif choice == '2':
            file = input('Название папки или файла: ')
            del_file_dir(file)
        elif choice == '3':
            file1 = input('Имя файла: ')
            file2 = input('Новое имя файла: ')
            file_copy(file1, file2)
        elif choice == '4':
            print(os.listdir())
        elif choice == '5':
            save_listdir()
            print('Выполнено')
        elif choice == '6':
            print(list_dirs_files())
        elif choice == '7':
            print(list_dirs_files(files=True))
        elif choice == '8':
            print(sys.platform, '(', os.name, ')')
        elif choice == '9':
            print('Дмитрий Куличенко')
        elif choice == '10':
            victorina()
        elif choice == '11':
            bank_account()
        elif choice == '12':
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    console_manager()
