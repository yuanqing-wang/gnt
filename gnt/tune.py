from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from torch.utils.data import DataLoader
from peft import (
    LoraConfig, 
    get_peft_model, 
)

def tune(model: str, dataset: DataLoader):
    # load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model)
    tokenizer.add_special_tokens({'sep_token': '<SEP>'})
    tokenizer.add_special_tokens({'pad_token': '<PAD>'})

    def tokenize_function(examples):
        output = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=64)
        output["labels"] = output["input_ids"]
        return output

    # get tokenized dataset
    dataset = dataset.map(tokenize_function, batched=True)

    # load the model
    model = AutoModelForCausalLM.from_pretrained(model, load_in_4bit=True)
    model = get_peft_model(model, LoraConfig())
    model.resize_token_embeddings(len(tokenizer))
    model.print_trainable_parameters()

    # define the training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        max_steps=10000,
        save_total_limit=2,
        fp16=True,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )

    trainer.train()
    return model