# UGV Pathfinding with Dynamic Obstacles

## Overview
This project extends the UGV pathfinding problem by introducing dynamic obstacles. Unlike static environments, obstacles can appear during the movement of the UGV, making the pathfinding process more challenging and realistic.

The system uses a replanning approach based on the A* algorithm to dynamically adjust the path as new obstacles are introduced.

---

## Problem Statement
In real-world environments, obstacles are not always known beforehand and may change over time. The objective is to enable an Unmanned Ground Vehicle (UGV) to navigate from a start node to a goal node while adapting to dynamically appearing obstacles and still finding an optimal path.

---

## Features
- Grid-based environment representation  
- Static obstacle generation at initialization  
- Dynamic obstacles appearing during traversal  
- Replanning using A* algorithm  
- Step-by-step movement simulation  
- Visualization of grid and path updates  
- Performance metrics tracking  

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
python3 ugv_dynamic.py
```

---

## How It Works
1. A grid environment is generated  
2. Static obstacles are placed initially  
3. A* algorithm computes an initial path  
4. The UGV starts moving step-by-step  
5. Dynamic obstacles appear randomly during traversal  
6. If the current path is blocked, the algorithm replans using A*  
7. The process continues until the goal is reached or no path exists  

---

## Obstacle Behavior
- Static obstacles are generated at the start  
- Dynamic obstacles appear randomly during execution  
- Obstacles can block the current path  
- Replanning is triggered when path becomes invalid  

---

## Output
- Displays grid with obstacles and path  
- Shows movement of UGV in real-time  
- Prints:
  - Steps Taken  
  - Replans Triggered  
  - Time Taken  

---

## Algorithm Used
Replanning A* Search:

```
f(n) = g(n) + h(n)
```

- g(n): Cost from start node  
- h(n): Heuristic (Manhattan distance)  
- Allows dynamic adjustment of path  

---

## Obstacle Density Levels
| Level | Initial Static Density |
|-------|------------------------|
| Low | 15% of cells are obstacles |
| Medium | 30% of cells are obstacles |
| High | 50% of cells are obstacles |

Dynamic obstacles are spawned in waves of 8 every 5 steps regardless of the density level chosen.

---
## Measures of Effectiveness
| Metric | Description |
|--------|-------------|
| Obstacle Density Level | Initial static obstacle density used for the run |
| Grid Size | Fixed at 70 x 70 km |
| Start / Goal | User-specified positions |
| Straight-line Distance | Euclidean (theoretical minimum) distance |
| Initial Planned Distance | Distance of the path A* planned before traversal began |
| Actual Distance Travelled | Real distance covered by the UGV including all detours |
| Extra Distance (replanning) | Additional distance caused by dynamic obstacle detours |
| Path Optimality | Ratio of straight-line to actual distance (higher = better) |
| Total Replans Triggered | How many times the UGV had to abandon its plan and replan |
| Dynamic Obstacles Spawned | Total new obstacles that appeared during the run |
| Steps Taken | Total cells visited by the UGV |
| Direction Changes | Number of turns taken along the actual path |
| Time Taken | Total simulation time in milliseconds |

---

## Project Structure
```
Q3_ugv_pathplanning/
├── requirements.txt
├── ugv_pathplanning.md
├── ugv_pathplanning.py
```
---
## Author

Polavarapu Girish  
Roll No: SE24UCSE177  

Course: CS-2201 – Artificial Intelligence
