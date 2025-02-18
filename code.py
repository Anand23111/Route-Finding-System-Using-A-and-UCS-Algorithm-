import csv
import sys
import heapq


def load_data(file_path):
    data = {}
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        cities = next(reader)[1:]
        for row in reader:
            city = row[0]
            distances = []
            for distance in row[1:]:
                try:
                    distances.append(int(distance))
                except ValueError:
                    distances.append(sys.maxsize) 
            data[city] = dict(zip(cities, distances))
    return data

# admissible and inadmissible heuristic functions

def admissible_heuristic(city, goal, data):
   
   
    return data[city][goal]

def inadmissible_heuristic(city, goal, data):
    # Use simple heuristic based on the provided road distance data
    # heuristic  may overestimate the actual cost, making it inadmissible
    return data[city][goal] * 2  # Overestimate by a factor of 2

# A* algorithm with heuristic
def astar_search(graph, start, end, heuristic_func, data):
    visited = set()
    queue = [(0, start)]
    came_from = {}
    g_score = {city: sys.maxsize for city in graph}
    g_score[start] = 0

    while queue:
        _, current = heapq.heappop(queue)

        if current == end:
            path = reconstruct_path(came_from, end)
            return path

        visited.add(current)

        for neighbor, distance in graph[current].items():
            if neighbor in visited:
                continue

            tentative_g_score = g_score[current] + distance

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = g_score[neighbor] + heuristic_func(neighbor, end, data)
                heapq.heappush(queue, (f_score, neighbor))

    return None

# Uniform Cost Search (UCS) algorithm
def uniform_cost_search(graph, start, end):
    visited = set()
    queue = [(0, start)]
    came_from = {}
    g_score = {city: sys.maxsize for city in graph}
    g_score[start] = 0

    while queue:
        _, current = heapq.heappop(queue)

        if current == end:
            path = reconstruct_path(came_from, end)
            return path

        visited.add(current)

        for neighbor, distance in graph[current].items():
            if neighbor in visited:
                continue

            tentative_g_score = g_score[current] + distance

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(queue, (g_score[neighbor], neighbor))

    return None

# Reconstruct the path from the goal to the start
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Main function
def find_route(data, start_city, end_city, search_algorithm, heuristic_func):
    if search_algorithm == 'A*':
        path = astar_search(data, start_city, end_city, heuristic_func, data)
    elif search_algorithm == 'UCS':
        path = uniform_cost_search(data, start_city, end_city)
    else:
        return "Invalid search algorithm. Please use 'A*' or 'UCS'."

    if not path:
        return f"No route found between {start_city} and {end_city}"

    route = " -> ".join(path)
    total_distance = calculate_total_distance(data, path)

    return f"Route: {route}\nTotal Distance: {total_distance} km"

# finding total distance of a path
def calculate_total_distance(data, path):
    total_distance = 0
    for i in range(len(path) - 1):
        city1, city2 = path[i], path[i + 1]
        total_distance += data[city1][city2]
    return total_distance

if __name__ == "__main__":
    data = load_data('Road_Distance.csv')

    while True:
        start_city = input("Enter the starting city: ")
        end_city = input("Enter the destination city: ")
        search_algorithm = input("Enter the search algorithm (A* or UCS): ").strip().upper()
        heuristic_choice = input("Enter the heuristic (admissible or inadmissible): ").strip().lower()

        if heuristic_choice == 'admissible':
            heuristic_func = admissible_heuristic
        elif heuristic_choice == 'inadmissible':
            heuristic_func = inadmissible_heuristic
        else:
            print("Invalid heuristic choice. Please use 'admissible' or 'inadmissible'.")
            continue

        result = find_route(data, start_city, end_city, search_algorithm, heuristic_func)
        print(result)

        another = input("Do you want to find another route? (yes/no): ").strip().lower()
        if another != "yes":
            break
