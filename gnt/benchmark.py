from typing import Union
import torch
from transformers import pipeline
from .utils import correct as _correct

def correct(
        model: str,
        # tokenizer: AutoTokenizer,
        task: str,
        answer: str,
):
    """Compute the accuracy of the model on a task and an answer. """
    # # Tokenize the sample string
    # tokenized_input = tokenizer(
    #     [task], return_tensors="pt", padding=False, 
    # )

    # # Generate output using the model
    # with torch.no_grad():
    #     outputs = model.generate(
    #         tokenized_input["input_ids"],
    #         max_new_tokens=500,
    #         do_sample=True,
    #         pad_token_id=tokenizer.eos_token_id
    #     )

    # # Decode the generated output
    # answer_hat = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    model = pipeline("text-generation", model, max_new_tokens=500, device="cuda:0")
    answer_hat = model(task)[0]["generated_text"]
    return _correct(answer_hat, answer)