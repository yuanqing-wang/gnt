def test_correct():
    from gnt.benchmark import correct
    from gnt.problems import generate_problem
    from gnt.generators import erdos_renyi_graph
    from gnt.algorithms import Diameter
    
    g = erdos_renyi_graph(5, 0.9)
    diameter = Diameter()

    task, answer = generate_problem(g, diameter)
    
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
    tokenizer.pad_token = tokenizer.eos_token
    
    is_correct = correct(model, tokenizer, task, answer)
    print(is_correct)
    