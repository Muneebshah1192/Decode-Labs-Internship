"""
AI Project 2: Iris Flower Classification Website
------------------------------------------------
A professional Flask interface for a supervised learning classification project.

Expected optional model files inside /models:
- iris_knn_model.pkl
- iris_scaler.pkl
- iris_label_encoder.pkl

If the files are missing, the app automatically trains a fallback KNN model
using scikit-learn's built-in Iris dataset so the website still works.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import joblib
import numpy as np
from flask import Flask, jsonify, render_template, request
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "iris_knn_model.pkl"
SCALER_PATH = MODEL_DIR / "iris_scaler.pkl"
ENCODER_PATH = MODEL_DIR / "iris_label_encoder.pkl"

FEATURE_LABELS = [
    "Sepal Length (cm)",
    "Sepal Width (cm)",
    "Petal Length (cm)",
    "Petal Width (cm)",
]

FEATURE_KEYS = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
]

SAMPLE_FLOWERS = {
    "Iris-setosa": [5.1, 3.5, 1.4, 0.2],
    "Iris-versicolor": [6.0, 2.9, 4.5, 1.5],
    "Iris-virginica": [6.7, 3.0, 5.2, 2.3],
}

SPECIES_INFO = {
    "Iris-setosa": {
        "title": "Iris Setosa",
        "summary": "Usually has smaller petals and is very easy for the model to identify.",
        "badge": "Compact petals",
    },
    "Iris-versicolor": {
        "title": "Iris Versicolor",
        "summary": "Usually sits between Setosa and Virginica, making it a good classification challenge.",
        "badge": "Medium profile",
    },
    "Iris-virginica": {
        "title": "Iris Virginica",
        "summary": "Usually has larger petals and stronger measurements compared with other classes.",
        "badge": "Large petals",
    },
}


@dataclass
class ModelBundle:
    model: object
    scaler: object
    encoder: object
    source: str
    accuracy: float
    f1_score: float


def normalize_species_name(name: str) -> str:
    """Make class names look clean even if model uses sklearn names."""
    clean = str(name).strip()
    if clean.lower() in {"setosa", "iris-setosa", "iris_setosa"}:
        return "Iris-setosa"
    if clean.lower() in {"versicolor", "iris-versicolor", "iris_versicolor"}:
        return "Iris-versicolor"
    if clean.lower() in {"virginica", "iris-virginica", "iris_virginica"}:
        return "Iris-virginica"
    return clean


def train_fallback_model() -> ModelBundle:
    """Train a built-in backup model so the website works without uploaded PKL files."""
    iris = load_iris()
    x = iris.data
    y_names = np.array([f"Iris-{name}" for name in iris.target_names])

    encoder = LabelEncoder()
    y = encoder.fit_transform(y_names[iris.target])

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
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    return ModelBundle(
        model=model,
        scaler=scaler,
        encoder=encoder,
        source="Auto-trained fallback model",
        accuracy=float(acc),
        f1_score=float(f1),
    )


def load_model_bundle() -> ModelBundle:
    """Load saved model files if available; otherwise train fallback model."""
    try:
        if MODEL_PATH.exists() and SCALER_PATH.exists() and ENCODER_PATH.exists():
            model = joblib.load(MODEL_PATH)
            scaler = joblib.load(SCALER_PATH)
            encoder = joblib.load(ENCODER_PATH)

            # Small validation run for display metrics if files load correctly.
            iris = load_iris()
            x = iris.data
            y_names = np.array([f"Iris-{name}" for name in iris.target_names])
            temp_encoder = LabelEncoder()
            y = temp_encoder.fit_transform(y_names[iris.target])
            _, x_test, _, y_test = train_test_split(
                x,
                y,
                test_size=0.2,
                random_state=42,
                stratify=y,
            )
            x_test_scaled = scaler.transform(x_test)
            y_pred = model.predict(x_test_scaled)
            acc = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, average="weighted")

            return ModelBundle(
                model=model,
                scaler=scaler,
                encoder=encoder,
                source="Your uploaded model files",
                accuracy=float(acc),
                f1_score=float(f1),
            )
    except Exception:
        # A broken or incompatible model should never crash the whole website.
        pass

    return train_fallback_model()


bundle = load_model_bundle()
app = Flask(__name__)


def parse_features(form_data) -> Tuple[np.ndarray, Dict[str, float]]:
    """Read and validate numeric flower measurements."""
    values: List[float] = []
    named_values: Dict[str, float] = {}

    for key, label in zip(FEATURE_KEYS, FEATURE_LABELS):
        raw_value = form_data.get(key, "")
        if raw_value is None:
            raw_value = ""
        raw_value = str(raw_value).strip()
        if raw_value == "":
            raise ValueError(f"{label} is required.")
        try:
            value = float(raw_value)
        except ValueError as exc:
            raise ValueError(f"{label} must be a valid number.") from exc

        if value <= 0 or value > 15:
            raise ValueError(f"{label} should be between 0 and 15 cm.")

        values.append(value)
        named_values[label] = value

    return np.array([values], dtype=float), named_values


def predict_species(values: np.ndarray) -> Dict:
    """Scale values and return prediction with confidence data."""
    scaled_values = bundle.scaler.transform(values)
    prediction = bundle.model.predict(scaled_values)

    if hasattr(bundle.encoder, "inverse_transform"):
        predicted_name = bundle.encoder.inverse_transform(prediction)[0]
    else:
        predicted_name = str(prediction[0])

    predicted_name = normalize_species_name(predicted_name)

    confidences = []
    if hasattr(bundle.model, "predict_proba"):
        probabilities = bundle.model.predict_proba(scaled_values)[0]
        if hasattr(bundle.encoder, "classes_"):
            class_names = [normalize_species_name(c) for c in bundle.encoder.classes_]
        else:
            class_names = ["Class 0", "Class 1", "Class 2"]

        for name, probability in zip(class_names, probabilities):
            confidences.append(
                {
                    "name": name,
                    "percent": round(float(probability) * 100, 2),
                }
            )

        confidences = sorted(confidences, key=lambda item: item["percent"], reverse=True)

    top_confidence = confidences[0]["percent"] if confidences else None

    return {
        "species": predicted_name,
        "info": SPECIES_INFO.get(predicted_name, {}),
        "confidence": top_confidence,
        "confidences": confidences,
    }


@app.context_processor
def inject_globals():
    return {
        "project_title": "Iris AI Classifier",
        "model_source": bundle.source,
        "model_accuracy": round(bundle.accuracy * 100, 2),
        "model_f1": round(bundle.f1_score * 100, 2),
        "sample_flowers": SAMPLE_FLOWERS,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        values, named_values = parse_features(request.form)
        result = predict_species(values)
        return render_template("result.html", result=result, values=named_values)
    except ValueError as error:
        return render_template("index.html", error=str(error), old=request.form), 400


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        payload = request.get_json(silent=True) or {}
        values, named_values = parse_features(payload)
        result = predict_species(values)
        return jsonify({"ok": True, "input": named_values, "prediction": result})
    except ValueError as error:
        return jsonify({"ok": False, "error": str(error)}), 400


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "model_source": bundle.source,
            "accuracy_percent": round(bundle.accuracy * 100, 2),
            "f1_percent": round(bundle.f1_score * 100, 2),
        }
    )


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
