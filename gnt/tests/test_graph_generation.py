import pytest 

def test_erdos_renyi():
    from gnt.generators import erdos_renyi_graph, describe
    g = erdos_renyi_graph(5, 0.5)
    text = describe(g)
    print(text)