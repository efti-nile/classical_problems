import heapq


def dijkstra(graph, start):
    # Priority queue to store (cost, vertex)
    pq = [(0, start)]
    # Dictionary to store the minimum cost to reach each node
    min_cost = {start: 0}
    # Dictionary to store the shortest path tree
    parent = {start: None}
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        if current_cost > min_cost[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight
            
            if neighbor not in min_cost or cost < min_cost[neighbor]:
                min_cost[neighbor] = cost
                parent[neighbor] = current_node
                heapq.heappush(pq, (cost, neighbor))
    
    return min_cost, parent


def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    min_cost, parent = dijkstra(graph, start_node)

    print("Minimum costs from start node:", min_cost)
    print("Shortest path tree:", parent)


def heuristic(a, b):
    # Simple heuristic function: Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(graph, start, goal):
    # Priority queue to store (cost, vertex)
    pq = [(0, start)]
    # Dictionary to store the minimum cost to reach each node
    min_cost = {start: 0}
    # Dictionary to store the shortest path tree
    parent = {start: None}
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        if current_node == goal:
            break
        
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            
            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
                parent[neighbor] = current_node
    
    return min_cost, parent


def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


def test_a_star():
    graph = {
        (0, 0): [((0, 1), 1), ((1, 0), 1)],
        (0, 1): [((0, 0), 1), ((1, 1), 1)],
        (1, 0): [((0, 0), 1), ((1, 1), 1)],
        (1, 1): [((0, 1), 1), ((1, 0), 1), ((1, 2), 1)],
        (1, 2): [((1, 1), 1), ((2, 2), 1)],
        (2, 2): [((1, 2), 1)]
    }
    
    start = (0, 0)
    goal = (2, 2)
    min_cost, parent = a_star(graph, start, goal)
    path = reconstruct_path(parent, start, goal)
    
    print("Minimum costs:", min_cost)
    print("Shortest path:", path)


if __name__ == "__main__":
    test_a_star()
    # test_dijkstra()
