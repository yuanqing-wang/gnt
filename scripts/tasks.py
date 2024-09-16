import numpy as np
import pandas as pd

def run(problem):
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt import algorithms
    
    df = pd.DataFrame(columns=["n", "p", "task", "answer"])
    for n in range(5, 16):
        for p in np.linspace(0, 1, 11):
            if p == 0:
                continue
            accurate = []
            for repeat in range(5):
                g = erdos_renyi_graph(n, p)
                task, answer = generate_problem(g, getattr(algorithms, problem)())
                print(task, answer)
                df.loc[len(df)] = [n, p, task, answer]
    df.to_csv(f"{problem}.csv", index=False)
            
    
    
if __name__ == "__main__":
    import sys
    run(sys.argv[1])