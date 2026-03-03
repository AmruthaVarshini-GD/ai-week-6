import torch
from transformers import pipeline

def load_model():
    generator = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )
    return generator


def generate_response(generator, prompt, max_tokens=150, temperature=0.2):
    chat_prompt = f"""<|system|>
You are a professional customer support AI.
</s>
<|user|>
{prompt}
</s>
<|assistant|>
"""

    outputs = generator(
        chat_prompt,
        max_new_tokens=max_tokens,
        temperature=temperature,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True,
        return_full_text=False
    )

    return outputs[0]["generated_text"].strip()
