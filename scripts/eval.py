
def run():
    from gnt.benchmark import correct
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import Diameter
    
    g = erdos_renyi_graph(5, 0.9)
    diameter = Diameter()

    task, answer = generate_problem(g, diameter)
    is_correct = correct("meta-llama/Meta-Llama-3.1-8B-Instruct", task, answer)
    print(is_correct)
    
if __name__ == "__main__":
    run()