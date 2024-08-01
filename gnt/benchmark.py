from vllm import LLM
from .utils import correct as _correct

def correct(
        model: LLM,
        task: str,
        answer: str,
):
    """Compute the accuracy of the model on a task and an answer. """
    output = model.generate(task)[0]
    return _correct(output, answer)
    
    
    
    
    