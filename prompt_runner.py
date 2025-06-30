import openai
import os
from prompt_templates import get_prompt

openai.api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"

def run_prompt(task, input_text, examples=None, model="gpt-3.5-turbo", temperature=0.7):
    prompt = get_prompt(task, input_text, examples)
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=512
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error running prompt: {e}")
        return None