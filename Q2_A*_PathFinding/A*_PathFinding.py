import numpy as np
import matplotlib.pyplot as plt
import heapq
import random
import time

# Grid size
ROWS = 30
COLS = 30

# Directions (up, down, left, right)
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Generate grid with obstacles
def generate_grid(density=0.2):
    grid = np.zeros((ROWS, COLS))
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < density:
                grid[i][j] = 1  # obstacle
    return grid

# A* Algorithm
def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    nodes_explored = 0
    
    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, nodes_explored
        
        for d in DIRS:
            neighbor = (current[0] + d[0], current[1] + d[1])
            
            if (0 <= neighbor[0] < ROWS and 
                0 <= neighbor[1] < COLS and 
                grid[neighbor] == 0):
                
                temp_g = g_score[current] + 1
                
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f_score = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))
                    came_from[neighbor] = current
    
    return None, nodes_explored

# Visualization
def visualize(grid, path, start, goal):
    display = grid.copy()
    
    for node in path:
        display[node] = 0.5  # path
    
    display[start] = 0.8  # start
    display[goal] = 0.9   # goal
    
    plt.imshow(display, cmap="viridis")
    plt.title("UGV Pathfinding (A*)")
    plt.colorbar()
    plt.show()

# MAIN
if __name__ == "__main__":
    
    density = 0.2  # change for difficulty
    
    grid = generate_grid(density)
    
    start = (0, 0)
    goal = (ROWS-1, COLS-1)
    
    # Ensure start & goal are not blocked
    grid[start] = 0
    grid[goal] = 0
    
    start_time = time.time()
    path, nodes = astar(grid, start, goal)
    end_time = time.time()
    
    print("\n--- RESULTS ---")
    
    if path:
        print("Path found!")
        print("Path Length:", len(path))
        print("Nodes Explored:", nodes)
        print("Time Taken:", round(end_time - start_time, 5), "seconds")
        
        visualize(grid, path, start, goal)
    else:
        print("No path found!")
