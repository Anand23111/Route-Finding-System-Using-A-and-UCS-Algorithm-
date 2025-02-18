
# Route Finding System Using A* and UCS Algorithm

## Overview
This project implements a route-finding system that utilizes **A\* Search** and **Uniform Cost Search (UCS)** algorithms to find the most optimal route between two cities. The system loads distance data between cities from a CSV file and allows the user to choose between different search algorithms and heuristic functions.

## Features
- **A\* Search Algorithm** with user-defined heuristics (Admissible or Inadmissible).
- **Uniform Cost Search (UCS)** which finds the optimal route based purely on actual distances.
- **Heuristic Function Options**:
  - **Admissible Heuristic**: Exact road distance between cities.
  - **Inadmissible Heuristic**: Overestimated heuristic where distance is multiplied by a factor of 2.

## Algorithm Description

### A* Search Algorithm
A* is an informed search algorithm that uses both the actual travel cost (`g_score`) and an estimate of the remaining cost (`f_score = g_score + heuristic`). A* prioritizes exploring cities with the least total cost. It guarantees finding the shortest path when an admissible heuristic is used.

### Uniform Cost Search (UCS)
UCS is an uninformed search algorithm that only considers the actual travel cost (`g_score`) and guarantees finding the shortest path based on actual distances. It does not use heuristics.

### Heuristic Functions
- **Admissible Heuristic**: This heuristic function provides the exact distance between cities, ensuring an optimal solution in A* search.
- **Inadmissible Heuristic**: This function overestimates the distance by multiplying the actual road distance by 2, potentially speeding up the search but leading to suboptimal paths.

## Data Input and Structure
The program requires a CSV file (`Road_Distance.csv`) that contains the road distance data. The file should have the following structure:

| City   | City1 | City2 | City3 | ... |
|--------|-------|-------|-------|-----|
| CityA  | 0     | 50    | 120   | ... |
| CityB  | 50    | 0     | 80    | ... |
| CityC  | 120   | 80    | 0     | ... |
| ...    | ...   | ...   | ...   | ... |

The first column represents the cities, and the other columns represent the distances between those cities.

## Installation and Usage

### Prerequisites
- Python 3.x
- Required libraries:
  - `csv`
  - `heapq`

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/route-finding-system.git
   cd route-finding-system
