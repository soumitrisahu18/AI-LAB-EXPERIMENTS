# Experiment 1: Breadth First Search (BFS)
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal = ""
    while queue:
        vertex = queue.popleft()
        traversal += vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal
graph = {}
n = int(input("Enter the number of vertices: "))
for i in range(n):
    vertex = input(f"Enter vertex {i + 1}: ")
    adjacent = input(
        f"Enter adjacent vertices of {vertex} (space-separated): "
    ).split()
    graph[vertex] = adjacent
start = input("Enter the starting vertex: ")
print("BFS Traversal:", bfs(graph, start))
