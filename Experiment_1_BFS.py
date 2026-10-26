# Experiment 1: Breadth First Search (BFS)
# Aim: To implement BFS traversal of a graph using Python.
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
start_node = "A"
print("BFS traversal starting from", start_node, ":")
print(" -> ".join(bfs(graph, start_node)))
