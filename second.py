from graph import G
from collections import deque
from networkx.classes.function import path_weight


def distance_of_path(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    return distance


def dfs(graph, stack, start, end):
    stack.append(start)
    if start == end:
        return stack
    for neighbor in graph[start]:
        if neighbor not in stack:
            path = dfs(graph, stack, neighbor, end)
            if path:
                return path
    stack.pop()


def bfs(graph, queue, start, end):
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)


dfs_result = dfs(G, deque(), 'Kyiv', 'Valletta')
print(" -> ".join([x for x in dfs_result]), path_weight(G, dfs_result, weight='weight'))

bfs_result = bfs(G, deque(), 'Kyiv', 'Valletta')
print(" -> ".join(bfs_result), path_weight(G, bfs_result, weight='weight'))
