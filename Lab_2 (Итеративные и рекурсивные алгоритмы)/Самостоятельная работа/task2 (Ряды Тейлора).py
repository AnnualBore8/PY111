from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    def get_next_item(n):
        """ Подсчет очередного элемента бесконечного ряда Тейлора для sin(x)"""
        return (pow(-1, n)) * (pow(x, 2*n+1)/factorial(2*n+1))

    sum_ = 0

    for i in count():
        current_value = get_next_item(i)
        sum_ += current_value

        if abs(current_value) <= DELTA:
            return sum_


if __name__ == "__main__":
    sinx(15)

# TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
