import requests
import os
import json
import heapq
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

CACHE_FILE = "graph_cache.json"

cities = ["Hyderabad", "Bengaluru", "Delhi", "Mumbai", "Chennai", "Kolkata"]

coords = {
    "Hyderabad": [78.4867, 17.3850],
    "Bengaluru": [77.5946, 12.9716],
    "Delhi": [77.1025, 28.7041],
    "Mumbai": [72.8777, 19.0760],
    "Chennai": [80.2707, 13.0827],
    "Kolkata": [88.3639, 22.5726]
}

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(graph):
    with open(CACHE_FILE, "w") as f:
        json.dump(graph, f, indent=4)

def get_distance(city1, city2):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            coords[city1],
            coords[city2]
        ]
    }

    try:
        response = requests.post(url, json=body, headers=headers)
        data = response.json()

        dist = data["routes"][0]["summary"]["distance"] / 1000
        print(f"{city1} -> {city2} = {int(dist)} km")
        return int(dist)

    except Exception as e:
        print("Error:", data)
        return float('inf')

def build_graph():
    cache = load_cache()

    if cache:
        print("Using cached data...")
        return cache

    graph = {}

    for c1 in cities:
        graph[c1] = {}
        for c2 in cities:
            if c1 != c2:
                graph[c1][c2] = get_distance(c1, c2)

    save_cache(graph)
    return graph

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    while pq:
        current_dist, current_city = heapq.heappop(pq)

        for neighbor, weight in graph[current_city].items():
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = build_graph()

    start_city = "Hyderabad"
    result = dijkstra(graph, start_city)

    print("\nShortest distances from", start_city)
    for city, dist in result.items():
        print(f"{city}: {dist} km")
