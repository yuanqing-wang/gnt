import pytest

def test_generate_problems():
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms.collections import get_algorithms
    
    
    g = erdos_renyi_graph(5, 0.5)
    algorithms = get_algorithms()
    for algorithm in algorithms:
        task, answer = generate_problem(g, algorithm)
        print(task, answer)
    
    