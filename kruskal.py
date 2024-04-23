class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(graph):
    node_indices = {node: i for i, node in enumerate(graph)}
    #u y v son indices enteros
    edges = [(weight, node_indices[u], node_indices[v]) for u in graph for v, weight in graph[u].items()]
    edges.sort()#ascendente
    num_vertices = len(graph)
    mst = []
    ds = DisjointSet(num_vertices)
    
    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v)
    
    return mst

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}
print(kruskal(graph))
