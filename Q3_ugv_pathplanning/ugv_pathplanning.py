import numpy as np
import matplotlib.pyplot as plt
import heapq
import random
import time

ROWS = 30
COLS = 30

# 4-direction movement
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

# Heuristic (Manhattan)
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# Generate grid with static obstacles
def generate_grid(density=0.2):
    grid = np.zeros((ROWS, COLS))
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1
    return grid

# A* Algorithm
def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

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

        for d in DIRS:
            neighbor = (current[0]+d[0], current[1]+d[1])

            if (0 <= neighbor[0] < ROWS and
                0 <= neighbor[1] < COLS and
                grid[neighbor] == 0):

                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f_score = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))
                    came_from[neighbor] = current

    return None

# Add dynamic obstacles
def add_dynamic_obstacles(grid, count=5):
    for _ in range(count):
        i = random.randint(0, ROWS-1)
        j = random.randint(0, COLS-1)
        grid[i][j] = 1

# Visualization
def visualize(grid, path, current, goal):
    display = grid.copy()

    for p in path:
        display[p] = 0.5

    display[current] = 0.8
    display[goal] = 0.9

    plt.imshow(display, cmap="viridis")
    plt.title("Dynamic UGV Pathfinding")
    plt.pause(0.3)
    plt.clf()

# MAIN
if __name__ == "__main__":

    grid = generate_grid(0.2)

    start = (0, 0)
    goal = (ROWS-1, COLS-1)

    grid[start] = 0
    grid[goal] = 0

    current = start
    total_path = [current]
    replans = 0

    start_time = time.time()

    plt.figure()

    while current != goal:
        path = astar(grid, current, goal)

        if path is None:
            print("No path possible!")
            break

        # move step by step
        for step in path[1:]:
            current = step
            total_path.append(current)

            visualize(grid, path, current, goal)

            # every few steps add obstacles
            if random.random() < 0.2:
                add_dynamic_obstacles(grid, count=5)
                replans += 1
                break  # trigger replanning

    end_time = time.time()

    print("\n--- RESULTS ---")
    print("Reached Goal:", current == goal)
    print("Steps Taken:", len(total_path))
    print("Replans Triggered:", replans)
    print("Time Taken:", round(end_time - start_time, 4), "seconds")

    plt.show()
