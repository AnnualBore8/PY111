def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    one = 1

    if not isinstance(n, int):
        raise TypeError('n должно быть целым числом - int')
    if n < 0:
        raise ValueError('n должно быть неотрицательным числом')

    if n == 0:
        return 1

    if n >= 1:
        for item in range(1, n):
            one *= item
            print(one)

    return one * n

      # TODO реализовать рекурсивный алгоритм нахождения факториала


if __name__ == '__main__':
    print(factorial_recursive(5))