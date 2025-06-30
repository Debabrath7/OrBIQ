
import streamlit as st
from prompt_runner import run_prompt
from prompt_evaluator import evaluate_qa, evaluate_summarization, evaluate_ner
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="OrbIQ Prompt Playground", layout="wide")

st.title("🤖 OrbIQ – Prompt Engineering Sandbox")

task = st.selectbox("Choose a Task", ["QA (Few-shot)", "Summarization", "NER"])

input_text = st.text_area("Enter your input text here:", height=150)

examples = [
    {"question": "Who wrote Hamlet?", "answer": "William Shakespeare"},
    {"question": "What is the capital of France?", "answer": "Paris"}
]

if st.button("Run Prompt"):
    if task == "QA (Few-shot)":
        output = run_prompt("qa_few_shot", input_text, examples)
        st.subheader("LLM Answer")
        st.write(output)
    elif task == "Summarization":
        output = run_prompt("summarization_instruction", input_text)
        st.subheader("LLM Summary")
        st.write(output)
    elif task == "NER":
        output = run_prompt("ner_prompt", input_text)
        st.subheader("LLM Output")
        st.text(output)
    else:
        st.warning("Unsupported task")

    st.success("Done!")
