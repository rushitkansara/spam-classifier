# Email Spam Classifier

A machine learning-based project that classifies emails as **Spam** or **Not Spam** using NLP and a Naive Bayes model.

---

## Features

- Preprocessing: punctuation removal, stemming, lowercasing
- TF-IDF vectorization of email text
- Multinomial Naive Bayes model
- Accuracy: ~98% on test data
- Streamlit app interface via `app.py`

---

## Tech Stack

- Python
- scikit-learn
- pandas
- NLTK
- Streamlit (optional interface)

---

## Project Structure

- emailSpamClassifier/
- |
- |––– spam_classifier.ipynb   #Jupyter notebook for training and evaluation
- |––– app.py                  #Interface (Streamlit)
- |––– requirements.txt        #Dependency list
- |––– data/                   #Dataset from kaggle
- |––– .gitignore
- |––– README.md               #You're reading it!

---

## How to Run

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train Model

```bash
jupyter notebook spam_classifier.ipynb
```

### Step 3: Run App

```bash
streamlit run app.py
```

---

## Sample Output

- Email                         |  Prediction
- "Congratulations, you won!"   |  Spam
- "Team meeting at 3 PM"        |  Not Spam

---

## Dataset Source

Kaggle dataset - https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

---

## Future Enhancements

- Deep learning variant (BERT or LSTM)
- Improved UI for mobile/web
- Deploy as REST API

---

## Authors

- Rushit Kansara   - https://github.com/Rushitkansara
- ChatGPT          - https://chatgpt.com

---
