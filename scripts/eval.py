import numpy as np

def run():
    from gnt.benchmark import correct
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import AverageDegree
    
    MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    for n in range(2, 100):
        for p in np.linspace(0, 1, 10):
            g = erdos_renyi_graph(n, p)
            task, answer = generate_problem(g, AverageDegree())
            is_correct = correct(MODEL, task, answer)
            print(is_correct)
    
if __name__ == "__main__":
    run()