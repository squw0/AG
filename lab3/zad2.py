class DisjointSetUnion:
    def __init__(self, n):
        # Inicjalizacja: każdy element jest własnym liderem, a ranga wynosi 1
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        # Path compression: elementy wskazują bezpośrednio na lidera
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank: łączymy mniejsze drzewo do większego
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(n, edges):
    # edges: lista (waga, u, v) - sortujemy po wadze
    edges.sort()
    dsu = DisjointSetUnion(n)
    mst = []
    mst_cost = 0

    for weight, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v))
            mst_cost += weight

    return mst, mst_cost

# Przykład: Graf niespójny
edges = [
    (1, 0, 1),  # (waga, u, v)
    (2, 1, 2),
    (2, 3, 4),
    (3, 2, 3),
    (4, 0, 5)
]
n = 6  # liczba wierzchołków

mst, cost = kruskal(n, edges)
print("Minimalne Drzewo Rozpinające (MST):", mst)
print("Całkowity koszt MST:", cost)
