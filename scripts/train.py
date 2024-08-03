from gnt.problems import generate_problem
from gnt.generators import erdos_renyi_graph
from gnt.algorithms import Diameter
from gnt.tune import tune


def run(args):
    # generate dataset 
    task, answer = zip(
        *(generate_problem(erdos_renyi_graph, Diameter, n=args.n, p=args.p) for _ in range(args.repeat))
    )
    dataset = list(zip(task, answer))
    
    # tune model
    model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    model = tune(model, dataset)
    
    
    
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=100)
    parser.add_argument('--p', type=float, default=0.1)
    parser.add_argument('--repeat', type=int, default=1000)
    
    run()