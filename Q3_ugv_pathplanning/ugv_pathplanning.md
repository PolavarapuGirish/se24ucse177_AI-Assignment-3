# UGV Path Planning using A* Algorithm (Python)

## Introduction
An Unmanned Ground Vehicle (UGV) is an autonomous robot used for navigation in complex environments such as battlefields. The objective is to find the shortest and safest path from a start node to a goal node while avoiding obstacles.

## Environment
The environment is modeled as a grid (e.g., 70 × 70 km area), where:

- Each cell represents a location
- Obstacles are pre-defined or randomly generated
- The UGV must safely reach the destination

## Problem Statement
Design an algorithm that enables a UGV to:

- Navigate from a start node to a goal node
- Avoid obstacles present in the environment
- Find the shortest possible path
- Adapt to both static and dynamic obstacles

## Static Environment (Known Obstacles)

### Description
- Obstacles are known beforehand
- Environment does not change during execution

### Algorithm Used: A* (A-Star)
A* is a heuristic-based algorithm used to find the shortest path.

f(n) = g(n) + h(n)

- g(n): Cost from start node
- h(n): Estimated cost to goal (Manhattan distance)

### Steps
1. Initialize start node with distance 0
2. Assign infinity to all other nodes
3. Select node with minimum cost
4. Update neighboring nodes
5. Repeat until goal is reached

### Advantages
- Guarantees shortest path
- Efficient for known environments

## Dynamic Environment (Unknown / Moving Obstacles)

### Description
- Obstacles may appear, disappear, or move
- Environment is not fully known in advance

### Solution Approach
- Use real-time sensing to detect obstacles
- Update the grid dynamically
- Recompute path when changes occur

### Algorithms Used
- A* with Replanning
- D* Algorithm
- D* Lite (recommended)

## Working of UGV
1. Compute initial path using A*
2. Start moving towards goal
3. Continuously scan environment
4. If obstacle detected:
   - Update map
   - Recalculate path
5. Continue until goal is reached

## Pseudocode
while current_position != goal:
if obstacle_detected:
    update_map()
    recompute_path_using_A_star()

move_to_next_position()

## Features
- Grid-based environment (customizable size)
- Random obstacle generation
- Three obstacle density levels:
  - Low (10%)
  - Medium (20–30%)
  - High (40%+)
- Shortest path computation using A*
- Easy to modify and extend

## How to Run
1. Open terminal
2. Navigate to project folder
3. Run: ugv_pathplanning.py

## Output
- Path found
- Path length
- Sequence of coordinates

## Measures of Effectiveness

### Static Environment
- Path Length
- Computation Time
- Nodes Explored
- Optimality

### Dynamic Environment
- Replanning Time
- Adaptability
- Collision Avoidance Rate
- Path Stability
- Success Rate

## Applications
- Military UGV navigation
- Robotics path planning
- Autonomous vehicles
- Game AI and simulations

## Future Improvements
- Visualization of grid and path
- Real-world map integration
- Dynamic obstacle handling
- GUI-based simulation

## Requirements
- Python 3
