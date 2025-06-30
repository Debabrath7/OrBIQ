# prompt_templates.py

def get_prompt(task, input_text, examples=None):
    if task == "qa_zero_shot":
        return f"Answer the following question as accurately as possible:\n\nQuestion: {input_text}"
    elif task == "qa_few_shot":
        few_shot = "\n".join([f"Q: {ex['question']}\nA: {ex['answer']}" for ex in examples])
        return f"{few_shot}\nQ: {input_text}\nA:"
    elif task == "qa_chain_of_thought":
        return f"Answer the following question step by step.\n\nQuestion: {input_text}\nLet’s think step by step:"
    elif task == "summarization_instruction":
        return f"Summarize the following article in 1-2 sentences:\n\n{input_text}"
    elif task == "summarization_style":
        return f"Summarize the text below for a high school student:\n\n{input_text}"
    elif task == "ner_prompt":
        return f"""Extract named entities from the following sentence and label them as PERSON, ORGANIZATION, LOCATION, or MISC.\n\nText: "{input_text}"\nFormat: Entity - Label\n"""
    else:
        raise ValueError(f"Unknown task: {task}")