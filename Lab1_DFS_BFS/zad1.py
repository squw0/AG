class GraphMatrix:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, i, j):
        if i >= self.num_vertices or j >= self.num_vertices or i < 0 or j < 0:
            print(f"nieprawidłowe indeksy: {i}, {j}")
            return
        self.adj_matrix[i][j] = 1
        if not self.directed:
            self.adj_matrix[j][i] = 1

    def remove_edge(self, i, j):
        if i >= self.num_vertices or j >= self.num_vertices or i < 0 or j < 0:
            print(f"nieprawidłowe indeksy: {i}, {j}")
            return
        self.adj_matrix[i][j] = 0
        if not self.directed:
            self.adj_matrix[j][i] = 0

    def display(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

g = GraphMatrix(4, directed=False)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("macierz sąsiedztwa dla nieskierowanego:")
g.display()