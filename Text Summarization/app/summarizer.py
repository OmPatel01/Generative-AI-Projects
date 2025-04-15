import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.abstractive_model import generate_abstractive_summary
from models.extractive_model import generate_extractive_summary

def summarize_text(text, method="both", num_sentences=3):
    """
    Runs summarization using the selected method(s).

    Args:
        text (str): Input text to summarize.
        method (str): "abstractive", "extractive", or "both"
        num_sentences (int): Number of extractive summary sentences.

    Returns:
        dict: Contains one or both summaries.
    """
    summaries = {}

    if method in ["abstractive", "both"]:
        summaries["abstractive"] = generate_abstractive_summary(text)

    if method in ["extractive", "both"]:
        summaries["extractive"] = generate_extractive_summary(text, num_sentences=num_sentences)

    return summaries
