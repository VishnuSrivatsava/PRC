import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import statistics

nltk.download('stopwords')

# Load the CSV file
data = pd.read_csv('./company_reviews.csv', sep=',')
data.Reviews = data.Reviews.astype(str)

# Transform text to lowercase
data['Reviews'] = data['Reviews'].apply(lambda x: x.lower())

# Removing all punctuations and special characters
data['Reviews'] = data['Reviews'].apply(lambda x: re.sub('[,.]', '', x))

# Remove stopwords
stopwords_list = stopwords.words('english')
data['Reviews'] = data['Reviews'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords_list)]))

# Sentiment analysis with TextBlob
score_list = [TextBlob(text).sentiment.polarity for text in data['Reviews']]
median = statistics.median(score_list)

# Classify sentiment based on median score
sentiment_label = ['positive' if score > median else 'negative' if score < median else 'neutral' for score in score_list]

# Add sentiment scores and labels to the dataset
data['SCORE'] = score_list
data['SENTIMENT_LABEL'] = sentiment_label

# Save the results to a new CSV file
data.to_csv("./TextBlobResultswithMedian.csv", sep='|', index=False)

# Create a new DataFrame with Company names and Scores
company_sentiment = pd.DataFrame({'Company': data['Company'], 'SCORE': data['SCORE'], 'SENTIMENT_LABEL': data['SENTIMENT_LABEL']})

# Save the mapping to a new CSV file
company_sentiment.to_csv("./CompanySentimentMapping.csv", sep='|', index=False)

# Display the mapping DataFrame
print(company_sentiment)
