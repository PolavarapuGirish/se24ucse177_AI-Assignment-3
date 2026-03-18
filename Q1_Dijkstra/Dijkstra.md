Dijkstra Algorithm – Indian Cities (Python)

Description

This project implements Dijkstra’s Algorithm (Uniform Cost Search) in Python to find the shortest distance from a selected starting city to all other cities.

The cities are represented as nodes and the roads between them are represented as weighted edges (distances in kilometers).

⸻

Objective
	•	To understand how shortest path algorithms work
	•	To apply Dijkstra’s Algorithm on real-world inspired data
	•	To simulate road distances between Indian cities

⸻

Algorithm

Dijkstra’s Algorithm is a greedy algorithm used for finding the shortest path in a graph with non-negative weights.

Steps:
	1.	Set distance of start node to 0 and others to infinity
	2.	Pick the node with the smallest distance
	3.	Update distances of neighboring nodes
	4.	Repeat until all nodes are visited

⸻

Features
	•	Simple and beginner-friendly implementation
	•	Uses Python dictionary to represent graph
	•	Uses priority queue (heapq) for efficiency
	•	Easy to modify (add more cities and distances)
	•	Works for any connected graph
	
⸻

How to Run
	1.	Open terminal
	2.	Navigate to project folder
	3.	Run:

python3 dijkstra_india.py

⸻

Example

Input:
Enter starting city: Hyderabad

Output:
Hyderabad: 0 km
Bangalore: 570 km
Chennai: 630 km
Mumbai: 710 km

⸻

Requirements
	•	Python 3
	•	No external libraries required

⸻

Applications
	•	GPS navigation systems
	•	Network routing protocols
	•	Transportation and logistics planning
	•	Map-based services

⸻

Future Improvements
	•	Add more Indian cities with real data
	•	Use file input instead of hardcoding graph
	•	Visualize graph using libraries like matplotlib or networkx
	•	Build a GUI or web interface
