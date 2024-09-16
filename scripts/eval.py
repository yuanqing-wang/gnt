import numpy as np

def run():
    from gnt.benchmark import correct
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import AverageDegree, NodeConnectivity
    
    
    MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"

    import pandas as pd
    df = pd.DataFrame(columns=["n", "p", "task", "reference", "answer", "is_correct"])
    for n in range(5, 16):
        for p in np.linspace(0, 1, 11):
            accurate = []
            for repeat in range(5):
                g = erdos_renyi_graph(n, p)
                task, answer = generate_problem(g, NodeConnectivity())
                answer_hat, is_correct = correct(MODEL, task, answer)
                # df.iloc[len(df)] = [n, p, task, answer, answer_hat]
                task = task.replace("\n", " ")
                answer = answer.replace("\n", " ")
                answer_hat = answer_hat.replace("\n", " ")
                df = df._append(dict(n=n, p=p, task=task, reference=answer, answer=answer_hat), ignore_index=True)
                    
                                
            
    import pandas as pd
    df.to_csv("connectivity.csv")
            
    
    
if __name__ == "__main__":
    run()