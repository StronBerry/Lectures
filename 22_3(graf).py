# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D'],
#     'D': ['B', 'C']
# }

import networkx as nx
import matplotlib.pyplot as plt

weighted_graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 4, 'E': 3},
    'C': {'A': 2, 'F': 7},
    'D': {'B': 4},
    'E': {'B': 3, 'F': 6},
    'F': {'C': 7, 'E': 6}
}

# Создаем направленный граф
G = nx.DiGraph()

# Добавляем узлы и ребра в граф
for node, edges in weighted_graph.items():
   G.add_node(node)
   for neighbor, weight in edges.items():
       G.add_edge(node, neighbor, weight=weight)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

from collections import defaultdict


def dijkstra(graph, source):
    distances = defaultdict(lambda: float('inf'))
    previous = {}
    unvisited = set(graph.keys())

    distances[source] = 0

    while unvisited:  # Пока есть непосещенные вершины
        current_node = min(unvisited, key=lambda node: distances.get(node, float(
            'inf')))
        unvisited.remove(current_node)

        # Финальная часть алгоритма:
        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[
                    neighbor] = current_node

    return distances, previous

# Находим кратчайшие пути от узла 'D'
distances, previous = dijkstra(weighted_graph, 'D')
print(distances)
# defaultdict(<function dijkstra.<locals>.<lambda> at 0x0000019924F4FBA0>,
# {'D': 0,
# 'B': 4,
# 'A': 9,
# 'E': 7,
# 'F': 13,
# 'C': 11})
print(previous)  # {'B': 'D', 'A': 'B', 'E': 'B', 'F': 'E', 'C': 'A'}


def get_shortest_path(previous, source, target):
   path = [target]  # Начинаем с целевой вершины
   while path[-1] != source:  # Пока не достигнем начальной вершины
      path.append(previous[path[-1]])  # Добавляем предыдущую вершину на путь к текущей вершине
   path.reverse()  # Переворачиваем список, чтобы путь был от начальной вершины к целевой
   return path

# Находим кратчайшие пути от узла 'D'
distances, previous = dijkstra(weighted_graph, 'D')
# Выводим кратчайший путь от 'D' до 'F'
path = get_shortest_path(previous, 'D', 'F')
print(f"Кратчайший путь от D до F: {path}")
# Кратчайший путь от D до F: ['D', 'B', 'E', 'F']