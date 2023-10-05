import nltk
import json
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import random

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Load and process intents from intents.json
with open('intents.json') as file:
    intents = json.load(file)

# Preprocess the intents data
words = []
classes = []
documents = []

lemmatizer = WordNetLemmatizer()

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize and lemmatize words
        words.extend(word_tokenize(pattern))
        documents.append((word_tokenize(pattern), intent['tag']))
    # Track unique classes (tags)
    if intent['tag'] not in classes:
        classes.append(intent['tag'])

# Lemmatize words and remove duplicates
words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalnum()]
words = sorted(list(set(words)))

# Create training data
X_train = []
y_train = []

for (pattern_words, tag) in documents:
    bag = [1 if word in pattern_words else 0 for word in words]
    X_train.append(bag)
    label = classes.index(tag)
    y_train.append(label)

# Train a simple Naive Bayes classifier
classifier = make_pipeline(CountVectorizer(), MultinomialNB())
classifier.fit(X_train, y_train)

# Evaluate the model (optional)
# You can use a separate test dataset and metrics for evaluation
# This example demonstrates training only

# Save the trained model to a file (optional)
# You can use joblib or pickle to save the model for later use
# This example demonstrates training only

# Print a success message
print("Model training completed.")
