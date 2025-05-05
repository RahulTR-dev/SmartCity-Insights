# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="sshleifer/distilbart-cnn-12-6",
#     revision="a4f8f3e"
# )

# def summarize(text: str) -> str:
#     if not text.strip():
#         return "No recent news to summarize."
#     result = summarizer(text, max_length=50, min_length=20, do_sample=False)
#     return result[0]["summary_text"]
from transformers import pipeline

# Load the BART model for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str):
    # Summarize the text using the BART model
    summary = summarizer(text, max_length=350, min_length=50, do_sample=False)
    return summary[0]['summary_text']
