quiz = {
    'Альберт Эйнштейн': 1879,
    'Винсент Ван Гог': 1853,
    'Мэрилин Монро': 1926,
    'Уолт Дисней': 1901,
    'Чарли Чаплин': 1889
}
# Ответы викторины
# ----------------
# Альберт Эйнштейн  1879
# Винсент Ван Гог   1853
# Мэрилин Монро     1926
# Уолт Дисней       1901
# Чарли Чаплин      1889

num_celebrity = 5
defis = 20
tour = 1
print('Викторина "Угадай год рождения знаменитости!"')
while True:
    print('-' * defis)
    print(f'Раунд №{tour}')
    print('-' * defis)

    true_answer = 0
    for celebrity, year in quiz.items():
        answer = int(input(f'Введите год рождения {celebrity} '))
        if answer == year:
            true_answer += 1

    print('-' * defis)
    print(f'Результаты раунда №{tour}')
    print('-' * defis)
    print(f'Количество правильных ответов: {true_answer}')
    print(f'Количество ошибок: {num_celebrity - true_answer}')
    print(f'Процент правильных ответов: {true_answer / num_celebrity * 100}%')
    print(f'Процент неправильных ответов: {(num_celebrity - true_answer) / num_celebrity * 100}% \n')
    print('-' * defis)
    repeat = ''
    while repeat != 'нет' and repeat != 'да':
        repeat = input('Хотите начать игру сначала? (да/нет) ')
    tour += 1
    if repeat == 'нет':
        break


