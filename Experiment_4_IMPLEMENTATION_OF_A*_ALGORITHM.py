# Experiment 4: A* Search Algorithm
def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start)]
    came_from = {}
    g_cost = {start: 0}
    while open_list:
        open_list.sort(key=lambda x: x[0])
        current = open_list.pop(0)[1]
        if current == goal:
            path = [goal]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_cost[goal]
        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current
                f_cost = new_cost + heuristic[neighbor]
                open_list.append((f_cost, neighbor))
    return None, float("inf")
# Main Program
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}
heuristic = {
    "A": 4,
    "B": 3,
    "C": 1,
    "D": 0
}
start = input("Enter start node: ")
goal = input("Enter goal node: ")
path, cost = a_star(graph, heuristic, start, goal)
if path:
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
    print("We have successfully implemented A* algorithm using Python.")
else:
    print("Path not found.")
