# Minimax Algorithm
def minimax(node, depth, maximizing_player):
    # If leaf node is reached
    if depth == 0 or isinstance(node, int):
        return node
    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
# Main program
# Game tree with leaf node values
game_tree = [
    [3, 5],
    [6, 9]
]
depth = 2
best_value = minimax(game_tree, depth, True)
print("Minimax Algorithm")
print("Optimal value:", best_value)
