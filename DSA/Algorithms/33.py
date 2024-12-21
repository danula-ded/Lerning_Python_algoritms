# Дан взвешенный ориентированный граф с n узлами и m ребрами.
# Узлы пронумерованы от 0 до n-1, необходимо проверить, содержит ли граф цикл отрицательного веса.
# Примечание: edges[i] состоит из вершин u, v и веса.

# белман форд
def has_cycle(V, graph, vert = 0):
    dist = [float("Inf")] * V 
    dist[vert] = 0

    for _ in range(V - 1): 
        for u, v, w in graph:
            if dist[u - 1] != float("Inf") and dist[u - 1] + w < dist[v - 1]: 
                    dist[v - 1] = dist[u - 1] + w
    
    # вторым проходом проверяем на цикличность 
    for u, v, w in graph:
        if dist[u - 1] != float("Inf") and dist[u - 1] + w < dist[v - 1]: 
            return 'цикл есть'
    return 'цикла нет'