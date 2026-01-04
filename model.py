import pandas as pd
import pickle
import re
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv("data.csv")

print("Dataset loaded")
print(df.head())
print("\nLabel distribution:")
print(df['label'].value_counts())

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

df['text'] = df['text'].apply(clean_text)

# Train-test split (binary stratified)
X_train, X_test, y_train, y_test = train_test_split(
    df['text'],
    df['label'],
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\n🏆 Model trained and saved successfully!")
