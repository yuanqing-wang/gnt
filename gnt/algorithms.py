import abc
from dataclasses import dataclass
from typing import Callable
from functools import partial
import networkx as nx

@dataclass
class Algorithm:
    """Base class for all algorithms.
    """
    name: str
    description: str
    implementation: Callable
    complexity: Callable = lambda n, e: 0.0,
    
Diameter = partial(
    Algorithm,
    name="diameter",
    description="the longest shortest path between any two nodes",
    implementation=nx.diameter,
)

NumberConnectedComponents = partial(
    Algorithm,
    name="number of connected components",
    description="the number of connected components",
    implementation=nx.number_connected_components,
)

NodeConnectivity = partial(
    Algorithm,
    name="NodeConnectivity",
    description="Node connectivity is equal to the minimum number of nodes that must be removed to disconnect G or render it trivial.",
    implementation=nx.node_connectivity,
)

Transitivity = partial(
    Algorithm,
    name="Transitivity",
    description="the transitivity",
    implementation=nx.transitivity,
)
    

