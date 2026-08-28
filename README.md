# 📰 Fake News Detection System

A Machine Learning-based Fake News Detection System that classifies news articles as **Fake News** or **Real News** using **Natural Language Processing (NLP)** and **Logistic Regression**.

The project provides an interactive **Streamlit web application** where users can enter a news article and get an instant prediction.

---

## 🚀 Live Demo

🔗 Streamlit App: https://fake-news-detection-system-ashwini.streamlit.app/

---

## 📌 Features

- Detects whether a news article is Fake or Real
- Text preprocessing and cleaning
- TF-IDF-based text feature extraction
- Logistic Regression classification
- Interactive Streamlit interface
- Real-time prediction for user-provided news
- Deployed using Streamlit Community Cloud

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Pickle
- Git & GitHub

---

## ⚙️ How It Works

The system follows these steps:

```text
News Article
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression Model
     ↓
Prediction
     ↓
Fake News / Real News
1. Text Preprocessing

The input news article is cleaned before prediction.

The preprocessing includes:

Converting text to lowercase
Removing URLs
Removing HTML tags
Removing punctuation
Removing unnecessary characters
Removing unwanted text patterns
2. TF-IDF Vectorization

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts the cleaned text into numerical features that can be processed by the Machine Learning model.

The trained TF-IDF vectorizer is saved as:

tfidf_vectorizer.pkl
3. Logistic Regression

The project uses Logistic Regression as the main Machine Learning classification model.

The trained model is saved as:

fake_news_model.pkl

The model predicts:

0 → Fake News
1 → Real News
🤖 Machine Learning Model
Logistic Regression

Logistic Regression is used because this is a binary classification problem.

There are two possible classes:

Fake News
Real News

The trained Logistic Regression model receives the TF-IDF numerical features and predicts the class of the news article.

📂 Project Structure
Fake_News_Detection/
│
├── app.py
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── .gitignore
File Description
File	Description
app.py	Streamlit application
fake_news_model.pkl	Trained Logistic Regression model
tfidf_vectorizer.pkl	Trained TF-IDF vectorizer
requirements.txt	Required Python libraries
.gitignore	Files excluded from Git
💻 Installation and Setup
1. Clone the Repository
git clone https://github.com/ashwinijain30/Fake-News-Project.git
2. Move into the Project Directory
cd Fake-News-Project
3. Install Required Libraries
pip install -r requirements.txt
4. Run the Streamlit Application
streamlit run app.py

The application will open in your web browser.

🖥️ Usage
Open the Fake News Detection application.
Enter or paste a news article into the text box.
Click the Detect News button.
The application processes the news article.
The trained Logistic Regression model makes the prediction.
The result is displayed as:
✅ Real News

or

❌ Fake News
🔄 Prediction Process
User enters news
       ↓
Text is cleaned
       ↓
TF-IDF converts text into numerical features
       ↓
Logistic Regression model
       ↓
Prediction
       ↓
0 = Fake News
1 = Real News
🌐 Deployment

The application is deployed using Streamlit Community Cloud.

The trained model and TF-IDF vectorizer are loaded from their respective .pkl files when the application starts.

This allows the application to make predictions without retraining the model every time.

🎯 Objective

The main objective of this project is to demonstrate how Natural Language Processing and Machine Learning can be used to classify news articles based on textual patterns.

📚 Learning Outcomes

Through this project, we gained practical knowledge of:

Python programming
Data preprocessing
Natural Language Processing
TF-IDF feature extraction
Machine Learning classification
Logistic Regression
Model saving and loading using Pickle
Streamlit application development
Git and GitHub
Machine Learning model deployment
⚠️ Limitations

The system classifies news based on patterns learned from the training data.

It does not independently verify the factual accuracy of a news claim or check external sources.

Therefore, the prediction should be considered a Machine Learning-based classification rather than a definitive fact check.

🔮 Future Improvements

Possible future improvements include:

Using a larger and more diverse dataset
Trying advanced NLP models such as BERT
Improving text preprocessing
Adding source verification
Adding external fact-checking capabilities
Improving model performance with additional training data
👩‍💻 Project Information

Project: Fake News Detection System
Type: Group Project
Duration: January 2025 – March 2025
Domain: Machine Learning / Natural Language Processing

📄 License

This project is created for educational and academic purposes.
