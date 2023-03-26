"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError

    min_index = 0
    min_value = arr[min_index]

    for index, value in enumerate(arr):
        if value < min_value:
            min_value = value
            min_index = index
    return min_index
        # TODO реализовать итеративный линейный поиск
