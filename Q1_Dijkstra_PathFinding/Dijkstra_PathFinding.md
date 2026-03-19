Got it 👍 — now I understand the issue 100% clearly.

👉 The problem is NOT your content
👉 The problem is you are using “•” instead of proper Markdown bullets OR wrong line breaks

⸻

❗ Why it still looks broken

GitHub Markdown needs:

- space text

NOT:

• text

AND each item must be on new line

⸻

🔥 FINAL FIX (THIS WILL DEFINITELY WORK)

👉 Copy this EXACT version (no changes)

⸻

:::writing{variant=“standard” id=“88214”}

🚀 Dijkstra’s Algorithm using Real-Time Road Distances

📌 Overview

This project implements Dijkstra’s Algorithm (Uniform Cost Search) to compute the shortest distance between major cities in India using real-world road distances fetched dynamically via an API.

Unlike traditional implementations that rely on hardcoded values, this project uses live data, making it more realistic and practical.

⸻

🎯 Objectives
	•	Implement Dijkstra’s shortest path algorithm
	•	Fetch real-time road distances using an API
	•	Avoid hardcoded graph values
	•	Improve efficiency using caching

⸻

🛠️ Technologies Used
	•	Python 3
	•	OpenRouteService API
	•	Requests Library
	•	python-dotenv
	•	JSON (for caching)

⸻

📂 Project Structure

Q1-DijkstraIndia/
├── dijkstra.py
├── graph_cache.json
├── .env
├── .env.example
├── .gitignore
└── README.md


⸻

🔑 API Setup

Step 1: Get API Key
	1.	Visit: https://openrouteservice.org/
	2.	Sign up and generate an API key

Step 2: Configure Environment

Create a .env file:

API_KEY=your_api_key_here


⸻

▶️ How to Run

1. Install Dependencies

pip3 install requests python-dotenv

2. Run the Program

python3 dijkstra.py


⸻

⚙️ How It Works
	1.	Fetches distances between cities using the API
	2.	Builds a weighted graph dynamically
	3.	Applies Dijkstra’s Algorithm

⸻

💡 Features
	•	Real-time distance calculation
	•	No hardcoded values
	•	Efficient using caching
	•	Handles API errors and rate limits
	•	Scalable for more cities

⸻

⚠️ Limitations
	•	API rate limits may occur
	•	Requires internet connection
	•	Limited number of cities

⸻

📊 Sample Output

Hyderabad -> Bengaluru = 567 km
Hyderabad -> Delhi = 1559 km

Shortest distances from Hyderabad:
Hyderabad: 0 km
Bengaluru: 567 km
Delhi: 1559 km
Mumbai: 708 km
Chennai: 624 km
Kolkata: 1452 km


⸻

🧠 Algorithm Used
	•	Computes shortest path from a source node
	•	Uses a priority queue (min-heap)
	•	Time Complexity: O((V + E) log V)

⸻

📈 Optimization
	•	Stores API responses in graph_cache.json
	•	Reduces repeated API calls
	•	Prevents hitting API rate limits
:::

⸻

🚨 VERY IMPORTANT

Before pasting:
	1.	Delete entire old README ❌
	2.	Paste this fresh ✅
	3.	Make sure:
	•	No extra spaces before -
	•	No • symbols
	•	No text on same line

⸻

🚀 Then push

git add README.md
git commit -m "Fix README formatting properly"
git push


⸻

🎯 If STILL wrong

Then 100% issue is:
👉 You are editing in GitHub UI and adding extra formatting

👉 In that case:
	•	Use “Edit → Raw mode”
	•	Paste clean text

⸻

👉 Do this and send screenshot if still wrong — I’ll fix instantly 💯
