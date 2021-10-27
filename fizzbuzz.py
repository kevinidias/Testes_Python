"""
Regras do fizzbuzz

1- Se a posição for múltipla de 3: fizz.
2- Se a posição for múltipla de 5: buzz.
3- Se a posição for múltipla de 3 e 5: fizzbuzz.
4- Para qualquer outra posição fale o próprio número.

Primeiramente escrevemos as regras, depois o código.
"""

from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)

"""def multiple_of_5(num):
    return multiple_of(5, num)


def multiple_of_3(num):
    return multiple_of(3, num)"""


def robot(pos):
    say = str(pos)
    if multiple_of_3(pos) and multiple_of_5(pos):
    #if pos % 3 == 0 and pos % 5 == 0:
        say = 'fizzbuzz'

    elif multiple_of_5(pos):
    #elif pos % 5 == 0:
        say = 'buzz'
    elif multiple_of_3(pos):
    #elif pos % 3 == 0:
        say = 'fizz'

    return say

"""    if pos == 15:
        return 'fizzbuzz'"""

"""    if pos - pos // 5 * 5 == 0:
        return 'buzz'

    if pos - pos // 3 * 3 == 0:
        return 'fizz'"""

"""    if pos in (20,10,5):
        return 'buzz'"""

"""    if pos in (9, 6, 3):
        return 'fizz'"""

"""    if pos == 5:
    return 'buzz'
if pos == 10:
    return 'buzz'
if pos == 20:
    return 'buzz'"""
"""    if pos == 6:
        return 'fizz'
    if pos == 3:
        return 'fizz'"""
    
"""    if pos == 4:
        return str(pos)
    if pos == 2:
        return str(pos)
    return str(pos)"""

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'