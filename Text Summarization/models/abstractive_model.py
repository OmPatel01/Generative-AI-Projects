from transformers import pipeline

# Load the model once (so it's reused across calls)
abstractive_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_abstractive_summary(text, min_length=50, max_length=500):
    """
    Generates an abstractive summary using BART.

    Args:
        text (str): Input text to summarize.
        min_length (int): Minimum length of summary.
        max_length (int): Maximum length of summary.

    Returns:
        str: Abstractive summary.
    """
    if not text or len(text.strip()) == 0:
        return "⚠️ Empty input provided."

    try:
        summary = abstractive_summarizer(
            text,
            min_length=min_length,
            max_length=max_length,
            do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        return f"❌ Error generating summary: {e}"