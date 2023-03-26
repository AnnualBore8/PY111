def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    count = 0

    for brckt in brackets_row:
        if brckt == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False

    if count == 0:
        return True  # TODO реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets("(()()()"))  # True
    print(check_brackets(")("))  # False
