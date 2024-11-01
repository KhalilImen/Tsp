from src.city import City
from src.tsp import genetic_algorithm
import numpy as np

def main():
    
    cities = [
        City(0, 0, 0, (8, 18), 10),
        City(1, 2, 3, (9, 17), 15),
        City(2, 5, 1, (10, 16), 8),
        City(3, 6, 7, (7, 19), 20)
    ]
    
    
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    
    
    best_route, best_distance = genetic_algorithm(distances, len(cities))
    print(f"Best route: {best_route}")
    print(f"Best distance: {best_distance[0]}")

if __name__ == "__main__":
    main()
