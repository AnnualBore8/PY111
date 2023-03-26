def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    first = 1

    if not isinstance(n, int):
        raise TypeError('n должно быть целым числом - int')
    if n < 0:
        raise ValueError('n должно быть неотрицательным числом')

    empty_list = []
    for i in range(n+1):
        if i != 0:
            empty_list.append(i)
        else:
            pass

    for next_par in empty_list:
        first *= next_par
    return first

# TODO реализовать итеративный алгоритм нахождения факториала


if __name__ == '__main__':
    factorial_iterative(5)
    print(factorial_iterative(5))