# AI Project 2: Iris Flower Classification Website

A professional Flask website for **Data Classification Using AI** using the Iris dataset and K-Nearest Neighbors classification.

## Project Features

- Premium responsive UI
- Iris flower prediction form
- KNN classification model
- StandardScaler feature scaling
- Confidence score display
- Model status page
- JSON API endpoint
- Works even if model files are missing
- Supports your Colab-exported `.pkl` files

## Folder Structure

```text
AI_Project2_Iris_Website/
│
├── app.py
├── train_and_export.py
├── requirements.txt
├── run.bat
├── run.sh
├── README.md
├── SUBMISSION_REPORT.txt
│
├── models/
│   ├── PUT_MODEL_FILES_HERE.txt
│   ├── iris_knn_model.pkl              # add later from Colab
│   ├── iris_scaler.pkl                 # add later from Colab
│   └── iris_label_encoder.pkl          # add later from Colab
│
├── data/
│   ├── PUT_IRIS_CSV_HERE.txt
│   └── Iris.csv                        # optional, add later from Kaggle
│
├── static/
│   ├── css/style.css
│   └── js/app.js
│
└── templates/
    ├── base.html
    ├── index.html
    ├── result.html
    ├── about.html
    └── 404.html
```

## How to Run

### Windows

Double-click:

```text
run.bat
```

Or run manually:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Mac/Linux

```bash
chmod +x run.sh
./run.sh
```

Or run manually:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## How to Add Your Colab Model Files

After training in Google Colab, download these files:

```text
iris_knn_model.pkl
iris_scaler.pkl
iris_label_encoder.pkl
```

Put them inside:

```text
models/
```

Then run the website again. It will automatically use your uploaded model files.

## API Usage

Endpoint:

```text
POST /api/predict
```

Example JSON:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Local Training

If you want to train locally:

```bash
python train_and_export.py
```

If `data/Iris.csv` exists, it will use that file. Otherwise it will use sklearn's built-in Iris dataset.

## Project Summary

This project demonstrates a complete supervised learning classification pipeline:

1. Load dataset
2. Understand features and target labels
3. Split data into training and testing sets
4. Apply StandardScaler
5. Train KNN classifier
6. Evaluate with accuracy and F1 score
7. Deploy prediction system using Flask
