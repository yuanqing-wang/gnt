import tqdm
import networkx as nx

def get_compatible_algorithms(graph):
    """For a given graph, list all possible algorithms. """
    # get all children of nx.algorithms
    algorithms = dir(nx.algorithms)
    algorithms = [algorithm for algorithm in algorithms if not algorithm.startswith('_')]
    algorithms = [getattr(nx.algorithms, algorithm) for algorithm in algorithms]
    algorithms = [algorithm for algorithm in algorithms if callable(algorithm)]

    # filter out algorithms that are not compatible with the graph
    compatible_algorithms = []
    for algorithm in algorithms:
        try:
            result = algorithm(graph)
            if isinstance(result, str) or isinstance(result, int) or isinstance(result, float):
                compatible_algorithms.append(algorithm)
        except Exception as e:
            pass
    
    return compatible_algorithms


GRAPHS = [
    nx.complete_graph(5),
    nx.binomial_tree(5),
    nx.cycle_graph(5),
    nx.path_graph(5),
]
def get_algorithms(graphs=GRAPHS):
    algorithms = []
    for graph in tqdm.tqdm(graphs):
        algorithms += get_compatible_algorithms(graph)
    algorithms = list(set(algorithms))
    return algorithms
        
def describe(algorithm):
    return algorithm.__doc__.strip().split("\n")[0]