# scripts/train_classifier.py
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib
#scripts/classifier_dataset.json
# Load data
with open("scripts/classifier_dataset.json", encoding="utf-8") as f:
    data = json.load(f)

X = [item["text"] for item in data]
y = [item["label"] for item in data]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "backend/models/classifier.pkl")
