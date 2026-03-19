 Dijkstra’s Algorithm with Real-Time Distance API

 Overview

This project implements Dijkstra’s Algorithm (Uniform Cost Search) to find the shortest path between cities in India using real-world road distances fetched dynamically from an API.

Unlike traditional implementations that use hardcoded values, this project integrates an external API to obtain accurate, real-time distances, making it more practical and realistic.

⸻

 Objectives
	•	Implement Dijkstra’s Algorithm
	•	Use real-time road distance data
	•	Avoid hardcoded values
	•	Optimize performance using caching

⸻

 Technologies Used
	•	Python 3
	•	OpenRouteService API
	•	Requests Library
	•	python-dotenv
	•	JSON (for caching)

⸻

 Project Structure

Q1-DijkstraIndia/
│
├── dijkstra.py         # Main implementation
├── graph_cache.json    # Stores cached distances
├── .env                # API key (not pushed to GitHub)
├── .env.example        # Template for API key
├── .gitignore          # Ignores sensitive files
└── README.md           # Project documentation


⸻

 API Setup

Step 1: Get API Key
	1.	Go to: https://openrouteservice.org/
	2.	Sign up and generate an API key

Step 2: Add API Key

Create a .env file:

API_KEY=your_api_key_here


⸻

 How to Run

1. Install dependencies

pip3 install requests python-dotenv

2. Run the program

python3 dijkstra.py


⸻

 How It Works
	1.	The program fetches distances between cities using the API
	2.	Builds a graph dynamically
	3.	Applies Dijkstra’s Algorithm
	4.	Outputs shortest distances from a selected source city

⸻

 Features
	•	✅ Real-time distance calculation
	•	✅ No hardcoded data
	•	✅ Efficient using caching
	•	✅ Handles API errors gracefully
	•	✅ Scalable for more cities

⸻

 Limitations
	•	API rate limits may occur (handled partially using caching)
	•	Requires internet connection

⸻

 Sample Output

Hyderabad -> Bengaluru = 567 km
Hyderabad -> Delhi = 1559 km

Shortest distances from Hyderabad:
Bengaluru: 567 km
Delhi: 1559 km
Mumbai: 708 km
Chennai: 624 km
Kolkata: 1452 km


⸻

 Concept Used

Dijkstra’s Algorithm
	•	Finds the shortest path from a source node to all other nodes
	•	Uses a priority queue
	•	Works for graphs with non-negative weights

⸻

 Conclusion

This project demonstrates how classical algorithms like Dijkstra can be enhanced using real-world data and modern APIs, making them more applicable to real-life scenarios such as navigation systems.
