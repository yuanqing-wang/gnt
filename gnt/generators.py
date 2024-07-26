import networkx as nx
from networkx import erdos_renyi_graph

def describe(graph):
    """Describe a graph. """
    edges = list(graph.edges())
    edges = str(edges).replace("[", "").replace("]", "")
    return f"graph with edges {edges}"

    