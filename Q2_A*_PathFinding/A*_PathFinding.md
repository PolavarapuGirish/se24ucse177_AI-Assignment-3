# UGV Pathfinding using A* Algorithm

## Overview
This project simulates an Unmanned Ground Vehicle (UGV) navigating a grid environment using the A* search algorithm to find the shortest path from start to goal while avoiding obstacles.

---

## Features
- Grid-based environment
- Random obstacle generation
- A* pathfinding algorithm
- Visualization using matplotlib
- Supports different obstacle densities

---

## Technologies Used
- Python
- NumPy
- Matplotlib

---

## How to Run

### 1. Install dependencies
pip3 install -r requirements.txt

### 2. Run program
python3 ugv.py

---

## Output
- Displays grid with obstacles
- Shows shortest path from start to goal
- Prints path length and nodes explored

---

## Algorithm Used
A* Search Algorithm:
f(n) = g(n) + h(n)
