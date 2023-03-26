from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    left_border = 0
    right_border = len(seq) - 1

    while left_border <= right_border:
        # middle_index = left_border + (right_border - left_border) // 2  # предложено в решении
        middle_index = (left_border + right_border) // 2
        middle_value = seq[middle_index]

        if middle_value == value:
            while True:
                if middle_index <= 0 or seq[middle_index - 1] != middle_value:
                    break
                else:
                    middle_index -= 1
            return middle_index
        elif middle_value < value:
            left_border = middle_index + 1
        elif middle_value > value:
            right_border = middle_index - 1
        # else:

    raise ValueError('Элемент не найден')

    # TODO реализовать итеративный алгоритм бинарного поиска


if __name__ == '__main__':
    a = binary_search(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(a)
