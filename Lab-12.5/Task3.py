import random
import math
from typing import List, Tuple

Coord = Tuple[float, float]

def generate_sensors(n: int, xlim=(0, 100), ylim=(0, 100)) -> List[Coord]:
    return [(random.uniform(*xlim), random.uniform(*ylim)) for _ in range(n)]

def euclidean(a: Coord, b: Coord) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])

def total_distance(path: List[Coord]) -> float:
    return sum(euclidean(path[i], path[(i+1)%len(path)]) for i in range(len(path)))

# Greedy TSP
def greedy_tsp(sensors: List[Coord]) -> List[Coord]:
    unvisited = sensors[:]
    path = [unvisited.pop(0)]
    while unvisited:
        last = path[-1]
        next_sensor = min(unvisited, key=lambda s: euclidean(last, s))
        path.append(next_sensor)
        unvisited.remove(next_sensor)
    return path

# Genetic Algorithm for TSP
def genetic_tsp(sensors: List[Coord], pop_size=100, generations=500, mutation_rate=0.02) -> List[Coord]:
    def create_individual():
        p = sensors[1:]
        random.shuffle(p)
        return [sensors[0]] + p

    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(1, len(sensors)), 2))
        child = [None]*len(sensors)
        child[0] = sensors[0]
        child[start:end] = parent1[start:end]
        fill = [s for s in parent2 if s not in child]
        idx = 0
        for i in range(1, len(sensors)):
            if child[i] is None:
                child[i] = fill[idx]
                idx += 1
        return child

    def mutate(ind):
        if random.random() < mutation_rate:
            i, j = random.sample(range(1, len(sensors)), 2)
            ind[i], ind[j] = ind[j], ind[i]
        return ind

    population = [create_individual() for _ in range(pop_size)]
    for _ in range(generations):
        population.sort(key=total_distance)
        next_gen = population[:pop_size//10]  # Elitism
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:pop_size//2], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            next_gen.append(child)
        population = next_gen
    best = min(population, key=total_distance)
    return best

def print_path(path: List[Coord], name: str, max_points: int = 5):
    print(f"\n{name} Path (first {max_points} points):")
    for i, coord in enumerate(path[:max_points]):
        print(f"  {i+1}: {coord}")
    if len(path) > max_points:
        print(f"  ... (total {len(path)} points)")

def main():
    n = 20  # Number of sensors
    sensors = generate_sensors(n)

    # Random path
    random_path = sensors[:]
    random.shuffle(random_path)
    dist_random = total_distance(random_path)
    print(f"Random Path Distance: {dist_random:.2f}")
    print_path(random_path, "Random")

    # Greedy
    greedy_path = greedy_tsp(sensors)
    dist_greedy = total_distance(greedy_path)
    print(f"Greedy Path Distance: {dist_greedy:.2f}")
    print_path(greedy_path, "Greedy")

    # Genetic Algorithm
    ga_path = genetic_tsp(sensors)
    dist_ga = total_distance(ga_path)
    print(f"Genetic Algorithm Path Distance: {dist_ga:.2f}")
    print_path(ga_path, "Genetic Algorithm")

    print("\nSummary:")
    print(f"Random: {dist_random:.2f}, Greedy: {dist_greedy:.2f}, Genetic: {dist_ga:.2f}")

if __name__ == "__main__":
    main()