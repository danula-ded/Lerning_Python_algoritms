# Дана система двусторонних дорог. 
# N-периферией называется множество городов, расстояние от которых до выделенного города (столицы) больше N. 
# Для данного N определите N-периферию.

# тут я белмана форда юзнул


def len_to_verts(V, graph, vert, N):
    dist = [float("Inf")] * V 
    dist[vert] = 0

    for _ in range(V - 1): 
        for u, v, w in graph:
            if dist[u - 1] != float("Inf") and dist[u - 1] + w < dist[v - 1]: 
                    dist[v - 1] = dist[u - 1] + w

    ans = []
    for i in range(V):
        if dist[i] > N:
            # print(i+1, dist[i], N)
            ans.append(i+1)
    return ans

edges = [
    (1, 2, 6),
    (1, 3, 2),
    (2, 4, 9),
    (2, 5, 3),
    (3, 4, 8),
    (4, 5, 5),
]

# print(len_to_verts(5, edges, 0, 5))
