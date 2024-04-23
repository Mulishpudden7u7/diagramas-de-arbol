def warshall(graph):
    nodes = list(graph.keys())
    closure = {node: {neighbor: False for neighbor in nodes} for node in nodes}
    
    for i in nodes:
        for j in nodes:
            if i == j or j in graph[i]:
                closure[i][j] = True
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    
    return closure

graph = {
    'A': {'B', 'C'},
    'B': {'D'},
    'C': {'D'},
    'D': {}
}
print(warshall(graph))
