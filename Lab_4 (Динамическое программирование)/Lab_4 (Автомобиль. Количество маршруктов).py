from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """

    # list_ = [[0]*n for i in range(m)]
    # # print(list_)
    #
    # for i in range(n):
    #     list_[0][i] = 1
    # # print(list_)
    #
    # for j in range(m):
    #     list_[j][0] = 1
    # # print(list_)
    #
    # for j in range(1, m):
    #     for i in range(1, n):
    #         list_[j][i] = list_[j][i-1] + list_[j-1][i] + list_[j-1][i-1]
    # # print(list_)
    # # print(list_[-1][-1])
    # return list_

    list_ = [[0]*m for i in range(n)]

    for i in range(m):
        list_[0][i] = 1

    for j in range(n):
        list_[j][0] = 1
    print(list_)

    for j in range(1, n):
        for i in range(1, m):
            list_[j][i] = list_[j][i-1] + list_[j-1][i] + list_[j-1][i-1]
    return list_

      # TODO решить задачу с помощью динамического программирования


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
