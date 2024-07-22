from hashlib import algorithms_available
import random
from .algorithms.collections import get_algorithms
from .algorithms.collections import describe as describe_algorithm
from .generators import erdos_renyi_graph
from .generators import describe as describe_generator
from gnt.algorithms import collections

def generate_problem(graph, algorithm=None):
    """Generate an algorithm and describe it using text. """
    graph_description = describe_generator(graph)
    algorithm_description = describe_algorithm(algorithm)
    task = f"Given a {graph_description}, {algorithm_description}."
    answer = algorithm(graph)
    return task, answer
    
    
    