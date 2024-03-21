from random import sample
import pytest
import mock
from loto import Cart, Player, Game

@pytest.mark.parametrize('arg', range(3))
def test_create(arg):
    cart = Cart()
    numbers = set()
    for item in cart.cart:
        numbers |= set(item)
    cart = numbers - {'*'}
    assert len(cart) == 15, 'В карточке количество чисел не равно 15'


@pytest.fixture
def fix():
    cart = Cart()
    cart.cart = [sample(['*', '-'], counts=[10, 20], k=10) for _ in range(3)]
    print(cart)
    return cart

def test_empty(fix):
    cart = fix
    assert cart.is_empty, "Должна быть карточка без цифр"

def test_not_empty():
    cart = Cart()
    assert not cart.is_empty, 'Карточка не должна быть пустая'

@pytest.fixture
def fix1():
    cart = Cart()
    cart.cart = ['*'] * 8 + [1]
    cart.cart = [cart.cart for _ in range(3)]
    return cart

@pytest.fixture
def fix2():
    cart = Cart()
    cart.cart = ['*'] * 9
    cart.cart = [cart.cart for _ in range(3)]
    return cart

def test_number_in_cart(fix1, fix2):
    assert fix1.is_num_to_cart(1), '1 должен быть в карте'
    assert not fix2.is_num_to_cart(1), '1 в карте, но чисел быть не должно'


@pytest.fixture
def fix3():
    cart = Cart()
    cart.cart = [[1, 10, 20, 30, 40, 'x', 'x', 'x', 'x'],
                 [2, 11, 21, 31, 41, 'x', 'x', 'x', 'x'],
                 [3, 12, 22, 32, 42, 'x', 'x', 'x', 'x']]
    return cart


def test_crossing_out_nuber(fix3):
    result_cart = [[1, 10, 20, 30, 40, 'x', 'x', 'x', 'x'],
                   [2, 11, '-', 31, 41, 'x', 'x', 'x', 'x'],
                   [3, 12, 22, 32, 42, 'x', 'x', 'x', 'x']]
    fix3.crossing_out_nuber(21)
    assert fix3.cart == result_cart, "Неправильно зачеркнута цифра"

def test_bot_step(fix3):
    bot = Player('Bot', bot=True)
    bot.cart = fix3
    assert bot.step(22), 'Неверный результат функции'
    print(bot.cart)
    assert bot.step(51), 'Результат функции должен быть False'

@pytest.mark.parametrize('num, y, result', ([21, 'д', True], [21, 'н', False], [51, 'д', False], [51, 'н', True]))
def test_human_step(fix3, num, y, result):
    with mock.patch('builtins.input', lambda x: y):
        player = Player('Player')
        player.cart = fix3
        assert player.step(num) is result, 'Error'

@pytest.fixture
def fix4():
    cart = Cart()
    cart.cart = [[ 1,   14,  22,  32, 40, 51, '*', 76,   86],
                 ['*', '*',  29,  33, 41, 53, '*', '*', '*'],
                 ['*', '*', '*', '*', 43, 52, '*', '*', '*']]
    return cart


def test_comp_step1(fix4):
    test_cart = [[ 1,   14,  22, '-', 40, 51, '*', 76,   86],
                 ['*', '*',  29,  33, 41, 53, '*', '*', '*'],
                 ['*', '*', '*', '*', 43, 52, '*', '*', '*']]
    bot = Player('Bot', bot=True)
    bot.cart = fix4
    bot.step(32)
    assert bot.cart.cart == test_cart, 'Error'
    bot.step(34)
    assert bot.cart.cart == test_cart, 'Error'


def test_comp_num(fix4):
    bot = Player('Bot', bot=True)
    bot.cart = fix4
    assert bot.cart.is_num_to_cart(32), "Есть номер"
    assert not bot.cart.is_num_to_cart(34), "Нет номера"
