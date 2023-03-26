import random
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    if len(container) <= 1:
        return container

    # if len(container) == 0:
    #     return container

    new_dict = {}
    new_list = []
    while len(container) > 1:
        max_item = max(container)
        a = [ind for ind, item in enumerate(container) if item == max_item]
        new_dict[max_item] = len(a)

        for i in range(len(a)):
            container.remove(max_item)

    for key, value in new_dict.items():
        for i in range(value):
            new_list.append(key)

    new_list.reverse()
    return new_list


    # TODO реализовать алгоритм сортировки подсчетами


if __name__ == '__main__':
    seq = [random.randint(0, 100) for _ in range(10)]
    seq_ = [4, 1, 19, 5, 4, 19, 3, 3, 2, 8]
    seq_1 = [4, 1]
    seq_11 = [1]
    seq_111 = []
    print(seq)
    print(seq_)
    print(sort(seq))
    print(sort(seq_))
    print(sort(seq_1))
    print(sort(seq_11))
    print(sort(seq_111))
