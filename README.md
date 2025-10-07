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

- spam-classifier/
- |
- |––– spam_classifier.ipynb   # Jupyter notebook for training and evaluation
- |––– app.py                  # Interface (Streamlit)
- |––– utils.py                # Utility functions
- |––– requirements.txt        # Core dependencies
- |––– requirements-dev.txt    # Development dependencies
- |––– model.pkl               # Pre-trained model
- |––– data/                   # Dataset from Kaggle
- |––– .gitignore
- |––– README.md               # You're reading it!

---

## How to Run

There are two ways to run this project:

### 1. Using the Jupyter Notebook (for development and experimentation)

**Step 1: Install Dependencies**
```bash
pip install -r requirements-dev.txt
```

**Step 2: Run the Notebook**
```bash
jupyter notebook spam_classifier.ipynb
```
This will open the notebook in your browser. You can run the cells to see the model training and evaluation process. The notebook will also save the trained model as `model.pkl`.

### 2. Using the Streamlit App (for demonstration)

**Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Run the App**
```bash
streamlit run app.py
```
On the first run, the app will train the model and save it as `model.pkl`. On subsequent runs, it will load the pre-trained model.

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
- Create a separate training script

---

## Authors

- Rushit Kansara   - https://github.com/Rushitkansara
- ChatGPT          - https://chatgpt.com

---
