from typing import Union
import torch
from functools import lru_cache
from transformers import pipeline
from .utils import correct as _correct
from vllm import LLM, SamplingParams

@lru_cache(maxsize=1)
def get_model(model):
    # return pipeline("text-generation", model=model, max_new_tokens=100, device="cuda:0", num_return_sequences=1,)
    llm = LLM(model)
    params = SamplingParams(max_tokens=100)
    model = lambda x: llm.generate(x, params)
    return model

def correct(
        model: str,
        task: str,
        answer: str,
):
    """Compute the accuracy of the model on a task and an answer. """
    model = get_model(model)
    answer_hat = model(task)[0]
    return _correct(answer_hat, answer)