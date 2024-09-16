import networkx as nx
from networkx import erdos_renyi_graph

def describe(graph):
    """Describe a graph. """
    edges = list(graph.edges())
    num_edges = len(edges)
    edges = str(edges).replace("[", "").replace("]", "")
    num_nodes = graph.number_of_nodes()
    
    return f"graph with {num_nodes} nodes indexed 0 through {num_nodes-1} and {num_edges} edges {edges}, " + \
        "where an edge (i,j) means that node i and node j are connected with an directed edge."

    