# 🔧 LiteLLM-Finetuner

LiteLLM-Finetuner is an open-source toolkit for efficient and scalable finetuning of quantized Large Language Models (LLMs).

## 🚀 Features

- **4-bit quantization** using bitsandbytes to drastically reduce memory usage without sacrificing performance.
- **Parameter-efficient finetuning** with LoRA and PEFT, allowing low-resource customization of large models.
- **Plug-and-play integration** with Hugging Face's Transformers and Datasets libraries.
- **Scalable training** on consumer GPUs or in distributed environments.

## 📚 Use Cases

- Finetune large models on domain-specific data.
- Experiment with quantized model training on limited hardware.
- Rapid prototyping for downstream NLP tasks like text classification, generation, and Q&A.

## 🛠️ Technologies

- `QLoRA` — memory-efficient quantization and finetuning
- `bitsandbytes` — 4-bit optimizer and quantization backend
- `Hugging Face Transformers` — model and tokenizer utilities
- `PEFT` — lightweight finetuning via LoRA adapters

---

This project is part of a broader effort to **democratize access to LLM research** and make state-of-the-art language models accessible to researchers and developers with modest compute resources.
