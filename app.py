import streamlit as st
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

import pandas as pd
import re
import string

# Cleaning function
def clean_text(msg):
    msg = msg.lower()
    msg = re.sub(r'\d+', '', msg)
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    return msg.strip()

# Load & train model
df = pd.read_csv('data/spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['cleaned'] = df['message'].apply(clean_text)

X = df['cleaned']
y = df['label']

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])
model.fit(X, y)

# Streamlit UI
st.title("📧 Spam Classifier")

user_input = st.text_area("Enter a message:")
if st.button("Predict"):
    prediction = model.predict([user_input])
    st.write(f"Prediction: **{prediction[0]}**")
