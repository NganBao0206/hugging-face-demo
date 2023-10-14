from transformers import pipeline

# Khởi tạo pipeline đánh giá cảm xúc
sentiment_pipeline = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")

def analyze_sentiment(text):
    # Đánh giá cảm xúc của văn bản
    return sentiment_pipeline(text)
