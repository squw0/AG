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

# Graf niespójny z wierzchołkami 0, 1, 2, 3, 4, 5
edges = [(0, 1), (1, 2), (3, 4)]  # Krawędzie grafu

# Inicjalizacja DSU dla 6 wierzchołków
dsu = DisjointSetUnion(6)

# Łączenie wierzchołków zgodnie z krawędziami
for u, v in edges:
    dsu.union(u, v)

# Sprawdzamy komponenty
print("Reprezentanci wierzchołków:")
for i in range(6):
    print(f"Wierzchołek {i}: Lider {dsu.find(i)}")
