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
    networkx: Callable
    complexity: Callable = lambda n, e: 0.0,
    
Diameter = partial(
    Algorithm,
    name="Diameter",
    description="the longest shortest path between any two nodes",
    networkx=nx.diameter,
)

NumberConnectedComponents = partial(
    Algorithm,
    name="NumberConnectedComponents",
    description="the number of connected components",
    networkx=nx.number_connected_components,
)

NodeConnectivity = partial(
    Algorithm,
    name="NodeConnectivity",
    description="Node connectivity is equal to the minimum number of nodes that must be removed to disconnect G or render it trivial.",
    networkx=nx.node_connectivity,
)

Transitivity = partial(
    Algorithm,
    name="Transitivity",
    description="the transitivity",
    networkx=nx.transitivity,
)
    

