import numpy as np

def run():
    from gnt.benchmark import correct
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import AverageDegree, NodeConnectivity, Transitivity
    
    
    MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct"

    import pandas as pd
    df = pd.DataFrame(columns=["n", "p", "algorithm", "is_correct"])
    algorithm = "NodeConnectivity"
    for n in range(5, 16):
        for p in np.linspace(0, 1, 11):
            accurate = []
            for repeat in range(5):
                g = erdos_renyi_graph(n, p)
                task, answer = generate_problem(g, locals()[algorithm]())
                _, is_correct = correct(MODEL, task, answer)
                accurate.append(is_correct)
            accurate = np.array(accurate)
            is_correct = np.mean(accurate)
            df = df._append(dict(n=n, p=p, algorithm=algorithm, is_correct=is_correct), ignore_index=True)
                    
    import pandas as pd
    df.to_csv("results.csv")
            
    
    
if __name__ == "__main__":
    run()