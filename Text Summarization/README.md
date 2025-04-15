# GenAI Text Summarization Project

## 📝 Project Description

This project demonstrates both **Abstractive** and **Extractive** text summarization techniques using state-of-the-art transformer models. Built using Python and Hugging Face Transformers, the goal is to provide concise summaries of longer textual content for applications like content generation, article compression, or information retrieval.

It supports:  
- **Abstractive Summarization** using `facebook/bart-large-cnn`, which generates human-like summaries.  
- **Extractive Summarization** using the `sentence-transformers/all-MiniLM-L6-v2` model and cosine similarity, which selects the most important sentences from the text.

---

## 🧠 Features

- 🔍 Dual approach: **Abstractive + Extractive** summarization  
- ⚡ Built on top of **Hugging Face Transformers** and **PyTorch**  
- 🧪 Handles small to moderately large text inputs effectively  
- 🌐 Scalable to web or app deployment via Streamlit or Flask  
- 🧠 Utilizes sentence embeddings and cosine similarity for extractive summaries
- 🗃️ Document uploads (PDFs, .txt) for summarization

---

## 🧰 Libraries and Tech Stack

- Transformers – for model pipelines  
- PyTorch – as backend for transformer models  
- Scikit-learn – for cosine similarity  
- NLTK – for sentence tokenization  
- NumPy – for vector operations  
- Sentence-Transformers – for MiniLM-based embeddings  

---

## 🧪 Model Details

### 🔹 Abstractive Summarization

The abstractive model used is `facebook/bart-large-cnn`, which leverages natural language generation to create fluent and semantically rich summaries that do not simply extract from the original text but rather generate a new version conveying the same meaning.

### 🔸 Extractive Summarization

The extractive summarizer uses `sentence-transformers/all-MiniLM-L6-v2` to embed sentences and then selects the most relevant ones using cosine similarity. It performs well on short to medium-length inputs.  
**Note:** On longer text documents, extractive summarization may fail due to **index out-of-range** issues caused by transformer input size limitations.

---

## 📌 Use Cases

- 📰 News summarization  
- 📚 Academic research briefs  
- 📄 Legal document summarization  
- 📱 Content previews in applications  
- ✍️ Assisting content creators with concise drafts  

---

## 💡 Future Enhancements

- ✅ Add support for long document chunking in extractive summarization  
- 🚀 Integrate a Streamlit interface for user-friendly interaction  
- 🧠 Introduce fine-tuned models for domain-specific summarization (e.g., healthcare, finance)  
- 📊 Add evaluation metrics (e.g., ROUGE, BLEU)    

