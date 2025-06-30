from sklearn.metrics import precision_score, recall_score, f1_score
import nltk
import difflib
from rouge_score import rouge_scorer
import re

nltk.download('punkt')

def evaluate_qa(predicted, ground_truth):
    predicted = predicted.strip().lower()
    ground_truth = ground_truth.strip().lower()
    ratio = difflib.SequenceMatcher(None, predicted, ground_truth).ratio()
    return round(ratio, 3)

def evaluate_summarization(predicted, reference):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, predicted)
    return {
        'ROUGE-1': round(scores['rouge1'].fmeasure, 3),
        'ROUGE-L': round(scores['rougeL'].fmeasure, 3)
    }

def evaluate_ner(predicted_text, gold_entities):
    pred = extract_ner_pairs(predicted_text)
    pred_labels = [label for _, label in pred]
    true_labels = [label for _, label in gold_entities]
    common = set(pred_labels) & set(true_labels)
    correct = len(common)
    total_pred = len(pred_labels)
    total_true = len(true_labels)
    precision = correct / total_pred if total_pred else 0
    recall = correct / total_true if total_true else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0
    return {
        'Precision': round(precision, 3),
        'Recall': round(recall, 3),
        'F1 Score': round(f1, 3)
    }

def extract_ner_pairs(text):
    lines = text.strip().split('\n')
    pairs = []
    for line in lines:
        match = re.match(r'(.+?)\s*-\s*(PERSON|ORG|LOCATION|MISC)', line.strip(), re.IGNORECASE)
        if match:
            entity, label = match.groups()
            pairs.append((entity.strip(), label.upper()))
    return pairs