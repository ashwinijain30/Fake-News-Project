# 📰 Fake News Detection System

A **Machine Learning-based Fake News Detection System** that classifies news articles as **Fake News** or **Real News** using Natural Language Processing (NLP) and a Logistic Regression model. The project provides an interactive **Streamlit web application** where users can enter a news article and get an instant prediction.

## 🚀 Live Demo

🔗 **Streamlit App:**
[https://fake-news-detection-system-ashwini.streamlit.app/](https://fake-news-detection-system-ashwini.streamlit.app/)

## 📌 Features

* Detects whether a news article is **Fake** or **Real**
* Text preprocessing and cleaning
* TF-IDF-based text feature extraction
* Logistic Regression classification
* Decision Tree model for comparison
* Interactive Streamlit interface
* Real-time prediction for user-provided news
* Deployed using Streamlit Community Cloud

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **TF-IDF Vectorization**
* **Logistic Regression**
* **Decision Tree Classifier**
* **Streamlit**
* **Git & GitHub**

## 📂 Project Structure

```text
Fake-News-Project/
│
├── app.py
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ How It Works

```text
News Article
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Machine Learning Model
     ↓
Prediction
     ↓
Fake News / Real News
```

### 1. Text Preprocessing

The input news is cleaned by:

* Converting text to lowercase
* Removing URLs
* Removing HTML tags
* Removing punctuation
* Removing unnecessary characters and numbers

### 2. TF-IDF Vectorization

**TF-IDF (Term Frequency–Inverse Document Frequency)** converts the cleaned news text into numerical features that can be processed by the machine learning model.

### 3. Model Prediction

The trained **Logistic Regression** model uses the TF-IDF features to classify the article as:

* `0 → Fake News`
* `1 → Real News`

A **Decision Tree Classifier** was also trained and evaluated for comparison.

## 📊 Dataset

The project uses separate datasets containing:

* **Fake news articles**
* **Real news articles**

The datasets are labeled before being combined and used for model training and testing.

## 💻 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/ashwinijain30/Fake-News-Project.git
```

Move into the project directory:

```bash
cd Fake-News-Project
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🖥️ Usage

1. Open the Fake News Detection application.
2. Enter or paste a news article.
3. Click **Detect News**.
4. The application displays the predicted result:

```text
✅ Real News
```

or

```text
❌ Fake News
```

## 📈 Machine Learning Models

| Model               | Purpose                   |
| ------------------- | ------------------------- |
| Logistic Regression | Main classification model |
| Decision Tree       | Model comparison          |
| TF-IDF              | Text feature extraction   |

## ⚠️ Disclaimer

This system predicts whether news is likely to be fake or real based on patterns learned from the training dataset. **It is not a replacement for professional fact-checking or verification from reliable sources.**

## 👩‍💻 Author

**Ashwini Jain**

* GitHub: [https://github.com/ashwinijain30](https://github.com/ashwinijain30)

## ⭐ Future Improvements

* Add more diverse and up-to-date datasets
* Add additional machine learning and deep learning models
* Display prediction confidence
* Integrate external fact-checking APIs
* Improve the user interface
* Support multiple languages
* Add explainable AI features to show why an article was classified as fake or real
