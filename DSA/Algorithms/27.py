# Дан неориентированный невзвешенный граф. 
# Необходимо посчитать количество его компонент связности и вернуть их в виде двумерного списка, 
# количество строк которого соответствует количеству компонент, а в строках содержится множество вершин каждой компоненты.

# Задача супер изи тупо dfs`ом проходимся, если остались вершины после прохода,
# значит есть еще компоненты связности, по ним проходимся.
def find_components(N, graph):
    list_of_comps = []
    visited = [False for _ in range(N)]
    def dfs(node, visited, component:list):
        visited[node] = True
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, component)
        return component
    for node in range(len(visited)):
        if visited[node] == False:
            list_of_comps.append(dfs(node, visited, []))
    return list_of_comps

graph = [
    [1, 2],
    [0],
    [0],
    [5],
    [6],
    [3],
    [4],
]
N = 7
print(find_components(N,graph))