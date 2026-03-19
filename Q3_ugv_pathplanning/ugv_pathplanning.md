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

## Measures of Effectiveness
- Steps Taken  
- Replans Triggered  
- Time Taken  
- Path Efficiency  

---

## Project Structure
```
Q3-UGVDynamic/
├── ugv_dynamic.py
├── requirements.txt
└── README.md
```
