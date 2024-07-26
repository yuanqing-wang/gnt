import pytest

def test_generate_problems():
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import Diameter
    
    g = erdos_renyi_graph(5, 0.5)
    diameter = Diameter()

    task, answer = generate_problem(g, diameter)
    print(task, answer)
    