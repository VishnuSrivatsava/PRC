import csv
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(review):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(review)

    # The compound score is a metric that calculates the sum of all the lexicon ratings and normalizes it between -1(most extreme negative) and +1 (most extreme positive)
    return sentiment['compound']

with open('company_reviews.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    with open('company_sentiments.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Company", "Sentiment Score"])

        for row in reader:
            company_name = row[0]
            reviews = row[1].split('\n')

            sentiment_scores = [analyze_sentiment(review) for review in reviews]

            # Calculate the average sentiment score for the company
            avg_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)

            writer.writerow([company_name, avg_sentiment_score])
