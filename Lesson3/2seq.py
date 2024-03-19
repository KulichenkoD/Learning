input_number = input('Введите список чисел через один из разделителей ("," ";" "/"): ')
numbers = input_number.replace(';', ',').replace('/', ',').split(',')
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print(result)