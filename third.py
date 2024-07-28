from graph import G
import networkx as nx
import pprint


def dijkstra(graph: nx.classes.Graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for (neighbor, props) in graph[current_vertex].items():
            distance = distances[current_vertex] + props["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


result = [x for x in dijkstra(G, 'Kyiv').items()]

result.sort(key=lambda x: x[1])

pprint.pp(result)