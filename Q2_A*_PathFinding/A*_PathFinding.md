# UGV Pathfinding using A* Algorithm

## Overview
This project simulates an Unmanned Ground Vehicle (UGV) navigating a grid-based environment using the A* search algorithm. The objective is to find the shortest path from a start node to a goal node while avoiding obstacles placed within the grid.

The system models a real-world scenario where a robot must efficiently navigate through a constrained environment such as a battlefield or terrain map.

---

## Features
- Grid-based environment representation
- Random obstacle generation with configurable density
- Implementation of A* pathfinding algorithm
- Visualization of grid, obstacles, and shortest path using matplotlib
- Supports different obstacle density levels (low, medium, high)
- Displays performance metrics such as path length and nodes explored

---

## Technologies Used
- Python
- NumPy
- Matplotlib

---

## How to Run

### 1. Install dependencies
```
pip3 install -r requirements.txt
```

### 2. Run program
```
python3 ugv.py
```

---

## How It Works
1. A grid environment is created using NumPy
2. Obstacles are randomly placed based on density
3. Start and goal nodes are defined
4. The A* algorithm is applied to compute the shortest path
5. The final path is visualized using matplotlib

---

## Obstacle Density
- Low density (~10–20%)
- Medium density (~30%)
- High density (~50%)

---

## Output
- Displays grid with obstacles
- Shows shortest path from start to goal
- Prints:
  - Path Length
  - Nodes Explored
  - Time Taken

---

## Algorithm Used
A* Search Algorithm:

```
f(n) = g(n) + h(n)
```

- g(n): Cost from start node
- h(n): Heuristic (Manhattan distance)

---

## Measures of Effectiveness
- Path Length
- Nodes Explored
- Time Taken
- Grid Size

---
## Obstacle Density Levels
| Level | Density |
|-------|---------|
| Low | 15% of cells are obstacles |
| Medium | 30% of cells are obstacles |
| High | 50% of cells are obstacles |

---
## Measures of Effectiveness
| Metric | Description |
|--------|-------------|
| Density Level | Obstacle density used for the run |
| Grid Size | Fixed at 70 x 70 km |
| Start / Goal | User-specified positions |
| Straight-line Distance | Euclidean (theoretical minimum) distance |
| Path Length | Actual distance travelled by the UGV |
| Path Optimality | Ratio of straight-line to path length (higher = better) |
| Nodes Expanded | Number of nodes processed by A* |
| Path Nodes | Total cells in the final path |
| Direction Changes | Number of turns taken along the path |
| Time Taken | Computation time in milliseconds |

---

## Project Structure
```
Q2-UGVPathfinder/
├── ugv.py
├── requirements.txt
└── README.md
```
