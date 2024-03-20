import math
from math import sin, cos, sqrt, hypot, pi, pow
def test_filter():
    new_list = [8, 6, 11, 3, -1]
    assert list(filter(lambda n: n % 2 == 0, new_list)) == [8, 6]
    assert list(filter(lambda n: n < 0, new_list)) == [-1]
    assert list(filter(lambda n: n % 2 != 0, new_list)) == [11, 3, -1]

def test_map():
    new_list = [8, 3, -1]
    assert list(map(lambda n: n * 2, new_list)) == [16, 6, -2]
    assert list(map(lambda n: -n, new_list)) == [-8, -3, 1]

def test_sorted():
    new_list = [8, 3, -1]
    assert sorted(new_list) ==  [-1, 3, 8]
    assert sorted(sorted(new_list), reverse=True) == new_list

def test_pi():
    assert sin(pi / 2) == 1
    assert round(sin(pi / 6), 3) == 0.5
    assert cos(2 * pi) == 1

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(1024) == 32

def test_pow():
    assert pow(2, 10) == 1024
    assert pow(16, 0.25) == 2

def test_hypot():
    assert hypot(3, 4) == 5
    assert hypot(5, 12) == 13
