input_number = input('Введите элементы 1-го списка (разделители: "," ";" "/"): ')
numbers1 = input_number.replace(';', ',').replace('/', ',').split(',')
input_number = input('Введите элементы 2-го списка (разделители: "," ";" "/"): ')
numbers2 = input_number.replace(';', ',').replace('/', ',').split(',')
for namber in numbers1[:]:
    if namber in numbers2:
        numbers1.remove(namber)

print(numbers1)