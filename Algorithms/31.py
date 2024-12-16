# Система двусторонних дорог такова, что для любой пары городов можно указать соединяющий их путь.
# Найдите такой город, сумма расстояний от которого до остальных городов минимальна.

# флойд)

def floydWarshall(V, graph: list[list[int]]):
    dist = graph.copy()
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # тут просто проход по вершинам и сумма путей от них до других
    sumforall = [sum(dist[i]) for i in range(len(dist))]
    return sumforall.index(min(sumforall))


# num_vertices = 5
# max_weight = 10
# np.random.seed(1)

# adjacency_matrix = np.zeros((num_vertices, num_vertices))

# for i in range(num_vertices):
#     for j in range(i+1, num_vertices):
#         weight = np.random.randint(1, max_weight+1)
#         adjacency_matrix[i, j] = weight
#         adjacency_matrix[j, i] = weight

# print(floydWarshall(num_vertices, adjacency_matrix.tolist()))
