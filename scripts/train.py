from gnt.problems import generate_problem
from gnt.generators import erdos_renyi_graph
from gnt.algorithms import AverageDegree
from gnt.tune import tune
from datasets import Dataset
import wandb
wandb.login(key="58466296c2de2fdd61d262115503afdf302441b7")

def run(args):
    # generate dataset 
    task, answer = zip(
        *(
            generate_problem(
                erdos_renyi_graph(n=args.n, p=args.p),
                AverageDegree(),
            ) for _ in range(args.repeat))
    )
    
    dataset = [
        {
            "text": task + f" [{answer}]"
        }
        for task, answer in zip(task, answer)
    ]
    
    # convert list to dataset
    dataset = Dataset.from_list(dataset)
    
    # inspect the length of each item in the dataset
    # tune model
    model = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    # model = "TinyLlama/TinyLlama_v1.1"
    model = tune(model, dataset)
    
    
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=5)
    parser.add_argument('--p', type=float, default=0.1)
    parser.add_argument('--repeat', type=int, default=20)
    args = parser.parse_args()
    run(args)