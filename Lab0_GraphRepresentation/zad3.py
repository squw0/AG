class GraphEdgeList:
    def __init__(self):
        self.edge_list = []

    def add_edge(self, i, j):
        if (i, j) not in self.edge_list and (j, i) not in self.edge_list:
            self.edge_list.append((i, j))
        else:
            print(f"krawędź ({i}, {j}) już istnieje.")

    def remove_edge(self, i, j):
        try:
            self.edge_list.remove((i, j))
        except ValueError:
            try:
                self.edge_list.remove((j, i))
            except ValueError:
                print(f"krawędź ({i}, {j}) nie istnieje.")

    def display(self):
        if not self.edge_list:
            print("graf nie ma krawędzi.")
        else:
            for edge in self.edge_list:
                print(f"{edge}")

g = GraphEdgeList()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("lista krawędzi dla nieskierowanego:")
g.display()