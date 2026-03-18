import heapq

def dijkstra(graph, start):
    # Priority queue
    pq = [(0, start)]
    
    # Distance dictionary
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example graph (Indian cities)
graph = {
    "Hyderabad": {"Bangalore": 570, "Chennai": 630, "Mumbai": 710},
    "Bangalore": {"Hyderabad": 570, "Chennai": 350},
    "Chennai": {"Hyderabad": 630, "Bangalore": 350, "Mumbai": 1330},
    "Mumbai": {"Hyderabad": 710, "Chennai": 1330}
}

start_city = input("Enter starting city: ")

result = dijkstra(graph, start_city)

print("\nShortest distances:")
for city, distance in result.items():
    print(f"{city}: {distance} km")
