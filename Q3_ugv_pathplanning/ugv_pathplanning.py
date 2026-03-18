while current_position != goal:

    # Check for obstacle
    if detect_obstacle():
        grid = update_map(grid)
        path = astar(grid, current_position, goal)

    # Move to next step
    current_position = path[1]
    path = path[1:]
