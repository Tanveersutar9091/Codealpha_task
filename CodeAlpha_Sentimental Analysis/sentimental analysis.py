import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Sample Data: Simulating scraped Amazon/Product reviews
data = {
    'Review': [
        "I absolutely love this product! It works perfectly.",
        "The item arrived broken and customer service was terrible.",
        "It's okay, does the job but nothing special.",
        "Fantastic quality, highly recommend to everyone!",
        "Poor design and very difficult to use. Disappointed.",
        "Average experience. It's fine for the price.",
        "Best purchase I've made this year! Simply amazing.",
        "Worst experience ever. The product stopped working after one day."
    ]
}

df = pd.DataFrame(data)

# 2. NLP Technique: Sentiment Classification
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Polarity is a float between -1 (negative) and 1 (positive)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply the analysis
df['Sentiment'] = df['Review'].apply(analyze_sentiment)
df['Polarity'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# 3. Visualization: Understanding Public Opinion
plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment', data=df, palette={'Positive': 'green', 'Negative': 'red', 'Neutral': 'gray'})
plt.title('Public Opinion Trend: Product Sentiment Analysis', fontsize=14)
plt.show()

# 4. Result for Marketing/Product Development
print("--- Business Insights ---")
pos_percent = (len(df[df['Sentiment'] == 'Positive']) / len(df)) * 100
print(f"Customer Satisfaction Rate: {pos_percent}%")
print("Recommendation: Focus marketing on 'Ease of Use' (Positive) and investigate 'Durability' issues (Negative).")

# Save for GitHub
df.to_csv('sentiment_results.csv', index=False)