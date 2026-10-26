# Objective Function
def objective_function(x):
  return -(x**2)+10
# Hill Climbing Function
def hill_climbing(start, step_size, max_iterations):
  current = start
  current_value = objective_function(current)
  print(f"Initial point: (x={current:.2f}), Value: {current_value:.2f}")
  for i in range(max_iterations):
    left = current - step_size
    right = current + step_size
    left_value = objective_function(left)
    right_value = objective_function(right)
    # Move To The Better Neighbour
    if left_value > current_value:
      current = left
      current_value = left_value
    elif right_value > current_value:
      current = right
      current_value = right_value
    else:
      break
  return current, current_value
# Main Program
start=float(input("Enter the starting point: "))
step_size=float(input("Enter the step size: "))
max_iterations=int(input("Enter the maximum number of iterations: "))
best_position, best_value = hill_climbing(start, step_size, max_iterations)
print(f"The best position is:{best_position:.2f}")
print(f"The best value is:{best_value:.2f}")
