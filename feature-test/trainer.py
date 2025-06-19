from transformers import EarlyStoppingCallback

trainer = Trainer(
  model=model,
  args=training_args,
  train_dataset=train_dataset,
  eval_dataset=eval_dataset,
  data_collator=data_collator,
  callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)
