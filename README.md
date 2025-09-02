# Twitter Sentiment Analysis 🐦

A modern, minimal web application that analyzes the sentiment of text using machine learning. Built with a trained Logistic Regression model and featuring a clean, aesthetic user interface.

![Sentiment Analysis Demo](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7+-blue) ![Flask](https://img.shields.io/badge/Flask-2.3+-red) ![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange)

## ✨ Features

- **🎯 Real-time Sentiment Analysis** - Instant classification of text as positive or negative
- **📊 Confidence Scoring** - Get confidence percentages for predictions
- **🎨 Minimal Aesthetic UI** - Clean, modern interface with smooth animations
- **📱 Responsive Design** - Works perfectly on desktop and mobile devices
- **⚡ Fast Processing** - Optimized TF-IDF vectorization and Logistic Regression
- **🔍 Text Preprocessing** - Advanced text cleaning with stemming and stopword removal

## 🛠️ Tech Stack

### Backend
- **Python 3.7+**
- **Flask** - Web framework
- **Scikit-learn** - Machine learning library
- **NLTK** - Natural language processing
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Joblib** - Model serialization

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradients and animations
- **JavaScript** - Interactive functionality

### Machine Learning
- **Logistic Regression** - Classification algorithm
- **TF-IDF Vectorizer** - Feature extraction
- **Porter Stemmer** - Word stemming
- **Sentiment140 Dataset** - Training data (1.6M tweets)

## 🎮 Usage

### Web Interface
1. Open the application in your browser
2. Type or paste text in the textarea
3. Click "Analyze Sentiment"
4. View the results with confidence score


## 🧠 Model Details

### Training Data
- **Dataset**: Sentiment140 (1.6 million tweets)
- **Classes**: Binary (0 = Negative, 4 = Positive → 0, 1)
- **Preprocessing**: Text cleaning, stemming, stopword removal

### Model Performance
- **Algorithm**: Logistic Regression
- **Features**: TF-IDF vectors (max 5000 features)
- **Accuracy**: ~78-82% on test data
- **Training Time**: ~2-3 minutes

### Text Preprocessing Pipeline
1. Remove non-alphabetic characters
2. Convert to lowercase
3. Tokenization
4. Remove stopwords
5. Porter stemming
6. TF-IDF vectorization

## 🎨 UI Features

- **Gradient Backgrounds** - Beautiful color transitions
- **Smooth Animations** - Fade-in effects and loading states
- **Auto-resize Textarea** - Dynamic height adjustment
- **Color-coded Results** - Green for positive, red for negative
- **Loading Indicators** - Visual feedback during processing
- **Example Suggestions** - Random placeholder examples





