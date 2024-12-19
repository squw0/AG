class GraphAdjList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, i, j):
        if i >= self.num_vertices or j >= self.num_vertices or i < 0 or j < 0:
            print(f"nieprawidłowe indeksy: {i}, {j}")
            return
        self.adj_list[i].append(j)

    def remove_edge(self, i, j):
        if i >= self.num_vertices or j >= self.num_vertices or i < 0 or j < 0:
            print(f"nieprawidłowe indeksy: {i}, {j}")
            return
        try:
            self.adj_list[i].remove(j)
        except ValueError:
            print(f"krawędź {i} -> {j} nie istnieje")

    def display(self):
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")

g = GraphAdjList(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("lista sąsiedztwa dla skierowanego:")
g.display()