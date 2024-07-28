I decided to check bfs and dfc on path from Kyiv to Valletta.

DFS:
    
Kyiv -> Bratislava -> Vienna -> Budapest -> Belgrade -> Sofia -> Athens -> Skopje -> Tirana -> Podgorica -> Sarajevo -> Zagreb -> Ljubljana -> Rome -> Valletta

This path is not optimal, because it is not the shortest one. Total distance is ~4979.358 km.

BSF:

Kyiv -> Bratislava -> Vienna -> Ljubljana -> Rome -> Valletta

This path is optimal, because it is the shortest one. Total distance is ~ 2518.102 km.

DFS is trying to go as deep as possible, while BFS is trying to go as wide as possible.
Because of that, BFS will usually find the shortest path, while DFS is better for finding cycles in graphs.

