graph = {
    'a':['b', 'c', 'd'],
    'b':['a','e'],
    'c':['a','d', 'e'],
    'd':['a', 'c'],
    'e':['b', 'c ']
}
visited = []
def DFS(visited, graph, root):
    if root not in visited:
        print(root)
        visited.append(root)
        for neighbour in graph[root]:
            DFS(visited, graph, neighbour)
DFS(visited, graph, 'a')
