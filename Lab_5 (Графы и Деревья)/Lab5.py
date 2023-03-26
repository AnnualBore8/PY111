from typing import Union

import networkx as nx
import matplotlib.pyplot as plt


def stairway_graph_funk(tuple_: tuple[int]) -> list:
    """
    Функция для создания списка кортежей из исходного кортежа для создания графа.
    :param tuple_: Исходный кортеж, содержащий информацию о стоимости каждого перехода
    :return: Список кортежей для создания графа
    """
    list_ = []
    for elem_1 in range(len(tuple_)):
        list_.append((elem_1, elem_1 + 1, tuple_[elem_1]))

    for elem_2 in range(len(tuple_) - 1):
        list_.append((elem_2, elem_2 + 2, tuple_[elem_2 + 1]))

    return list_


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """

    # Самый простой способ решения - это просто скопировать код из задания "Дейкстра. Кратчайший путь."
    # Для того чтобы код работал корректно необходимо сделать всего три изменения: заменить "g" на "graph", задать
    # значение для current_node = 0 и возвращать значение списка по последнему ключу.

    visited_nodes = {node: False for node in graph.nodes}
    # print(visited_nodes)
    total_coasts = {node: float('inf') for node in graph.nodes}
    # print(total_coasts)
    current_node = 0
    total_coasts[current_node] = 0

    for _ in range(len(graph)):
        not_visited_total_coasts = {node: coast for node, coast in total_coasts.items() if not visited_nodes[node]}
        min_coast = float('inf')
        # print(not_visited_total_coasts)

        for node, coast in not_visited_total_coasts.items():
            if coast < min_coast:
                min_coast = coast
                current_node = node
        # print(not_visited_total_coasts)
        visited_nodes[current_node] = True

        for neighbor_node in graph[current_node]:
            weight = graph[current_node][neighbor_node]['weight']
            total_coasts[neighbor_node] = min(total_coasts[neighbor_node], total_coasts[current_node] + weight)

    return list(total_coasts.values())[-1]  # первое, что пришло в голову
    # return total_coasts[len(stairway)]  # возможно, более адекватный вариант, но он почему-то не проходит тесты


def stairway_path_using_networkx(graph: nx.DiGraph):
    """
    Функция рассчитывает минимальную стоимость подъема по лестнице. Фактически делает то же самое, что и функция
    stairway_path только при помощи
    :param graph:
    :return:
    """
    lengths = nx.dijkstra_path_length(graph, list(graph.nodes)[0], list(graph.nodes)[-1])

    return lengths

    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    step = stairway_graph_funk(stairway)
    nodelist = [i + 1 for i in range(len(stairway))]

    stairway_graph = nx.DiGraph()
    stairway_graph.add_nodes_from([i for i in range(len(stairway))])

    for from_loc, to_loc, dist in step:
        stairway_graph.add_edge(from_loc, to_loc, weight=dist)

    pos = nx.spring_layout(stairway_graph)
    nx.draw(stairway_graph, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(stairway_graph, 'weight')
    nx.draw_networkx_edge_labels(stairway_graph, pos, edge_labels=edge_labels)
    nx.draw_networkx_nodes(stairway_graph, pos, nodelist=nodelist, node_color='r')
    plt.show()

    # # первоначально для понимания перебрал все варианты руками, потому что сразу не дошло, как это работает
    # stairway_graph = nx.DiGraph()
    #
    # stairway_graph.add_weighted_edges_from(
    #     [
    #         (0, 1, 5), (0, 2, 11), (1, 2, 11), (1, 3, 43), (2, 3, 43), (2, 4, 2), (3, 4, 2),
    #         (3, 5, 23), (4, 5, 23), (4, 6, 43), (5, 6, 43), (5, 7, 22), (6, 7, 22), (6, 8, 12),
    #         (7, 8, 12), (7, 9, 6), (8, 9, 6), (8, 10, 8), (9, 10, 8)
    #     ]
    # )
    #
    # nx.draw_networkx(stairway_graph, with_labels=True, node_color='red')
    # plt.show()
    #
    #   # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    print(stairway_path(stairway_graph))  # 72
    print(stairway_path_using_networkx(stairway_graph))  # 72
