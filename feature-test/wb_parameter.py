import wandb
from transformers.integrations import WandbCallback

wandb.init(project="qlora-finetune")
trainer = Trainer(
  model=model,
  args=training_args,
  train_dataset=train_dataset,
  eval_dataset=eval_dataset,
  data_collator=data_collator,
  callbacks=[WandbCallback()]
)
