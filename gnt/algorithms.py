import abc
from dataclasses import dataclass
from typing import Callable, Any
from functools import partial
import networkx as nx

def _as_str(x: Any):
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float):
        return f"{x:.2f}"
    return x

@dataclass
class Algorithm:
    """Base class for all algorithms.
    """
    name: str
    description: str
    implementation: Callable
    complexity: Callable = lambda n, e: 0.0,
    
    def __post_init__(self):
        self.implementation = lambda g: _as_str(self.implementation(g))
    
Diameter = partial(
    Algorithm,
    name="diameter",
    description="the length of the longest shortest path between any two nodes",
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
    
AverageDegree = partial(
    Algorithm,
    name="average degree",
    description="the average degree, the number of edges over the number of nodes",
    implementation=lambda g: g.number_of_edges() / g.number_of_nodes(),
)

