UGV Path Planning in Static and Dynamic Environments

1. Introduction

An Unmanned Ground Vehicle (UGV) is an autonomous robot used for navigation in complex environments such as battlefields. The objective is to find the shortest and safest path from a start node to a goal node while avoiding obstacles.

The environment is modeled as a grid (e.g., 70 × 70 km area), where each cell represents a location.

⸻

2. Problem Statement

Design an algorithm that enables a UGV to:
	•	Navigate from a start node to a goal node
	•	Avoid obstacles present in the environment
	•	Find the shortest possible path
	•	Adapt to both static and dynamic obstacles

⸻

3. Static Environment (Known Obstacles)

Description
	•	Obstacles are known beforehand
	•	Environment does not change during execution

Algorithm Used: A* (A-Star)

A* is a heuristic-based algorithm used to find the shortest path.

f(n) = g(n) + h(n)
	•	g(n): Cost from start node
	•	h(n): Estimated cost to goal (Manhattan distance)

Steps:
	1.	Initialize start node with distance 0
	2.	Assign infinity to all other nodes
	3.	Select node with minimum cost
	4.	Update neighboring nodes
	5.	Repeat until goal is reached

Advantages
	•	Guarantees shortest path
	•	Efficient for known environments

⸻

4. Dynamic Environment (Unknown / Moving Obstacles)

Description
	•	Obstacles may appear, disappear, or move
	•	Environment is not fully known in advance

Challenge
	•	Precomputed paths may become invalid
	•	Requires real-time decision making

⸻

5. Solution for Dynamic Environment

Approach: Replanning + Real-Time Sensing

The UGV continuously:
	1.	Senses environment using sensors
	2.	Updates internal map
	3.	Recomputes path if needed

⸻

Algorithms Used

1. A* with Replanning
	•	Re-run A* when obstacle is detected
	•	Simple but less efficient

2. D* Algorithm
	•	Updates only affected parts of path
	•	Suitable for dynamic changes

3. D* Lite (Recommended)
	•	Faster and more efficient version of D*
	•	Widely used in robotics

⸻

6. Working of UGV in Dynamic Environment
	1.	Compute initial path using A*
	2.	Start moving towards goal
	3.	Continuously scan environment
	4.	If obstacle detected:
	•	Update grid
	•	Recalculate path
	5.	Continue until goal is reached

⸻

7. Pseudocode

while current_position != goal:
if obstacle detected:
update map
recompute path using A*

move to next position


⸻

8. Measures of Effectiveness

For Static Environment:
	•	Path Length
	•	Computation Time
	•	Nodes Explored
	•	Optimality

For Dynamic Environment:
	•	Replanning Time
	•	Adaptability
	•	Collision Avoidance Rate
	•	Path Stability
	•	Success Rate

⸻

9. Applications
	•	Military UGV navigation
	•	Autonomous vehicles
	•	Robotics path planning
	•	Search and rescue operations
	•	Game AI simulations

⸻

10. Conclusion

In static environments, A* efficiently finds the shortest path. However, in dynamic environments, real-time adaptation is required. Algorithms like D* and D* Lite allow the UGV to update paths dynamically, ensuring safe and optimal navigation even when obstacles change over time.

⸻

11. Future Improvements
	•	Integration with real-world maps
	•	Machine learning for obstacle prediction
	•	3D environment navigation
	•	Real-time visualization
	•	Multi-agent coordination
