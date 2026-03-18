import heapq
import random

# Grid size
SIZE = 20   # you can change to 70

# Generate grid with obstacle density
def generate_grid(size, density):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < density:
                row.append(1)  # obstacle
            else:
                row.append(0)  # free
        grid.append(row)
    return grid

# Heuristic (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f, neighbor))
                    came_from[neighbor] = current

    return None

# Example usage
grid = generate_grid(SIZE, 0.2)  # 20% obstacles

start = (0, 0)
goal = (SIZE-1, SIZE-1)

path = astar(grid, start, goal)

if path:
    print("Path found:", path)
    print("Path length:", len(path))
else:
    print("No path found")
