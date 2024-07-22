import pytest
import networkx as nx

def test_complete_graph():
    g = nx.complete_graph(5)
    from gnt.algorithms.collections import get_compatible_algorithms
    algorithms = get_compatible_algorithms(g)
    
def test_all_algorithms():
    from gnt.algorithms.collections import get_algorithms
    algorithms = get_algorithms()
    for algorithm in algorithms:
        print(algorithm.__name__)
        
def test_describe():
    from gnt.algorithms.collections import describe
    from gnt.algorithms.collections import get_algorithms
    algorithms = get_algorithms()
    for algorithm in algorithms:
        print(describe(algorithm))

    