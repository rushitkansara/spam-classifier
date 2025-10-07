# Email Spam Classifier

A machine learning project that classifies emails as **Spam** or **Not Spam** using Natural Language Processing and a Naive Bayes model.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Dataset Source](#dataset-source)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

---

## Features

- Text preprocessing including lowercasing, punctuation removal, and stemming.
- TF-IDF vectorization to convert text data into a numerical format.
- A Multinomial Naive Bayes model for classification.
- Achieves an accuracy of approximately 95% on the test dataset.
- A user-friendly web interface built with Streamlit.

---

## Tech Stack

- Python
- scikit-learn
- pandas
- NLTK
- Streamlit

---

## Project Structure

```
spam-classifier/
├── .gitignore
├── app.py
├── data/
│   └── spam.csv
├── model.pkl
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── spam_classifier.ipynb
└── utils.py
```

---

## Setup and Installation

There are two ways to set up and run this project:

### 1. For Development and Experimentation (using the Jupyter Notebook)

**Step 1: Clone the repository**
```bash
git clone https://github.com/Rushitkansara/emailSpamClassifier.git
cd emailSpamClassifier
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements-dev.txt
```

**Step 3: Run the Notebook**
```bash
jupyter notebook spam_classifier.ipynb
```
This will open the notebook in your browser, allowing you to run the cells, see the model training and evaluation process, and generate the `model.pkl` file.

### 2. For Demonstration (using the Streamlit App)

**Step 1: Clone the repository**
```bash
git clone https://github.com/Rushitkansara/emailSpamClassifier.git
cd emailSpamClassifier
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Run the App**
```bash
streamlit run app.py
```
On the first run, the app will automatically train the model and save it as `model.pkl`. Subsequent runs will load the pre-trained model for faster startup.

---

## Usage

Once the Streamlit app is running, you can enter a message into the text area and click the "Predict" button to see the classification.

---

## Sample Output

- **Input:** "Congratulations, you won!"
- **Prediction:** Spam

- **Input:** "Team meeting at 3 PM"
- **Prediction:** Not Spam

---

## Dataset Source

The dataset used for training and evaluation is the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) from Kaggle.

---

## Future Enhancements

- **Implement a Deep Learning Model:** Explore using models like BERT or LSTMs for potentially higher accuracy.
- **Improve the User Interface:** Enhance the web interface for a better user experience on both mobile and web platforms.
- **Deploy as a REST API:** Create a RESTful API to serve the model, allowing for easier integration with other applications.
- **Create a Separate Training Script:** Decouple the model training process from the main application for better modularity.

---

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Authors

- Rushit Kansara - [https://github.com/Rushitkansara](https://github.com/Rushitkansara)
- ChatGPT - [https://chatgpt.com](https://chatgpt.com)
- Gemini CLI

---
