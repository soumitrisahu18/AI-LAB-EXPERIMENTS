from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    
    while queue:
        jug1, jug2, path = queue.popleft()
        
        if (jug1, jug2) in visited:
            continue
            
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]
        
        if jug1 == target or jug2 == target:
            return path
            
        next_states = [
            (capacity1, jug2),  # Fill jug 1
            (jug1, capacity2),  # Fill jug 2
            (0, jug2),          # Empty jug 1
            (jug1, 0),          # Empty jug 2
            # Pour jug 2 into jug 1
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1)),
            # Pour jug 1 into jug 2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))
                
    return None

# Main Program
if __name__ == "__main__":
    jug1 = int(input("Enter capacity of jug 1: "))[span_2](start_span)[span_2](end_span)
    jug2 = int(input("Enter capacity of jug 2: "))[span_3](start_span)[span_3](end_span)
    target = int(input("Enter target amount: "))
    
    solution = water_jug(jug1, jug2, target)[span_4](start_span)[span_4](end_span)
    
    if solution:
        print("\nSteps to reach target:")[span_5](start_span)[span_5](end_span)
        for step in solution:[span_6](start_span)[span_6](end_span)
            print(step)[span_7](start_span)[span_7](end_span)
    else:
        print("NO solution exists")[span_8](start_span)[span_8](end_span)
