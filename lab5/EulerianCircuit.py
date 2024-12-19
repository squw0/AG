from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def dfs(self, u, visited):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs(v, visited)

    def is_connected(self):
        visited = {node: False for node in self.graph}
        # Find a vertex with non-zero degree
        for node in self.graph:
            if len(self.graph[node]) > 0:
                break
        # If no vertex with non-zero degree is found, the graph is connected
        if not node:
            return True
        # Start DFS traversal from a vertex with non-zero degree
        self.dfs(node, visited)
        # Check if all non-zero degree vertices are visited
        for node in self.graph:
            if not visited[node] and len(self.graph[node]) > 0:
                return False
        return True

    def is_eulerian(self):
        if not self.is_connected():
            return False
        # Count vertices with odd degree
        odd_degree_count = sum(1 for node in self.graph if len(self.graph[node]) % 2 != 0)
        if odd_degree_count == 0:
            return 'Eulerian Circuit'
        elif odd_degree_count == 2:
            return 'Eulerian Path'
        else:
            return False

    def eulerian_path(self):
        euler_path = []
        start_vertex = next(iter(self.graph))
        current_vertex = start_vertex
        while self.graph[current_vertex]:
            next_vertex = self.graph[current_vertex][0]
            if len(self.graph[current_vertex]) == 1:
                # If the current vertex has only one adjacent vertex
                euler_path.append((current_vertex, next_vertex))
                self.remove_edge(current_vertex, next_vertex)
            else:
                # If there are multiple adjacent vertices
                for vertex in self.graph[current_vertex]:
                    if not self.is_bridge(current_vertex, vertex):
                        next_vertex = vertex
                        break
                euler_path.append((current_vertex, next_vertex))
                self.remove_edge(current_vertex, next_vertex)
            current_vertex = next_vertex
        return euler_path

    def is_bridge(self, u, v):
        # Remove edge (u, v) and check if the graph becomes disconnected
        self.remove_edge(u, v)
        visited = {node: False for node in self.graph}
        self.dfs(u, visited)
        # Add edge (u, v) back
        self.add_edge(u, v)
        return not visited[v]

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 3)

euler_type = g.is_eulerian()
if euler_type:
    print("Graph contains an", euler_type)
    if euler_type == 'Eulerian Path':
        print("Eulerian Path:", g.eulerian_path())
elif euler_type is False:
    print("Graph doesn't contain an Eulerian Path or Circuit")
