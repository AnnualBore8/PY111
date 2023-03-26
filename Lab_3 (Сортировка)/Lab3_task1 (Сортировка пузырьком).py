import random
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    for l in range(len(container) - 1):
        for r in range(len(container) - 1 - l):
            if container[r] > container[r + 1]:
                container[r], container[r + 1] = container[r + 1], container[r]
    return container

    # TODO реализовать алгоритм сортировки пузырьком


if __name__ == '__main__':
    seq = [random.randint(0, 100) for _ in range(10)]
    print(seq)
    print(sort(seq))