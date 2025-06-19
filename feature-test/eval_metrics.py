from transformers import TrainerCallback

class GenerationCallback(TrainerCallback):
    def on_epoch_end(self, args, state, control, **kwargs):
        sample = "Your prompt here"
        gen = model.generate(**tokenizer(sample, return_tensors="pt"))
        text = tokenizer.decode(gen[0], skip_special_tokens=True)
        # compute ROUGE/perplexity here, then log to W&B or stdout
        print(f"\n>>> Generated sample: {text}\n")
