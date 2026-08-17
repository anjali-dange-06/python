print("Best-First Search")

import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values
h = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (h[start], start))

    while priority_queue:
        heuristic, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print(node, end=' ')
        visited.add(node)

        if node == goal:
            print("\nGoal reached!")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (h[neighbour], neighbour)
                )

    print("\nGoal not found")

best_first_search(graph, 'A', 'F')