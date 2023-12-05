import random
import time
import psutil
import gc
from hamiltonian_path_dp import Hamiltonian_path
from hamiltonian_path_backtrack import Graph

def generate_random_graph(N):
    # Create an empty adjacency matrix (2D list)
    adj = [[0] * N for _ in range(N)]

    # Connect vertices randomly to create edges
    for i in range(N):
        for j in range(i + 1, N):
            if random.choice([True, False]):
                adj[i][j] = 1
                adj[j][i] = 1

    return adj

if __name__ == '__main__':
    N = [16, 18, 20, 25]
    for i in range(0, len(N)):
        print('N:', N[i])
        adj_matrix = generate_random_graph(N[i])
        print(adj_matrix)
        print()

        # HAMILTONIAN PATH DYNAMIC PROGRAMMING
        gc.collect()
        start = time.time()

        hamilton_path_dp = Hamiltonian_path(adj_matrix[:len(adj_matrix)-1], len(adj_matrix)-1)

        elapsed_time = time.time() - start
        process = psutil.Process()
        memory_usage = process.memory_info().rss / (1024 ** 2)  # in megabytes

        unit = 's'
        if elapsed_time < 1:
            elapsed_time *= 1000
            unit = 'ms'

        print('Hamiltonian Path Dynamic Programming:')
        print(f'    Elapsed Time: {elapsed_time:.2f} {unit}')
        print(f'    Memory Usage: {memory_usage:.2f} MB')
        if hamilton_path_dp:
            print('    Exist: YES')
        else:
            print('    Exist: NO')

        print()

        # HAMILTONIAN PATH BACTRACKING
        graph = Graph(N[i])
        graph.graph = adj_matrix

        gc.collect()
        start = time.time()

        hamilton_path_backtracking = graph.hamPath()

        elapsed_time = time.time() - start
        process = psutil.Process()
        memory_usage = process.memory_info().rss / (1024 ** 2)  # in megabytes

        unit = 's'
        if elapsed_time < 1:
            elapsed_time *= 1000
            unit = 'ms'

        print('Hamiltonian Path Backtracking:')
        print(f'    Elapsed Time: {elapsed_time:.2f} {unit}')
        print(f'    Memory Usage: {memory_usage:.2f} MB')
        if hamilton_path_backtracking:
            print('    Exist: YES')
        else:
            print('    Exist: NO')

        print()
        print()


