import networkx as nx

def is_connected(graph):
    """Sprawdza, czy graf jest spójny"""
    if len(graph) == 0:
        return True
    
    visited = set()
    
    def dfs(v):
        visited.add(v)
        for neighbor in graph.neighbors(v):
            if neighbor not in visited:
                dfs(neighbor)
    
    start_node = next(iter(graph))
    dfs(start_node)
    return len(visited) == len(graph)

def has_eulerian_cycle(graph):
    """Sprawdza, czy graf ma cykl Eulera"""
    # Warunek: graf musi być spójny i każdy wierzchołek musi mieć parzysty stopień
    return is_connected(graph) and all(degree % 2 == 0 for node, degree in graph.degree())

def fleury_algorithm(graph):
    """Implementacja algorytmu Fleury'ego"""
    if not has_eulerian_cycle(graph):
        return "Graf nie ma cyklu Eulera"
    
    # Kopia grafu, aby nie modyfikować oryginału
    graph_copy = graph.copy()
    cycle = []
    
    def is_bridge(u, v):
        """Sprawdza, czy krawędź u-v jest mostem"""
        graph_copy.remove_edge(u, v)
        
        # Sprawdzenie spójności grafu po usunięciu krawędzi
        is_connected_after_removal = is_connected(graph_copy)
        
        # Przywracamy krawędź
        graph_copy.add_edge(u, v)
        
        return not is_connected_after_removal
    
    # Wybieramy wierzchołek początkowy
    current_vertex = next(iter(graph))
    
    # Dopóki graf ma krawędzie
    while graph_copy.edges:
        for neighbor in graph_copy.neighbors(current_vertex):
            # Jeśli krawędź nie jest mostem, przechodzimy po niej
            if not is_bridge(current_vertex, neighbor):
                cycle.append((current_vertex, neighbor))
                graph_copy.remove_edge(current_vertex, neighbor)
                current_vertex = neighbor
                break
        else:
            # Jeśli wszystkie krawędzie są mostami, wybieramy dowolną krawędź
            neighbor = next(graph_copy.neighbors(current_vertex))
            cycle.append((current_vertex, neighbor))
            graph_copy.remove_edge(current_vertex, neighbor)
            current_vertex = neighbor
    
    return cycle

# Przykład użycia
if __name__ == "__main__":
    # Tworzymy graf
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])

    print("Cykl Eulera:", fleury_algorithm(G))
