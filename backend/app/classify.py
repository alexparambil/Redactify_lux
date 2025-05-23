 
import joblib
from sklearn.pipeline import Pipeline

model: Pipeline = joblib.load("models/classifier.pkl")

def classify_text(text: str):
    return model.predict([text])[0]
