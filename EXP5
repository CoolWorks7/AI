graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'D': 2, 'E': 2},
    'C': {'A': 1, 'G': 3, 'H': 4},
    'D': {'B': 2},
    'E': {'B': 2, 'F': 3},
    'F': {'E': 3},
    'G': {'C': 3, 'I': 2},
    'H': {'C': 4},
    'I': {'G': 2, 'F': 1}
}

def heuristic(node):
    values = {
        'A': 6,
        'B': 5,
        'C': 4,
        'D': 6,
        'E': 6,
        'F': 1,
        'G': 3,
        'H': 5,
        'I': 2,
    }
    return values[node]


def hill_climbing(start_node, goal_node, type):
    current_node = start_node
    while current_node != goal_node:
        neighbours = graph[current_node]

        for key in neighbours:
            neighbours[key] = heuristic(key)

        temp = ''
        if type == 'simple':
            temp = min(neighbours.values())
        else:
            temp = max(neighbours.values())

        best_neighbour = [key for key in neighbours if neighbours[key] == temp][0]

        if best_neighbour in closed_nodes:
            return False
        closed_nodes.append(best_neighbour)
        current_node = best_neighbour
    return True


start_node = 'A'
goal_node = 'F'
closed_nodes = [start_node]

print(f'\n\tFinding Goal Node {goal_node} using Hill Climbing Algorithm\n')

print(f'\t1) Simple Hill Climbing:-\n')
result1 = hill_climbing(start_node, goal_node, 'simple')
if result1:
    print(f'\t\tThe Goal Node "{goal_node}" is found by Simple Hill Climbing Algorithm.')
    print(f'\t\tThe Path is shown below:-', end="\n\t\t")
    for i in range(len(closed_nodes)):
        if i < len(closed_nodes) - 1:
            print(closed_nodes[i], end=' --> ')
        else:
            print(closed_nodes[i], end='\n\n\n')
else:
    print(f'\t\tThe Goal Node "{goal_node}" is not found by Simple Hill Climbing Algorithm.')


print(f'\t2) Steepest Hill Climbing:-\n')

result2 = hill_climbing(start_node, goal_node, 'steepest')
if result2:
    print(f'\t\tThe Goal Node "{goal_node}" is found by Steepest Hill Climbing Algorithm.')
    print(f'\t\tThe Path is shown below:-', end="\n\t\t")
    for i in range(len(closed_nodes)):
        if (i < len(closed_nodes) - 1):
            print(closed_nodes[i], end=' --> ')
        else:
            print(closed_nodes[i], end='\n\n\n')
else:
    print(f'\t\tThe Goal Node "{goal_node}" is not found by Steepest Hill Climbing Algorithm.')
