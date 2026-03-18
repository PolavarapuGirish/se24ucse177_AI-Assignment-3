UGV Path Planning using A* Algorithm (Python)

  Description

This project simulates an Unmanned Ground Vehicle (UGV) navigating through a battlefield represented as a 2D grid. The UGV finds the shortest path from a user-defined start node to a goal node while avoiding obstacles.

The environment is modeled as a grid (e.g., 70 × 70 km area), where:
	•	Each cell represents a location
	•	Obstacles are pre-defined or randomly generated
	•	The UGV must safely reach the destination

⸻

  Objective
	•	Design an algorithm for autonomous navigation
	•	Avoid obstacles while minimizing travel distance
	•	Evaluate performance using effectiveness metrics

⸻

  Algorithm Used

A (A-Star) Algorithm*

A* is a heuristic-based search algorithm that finds the shortest path efficiently.

It uses the function:

f(n) = g(n) + h(n)

Where:
	•	g(n) = cost from start node
	•	h(n) = estimated cost to goal (Manhattan distance)

⸻

  Features
	•	Grid-based environment (customizable size)
	•	Random obstacle generation
	•	Three obstacle density levels:
	•	Low (10%)
	•	Medium (20–30%)
	•	High (40%+)
	•	Shortest path computation using A*
	•	Easy to modify and extend

⸻

  Files
	•	ugv_path_planning.py – main implementation

⸻

  How to Run
	1.	Open terminal
	2.	Navigate to project folder
	3.	Run:

python3 ugv_path_planning.py

⸻

  Example

Start Node: (0, 0)
Goal Node: (19, 19)

Output:
	•	Path found
	•	Path length
	•	Sequence of coordinates

⸻

  Measures of Effectiveness

The performance of the algorithm is evaluated using:
	1.	Path Length
	•	Total steps taken to reach goal
	2.	Computation Time
	•	Time required to compute path
	3.	Nodes Explored
	•	Number of nodes visited during search
	4.	Success Rate
	•	Ability to find path under different obstacle densities
	5.	Optimality
	•	Whether the shortest path is found (A* ensures optimality)

⸻

  Applications
	•	Military UGV navigation
	•	Robotics path planning
	•	Autonomous vehicles
	•	Game AI and simulations

⸻

  Future Improvements
	•	Visualization of grid and path
	•	Real-world map integration
	•	Dynamic obstacle handling
	•	GUI-based simulation
