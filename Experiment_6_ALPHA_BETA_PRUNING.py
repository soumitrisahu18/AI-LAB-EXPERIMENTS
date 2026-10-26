import math
def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta, height):
    if depth == height:
        return values[node_index]
    if maximizing_player:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
# Main Program
if __name__ == "__main__":
    values = list(map(int, input("Enter 8 leaf nodes: ").split()))[span_2](start_span)[span_2](end_span)
    height = 3[span_3](start_span)[span_3](end_span)
    result = alpha_beta(0, 0, True, values, -math.inf, math.inf, height)[span_4](start_span)[span_4](end_span)
    print("The optimal value is:", result)[span_5](start_span)[span_5](end_span)
