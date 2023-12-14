import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load CompanySentimentMapping.csv
company_sentiment = pd.read_csv("./CompanySentimentMapping.csv", sep='|')

# Drop duplicate rows based on the 'Company' column
company_sentiment_cleaned = company_sentiment.drop_duplicates(subset='Company')

def search_company():
    search_text = search_var.get().lower()
    
    # Filter DataFrame based on the search text
    filtered_data = company_sentiment_cleaned[company_sentiment_cleaned['Company'].str.lower().str.contains(search_text, regex=True)]

    # Display the result in the treeview
    display_result(filtered_data)

def display_result(data):
    tree.delete(*tree.get_children())  # Clear previous results

    for index, row in data.iterrows():
        tree.insert('', 'end', values=(row['Company'], row['SCORE'], row['SENTIMENT_LABEL']))

# Create main window
root = tk.Tk()
root.title("Company Sentiment Mapping")

# Create search bar
search_var = tk.StringVar()
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.grid(row=0, column=0, padx=10, pady=10)

# Create search button
search_button = ttk.Button(root, text="Search", command=search_company)
search_button.grid(row=0, column=1, padx=10, pady=10)

# Create treeview to display results
tree = ttk.Treeview(root, columns=('Company', 'SCORE', 'SENTIMENT_LABEL'), show='headings')
tree.heading('Company', text='Company')
tree.heading('SCORE', text='Score')
tree.heading('SENTIMENT_LABEL', text='Sentiment Label')
tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Bind Enter key to search function
root.bind('<Return>', lambda event=None: search_company())

# Start the GUI
root.mainloop()
