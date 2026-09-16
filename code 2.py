# A* Algorithm with User Input

def astar(graph, h, start, goal):
    open_list = [start]
    closed_list = []
    g = {start: 0}
    parent = {start: None}

    while open_list:
        # Find node with lowest f = g + h
        current = min(open_list, key=lambda node: g[node] + h[node])

        if current == goal:
            break

        open_list.remove(current)
        closed_list.append(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue

            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current

                if neighbor not in open_list:
                    open_list.append(neighbor)

    # Construct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    return path, g[goal]


# ---------------- USER INPUT ----------------
# Number of nodes
#n = int(input("Enter the number of nodes: "))
# Graph representation (adjacency list)
#graph = {}

# Heuristic values
#h = {}
