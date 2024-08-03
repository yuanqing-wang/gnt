import networkx as nx
from typing import Any, Callable
from .generators import erdos_renyi_graph
from .generators import describe as describe_generator

GENERAL_INSTRUCTION = """
Return the answer in [] brackets. 
If the answer is a floating point number, round it to 2 decimal places.
"""
    
def generate_problem(
        graph: nx.Graph,
        algorithm: Callable[[nx.Graph], Any] = None,
):
    """Generate a problem for a graph and an algorithm. """
    graph_description = describe_generator(graph)
    task = f"Given a {graph_description}, " \
        + f"what is its {algorithm.name}, {algorithm.description}? " \
        + GENERAL_INSTRUCTION
    answer = algorithm.implementation(graph)
    return task, answer
    
    