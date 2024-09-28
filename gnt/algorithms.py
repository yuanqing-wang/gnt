import abc
from dataclasses import dataclass
from typing import Callable, Any
from functools import partial
import networkx as nx

class _AsStr:
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self, x):
        x = self.fn(x)
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
        if not isinstance(self.implementation, _AsStr):
            self.implementation = _AsStr(self.implementation)
    
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
    name="node connectivity",
    description="the minimum number of nodes that must be removed to disconnect G or render it trivial.",
    implementation=nx.node_connectivity,
)

Transitivity = partial(
    Algorithm,
    name="Transitivity",
    description="the probability that the adjacent vertices of a vertex are connected",
    implementation=nx.transitivity,
)
    
AverageDegree = partial(
    Algorithm,
    name="average degree",
    description="the number of edges over the number of nodes",
    implementation=lambda g: g.number_of_edges() / g.number_of_nodes(),
)


def _largest_cycle(g):
    cycles = sorted(list(nx.simple_cycles(g)), key = lambda s: len(s))
    if len(cycles) == 0:
        return 0
    return len(cycles[-1])
    

LargestCycle = partial(
    Algorithm,
    name="largest cycle",
    description="the length of the longest cycle in the graph",
    implementation=lambda g: _largest_cycle(g),
)

