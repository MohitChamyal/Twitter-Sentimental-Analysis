from flask import Flask, request, jsonify, render_template
import os
import sys

app = Flask(__name__)

# Check if model files exist
MODEL_PATH = 'twitter_sentiment_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    print("❌ Model files not found!")
    print("Please run the model saving code in your Jupyter notebook first.")
    print("Required files:")
    print(f"- {MODEL_PATH}")
    print(f"- {VECTORIZER_PATH}")
    sys.exit(1)

try:
    import joblib
    import re
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    
    # Download required NLTK data
    try:
        nltk.download('stopwords', quiet=True)
    except:
        print("⚠️ NLTK download failed, using backup stopwords")
    
    # Load the saved model and components
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    
    # Initialize preprocessing components
    porter_stemmer = PorterStemmer()
    try:
        stop_words = set(stopwords.words('english'))
    except:
        # Backup stopwords if NLTK fails
        stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'through', 'during', 'before', 'after', 'above', 'below', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once'}
    
    print("✅ Model loaded successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages:")
    print("pip install flask scikit-learn nltk pandas numpy joblib")
    sys.exit(1)

def preprocess_text(text):
    """Preprocess text for sentiment analysis"""
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove stopwords and stem the words
    words = [porter_stemmer.stem(word) for word in words if word not in stop_words]
    
    # Join the processed words back to text
    return ' '.join(words)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get text from request
        data = request.get_json()
        text = data['text']
        
        if not text.strip():
            return jsonify({'error': 'Please enter some text'}), 400
        
        # Preprocess the text
        processed_text = preprocess_text(text)
        
        if not processed_text.strip():
            return jsonify({'error': 'Text contains no meaningful words after processing'}), 400
        
        # Transform using the saved vectorizer
        text_vector = vectorizer.transform([processed_text])
        
        # Make prediction
        prediction = model.predict(text_vector)[0]
        probability = model.predict_proba(text_vector)[0]
        
        # Convert prediction to sentiment
        sentiment = "Positive" if prediction == 1 else "Negative"
        confidence = max(probability) * 100
        
        return jsonify({
            'sentiment': sentiment,
            'confidence': round(confidence, 2),
            'processed_text': processed_text
        })
        
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'model_loaded': True})

if __name__ == '__main__':
    print("🚀 Starting Twitter Sentiment Analysis App...")
    print("📊 Model and vectorizer loaded successfully!")
    print("🌐 Access the app at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
