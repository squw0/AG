import itertools

def calculate_cycle_weight(graph, cycle):
    weight = 0
    for i in range(len(cycle) - 1):
        weight += graph[cycle[i]][cycle[i + 1]]
    weight += graph[cycle[-1]][cycle[0]]  # Wracamy do punktu początkowego
    return weight

def brute_force(graph):
    vertices = list(range(len(graph)))
    min_weight = float('inf')
    best_cycle = None
    
    # Sprawdzamy wszystkie permutacje wierzchołków
    for perm in itertools.permutations(vertices):
        weight = calculate_cycle_weight(graph, perm)
        if weight < min_weight:
            min_weight = weight
            best_cycle = perm
            
    return min_weight, best_cycle


def nearest_neighbor(graph, start=0):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    cycle = [start]
    current_vertex = start
    total_weight = 0
    
    for _ in range(n - 1):
        next_vertex = None
        min_edge_weight = float('inf')
        
        # Wybieramy najbliższego nieodwiedzonego sąsiada
        for neighbor in range(n):
            if not visited[neighbor] and graph[current_vertex][neighbor] < min_edge_weight:
                next_vertex = neighbor
                min_edge_weight = graph[current_vertex][neighbor]
        
        visited[next_vertex] = True
        cycle.append(next_vertex)
        total_weight += min_edge_weight
        current_vertex = next_vertex
    
    # Powrót do punktu początkowego
    total_weight += graph[current_vertex][start]
    cycle.append(start)
    
    return total_weight, cycle


# Definicja grafu
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Uruchamiamy algorytm Brute-Force
min_weight_bf, cycle_bf = brute_force(graph)
print(f"Brute-Force: Minimum Weight = {min_weight_bf}, Cycle = {cycle_bf}")

# Uruchamiamy algorytm Najbliższego Sąsiada
min_weight_nn, cycle_nn = nearest_neighbor(graph)
print(f"Nearest Neighbor: Minimum Weight = {min_weight_nn}, Cycle = {cycle_nn}")
