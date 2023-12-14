import pandas as pd
import streamlit as st

# Load CompanySentimentMapping.csv
company_sentiment = pd.read_csv("./CompanySentimentMapping.csv", sep='|')

# Drop duplicate rows based on the 'Company' column
company_sentiment_cleaned = company_sentiment.drop_duplicates(subset='Company')

# Title
st.title("Company Sentiment Mapping")

# Search bar
search_text = st.text_input("Enter the company name").lower()

# Filter DataFrame based on the search text
filtered_data = company_sentiment_cleaned[company_sentiment_cleaned['Company'].str.lower().str.contains(search_text, regex=True)]

# Display the result in a dropdown
with st.expander("See Results", expanded=bool(search_text and not filtered_data.empty)):
    st.table(filtered_data)

# Display overall employee satisfaction score
st.subheader("Overall Employee Satisfaction Score")
st.bar_chart(filtered_data['SCORE'])
