count = int(input('Введите количество элементов: '))
result = []
for i in range(count):
    elem = int(input(f'Введите элемент №{i+1}: '))
    result.append(elem)
result.sort()
print(result)