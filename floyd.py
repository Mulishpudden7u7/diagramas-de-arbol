def floyd_warshall(graph):
    dist = graph.copy()
    nodes = list(graph.keys())
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])#compara suma de ij con la suma de ik y kj
    
    return dist

graph = {
    'A': {'A': 0, 'B': 4, 'C': float('inf'), 'D': float('inf')},
    'B': {'A': float('inf'), 'B': 0, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': float('inf'), 'C': 0, 'D': 3},
    'D': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0}
}
print(floyd_warshall(graph))
