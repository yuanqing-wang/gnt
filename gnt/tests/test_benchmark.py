def test_correct():
    from gnt.benchmark import correct
    from vllm import LLM
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import Diameter
    
    g = erdos_renyi_graph(5, 0.5)
    diameter = Diameter()

    task, answer = generate_problem(g, diameter)
    
    model = LLM("meta-llama/Meta-Llama-3-70B-Instruct")
    is_correct = correct(model, task, answer)
    print(is_correct)
    