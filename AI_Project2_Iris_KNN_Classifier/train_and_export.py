"""
Train and export Iris KNN model files for the website.
Run this if you want to generate local PKL files:

python train_and_export.py

Outputs:
models/iris_knn_model.pkl
models/iris_scaler.pkl
models/iris_label_encoder.pkl
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Iris.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)


def load_data():
    if DATA_PATH.exists():
        print(f"Loading Kaggle dataset from: {DATA_PATH}")
        df = pd.read_csv(DATA_PATH)
        if "Id" in df.columns:
            df = df.drop("Id", axis=1)
        x = df.drop("Species", axis=1).values
        y_names = df["Species"].values
    else:
        print("data/Iris.csv not found. Using sklearn built-in Iris dataset.")
        iris = load_iris()
        x = iris.data
        y_names = np.array([f"Iris-{name}" for name in iris.target_names])[iris.target]
    return x, y_names


x, y_names = load_data()
encoder = LabelEncoder()
y = encoder.fit_transform(y_names)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")

print("Accuracy:", round(accuracy, 4))
print("F1 Score:", round(f1, 4))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

joblib.dump(model, MODEL_DIR / "iris_knn_model.pkl")
joblib.dump(scaler, MODEL_DIR / "iris_scaler.pkl")
joblib.dump(encoder, MODEL_DIR / "iris_label_encoder.pkl")

print("\nSaved model files inside models/ folder.")
