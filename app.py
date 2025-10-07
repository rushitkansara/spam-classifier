import streamlit as st
import pickle
import os
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from utils import clean_text

MODEL_PATH = 'model.pkl'

# Function to train and save the model
def train_and_save_model():
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

    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    
    return model

# Load the model
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    model = train_and_save_model()

# Streamlit UI
st.title("📧 Spam Classifier")

user_input = st.text_area("Enter a message:")
if st.button("Predict"):
    cleaned_input = clean_text(user_input)
    prediction = model.predict([cleaned_input])
    st.write(f"Prediction: **{prediction[0]}**")
