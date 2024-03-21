import random
from random import sample
from collections import defaultdict

def update_1(example, k_5):
    ind =[]
    result = []
    for i in range(2):
        if k_5[i] < 5:
            ind.append(i)
    if ind:
        target = sample(ind, k=1)
        for i in range(3):
            if i == target[0]:
                result.append(example[0])
                k_5[i] += 1
            else:
                result.append('*')
    else:
        result.append('*')
        result.append('*')
        result.append(example[0])
        k_5[2] += 1
    return result, k_5

def update_2(example, k_5):
    result = []
    if k_5[0] == 5:
        result.append('*')
        result.append(example[0])
        result.append(example[1])
        k_5[1] += 1
        k_5[2] += 1
    else:
        if k_5[1] == 4:
            result.append(example[0])
            result.append('*')
            result.append(example[1])
            k_5[0] += 1
            k_5[2] += 1
        elif k_5[2] == 4:
            result.append(example[0])
            result.append(example[1])
            result.append('*')
            k_5[0] += 1
            k_5[1] += 1
        else:
            k_5[0] += 1
            result.append(example[0])
            if k_5[1] >= k_5[2]:
                result.append('*')
                result.append(example[1])
                k_5[2] += 1
            else:
                result.append(example[1])
                result.append('*')
                k_5[1] += 1
    return result, k_5
def numbers_in_cart(cart):
    numbers = set()
    for item in cart:
        numbers |= set(item)
    return numbers - {'*', '-'}
class Cart:
    def __init__(self):
        bag = set(i for i in range(1, 91))
        app = defaultdict(list)
        app_sort = defaultdict(list)
        count = 0
        zero = ['*', '*', '*']
        while count < 15:
            item = sample(list(bag), k=1)
            new = item[0] - 1
            if len(app[new // 10]) < 2:
                app[new // 10].append(new + 1)
                bag -= set(item)
                count += 1
        for i in range(9):
            app_sort[i] = sorted(app[i])
        k_5 = [0, 0, 0]
        for i in range(9):
            k = len(app_sort[i])
            if k == 0:
                app_sort[i] = zero
            elif k == 1:
                app_sort[i], k_5 = update_1(app_sort[i], k_5)
            else:
                app_sort[i], k_5 = update_2(app_sort[i], k_5)
        result = []
        for i in range(3):
            result.append([app_sort[key][i] for key in range(9)])
        self.cart = result
    def __str__(self):
        s = ' ' + '_' * 27 + '\n'
        for item in self.cart:
            s += '|'
            for char in item:
                s += f'{str(char):^3}'
            s += '|\n'
        s += ' ' + '-' * 27 + '\n'
        return s.replace('*', ' ')

    def __eq__(self, other):
        if isinstance(other, Cart):
            cart1 = numbers_in_cart(self.cart)
            cart2 = numbers_in_cart(other.cart)
            return len(cart1) == len(cart2) and cart1 == cart2

    def __ne__(self, other):
        if isinstance(other, Cart):
            cart1 = numbers_in_cart(self.cart)
            cart2 = numbers_in_cart(other.cart)
            return len(cart1) != len(cart2) or cart1 != cart2

    @property
    def is_empty(self):
        return len(numbers_in_cart(self.cart)) == 0

    def is_num_to_cart(self, num):
        return any([item.count(num) for item in self.cart])

    def crossing_out_nuber(self, num):
        for item in self.cart:
            try:
                index = item.index(num)
                item[index] = '-'
                break
            except ValueError:
                pass

class Player:
    def __init__(self, name, bot=False):
        self.cart = Cart()
        self.name = name
        self.bot = bot
        print(f'Имя игрока: {self.name}')

    def __str__(self):
        s = f'''Имя игрока: {self.name}
        Это - {'бот' if self.bot else 'человек '}'''
        return s

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name and (self.bot == other.bot)

    def __ne__(self, other):
        if isinstance(other, Player):
            return not (self.name == other.name and (self.bot == other.bot))

    def step(self, num):
        print(f'Карта игрока: {self.name}')
        print(self.cart)
        if self.bot:
            if self.cart.is_num_to_cart(num):
                self.cart.crossing_out_nuber(num)
                print('Номер есть')
            else:
                print('Номера нет в карточке')
            return True
        else:
            ans = input('Зачеркнуть цифру (Д/Н)? ')
            while ans not in 'ДдНн':
                ans = input('Некорректный ввод. Зачеркнуть цифру (Д/Н)? ')
            if ans in 'Дд':
                if self.cart.is_num_to_cart(num):
                    self.cart.crossing_out_nuber(num)
                    return True
                else:
                    return False
            else:
                if self.cart.is_num_to_cart(num):
                    return False
                else:
                    return True

class Game:
    bagful = list(range(1, 91))

    def __init__(self):
        name = input('Введите имя игрока: ')

        self.player = Player(name)
        self.bot = Player('Бот - Вася', bot=True)

    def __str__(self):
        s = f'''        Играют 2 игрока:
        -----------------
        {str(self.player)}
        {str(self.bot)}
        -----------------'''
        return s

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.bot == other.bot and self.player == other.player

    def __ne__(self, other):
        if isinstance(other, Game):
            return not (self.bot == other.bot and self.player == other.player)

    def start(self):

        while not (self.bot.cart.is_empty or self.player.cart.is_empty):
            num = sample(self.bagful, k=1)
            print(f'Выпал бочонок №: {num[0]}')
            self.bagful.remove(num[0])
            self.bot.step(num[0])
            step = self.player.step(num[0])
            if not (step and len(self.bagful)):
                break
            num = sample(self.bagful, k=1)
            print(f'Выпал бочонок: {num[0]}')
            self.bagful.remove(num[0])
        if self.bot.cart.is_empty or not step:
            winner = self.bot.name
        elif self.player.cart.is_empty:
            winner = self.player.name
        else:
            print('Все бочонки вынуты')
            return
        print()
        print("_" * 40)
        print(f"Победитель: {winner}")

if __name__ == '__main__':
    game = Game()
    #game.start()
    print(game)