from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
import torch

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load MiniLM model & tokenizer
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def sentence_embedding(sentence):
    """Generates embedding for a single sentence using MiniLM."""
    inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def generate_extractive_summary(text, num_sentences=3):
    """
    Generates an extractive summary using MiniLM sentence embeddings.

    Args:
        text (str): Input text to summarize.
        num_sentences (int): Number of key sentences to return.

    Returns:
        str: Extractive summary.
    """
    if not text or len(text.strip()) == 0:
        return "⚠️ Empty input provided."

    try:
        sentences = sent_tokenize(text)
        if len(sentences) <= num_sentences:
            return " ".join(sentences)

        # Get sentence embeddings
        embeddings = np.array([sentence_embedding(sent) for sent in sentences])

        # Compute similarity to the overall document
        doc_embedding = embeddings.mean(axis=0)
        similarities = cosine_similarity([doc_embedding], embeddings)[0]

        # Select top N sentences
        top_indices = similarities.argsort()[-num_sentences:][::-1]
        top_sentences = [sentences[i] for i in sorted(top_indices)]

        return " ".join(top_sentences)

    except Exception as e:
        return f"❌ Error generating extrasctive summary: {e}"