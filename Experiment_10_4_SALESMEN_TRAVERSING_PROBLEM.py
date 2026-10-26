from itertools import permutations

def travelling_sales(graph, start):
  cities = list(range(len(graph)))
  cities.remove(start)

  min_cost = float('inf')
  best_path = None

  for path in permutations(cities):
    current_cost = 0
    current_path = [start]
    k = start

    for city in path:
      current_path.append(city)
      current_cost += graph[k][city]
      k = city
    current_cost += graph[k][start]
    current_path.append(start)

    if current_cost < min_cost:
      min_cost = current_cost
      best_path = current_path
  return min_cost, best_path

print("Please enter the distance matrix row by row. Values must be space-separated integers.")
n = int(input("Enter the number of cities: "))
graph = []

for i in range(n):
  while True:
    try:
      row = list(map(int, input(f"Enter {n} distances from city {i} to all other cities (space-separated): ").split()))
      if len(row) != n:
        print(f"Error: You must enter exactly {n} values. You entered {len(row)} values. Please try again.")
        continue
      graph.append(row)
      break
    except ValueError:
      print("Error: Please enter only valid integers. Try again.")

while True:
  try:
    start = int(input("Enter the starting city index (0 to {}): ".format(n - 1)))
    if 0 <= start < n:
      break
    print(f"Error: Index must be between 0 and {n - 1}.")
  except ValueError:
    print("Error: Please enter a valid integer.")

cost, path = travelling_sales(graph, start)
print("\nOptimal path:", "->".join(map(str, path)))
print("\nMinimum cost:", cost)
