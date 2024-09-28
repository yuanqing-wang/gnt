import numpy as np
import pandas as pd
import networkx as nx

def run():
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt import algorithms
    
    df = pd.DataFrame(columns=["problem", "n", "p", "task", "answer"])
    for problem in ["AverageDegree", "NodeConnectivity", "Transitivity", "Diameter"]:
        for n in range(20, 30):
            for p in np.linspace(0, 1, 11):
                if p == 0:
                    continue
                for repeat in range(3):
                    g = erdos_renyi_graph(n, p)
                    if not nx.is_connected(g):
                        continue
                    task, answer = generate_problem(g, getattr(algorithms, problem)())
                    print(task, answer)
                    df.loc[len(df)] = [problem, n, p, task, answer]
    df.to_csv("tasks.csv", index=False)
            
    
    
if __name__ == "__main__":
    import sys
    run()