"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self._stack = [5, 4, 3, 1]  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        return self._stack.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._stack:
            raise IndexError('Извлечение из пустой очереди невозможно')

        return self._stack.pop(0)  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError('Индекс должен быть целым числом')
        if not 0 <= ind < len(self._stack):
            raise IndexError('Индекс вне границ стека')

        return self._stack[ind]
        # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self._stack.clear()# TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._stack) # TODO реализовать метод __len__
