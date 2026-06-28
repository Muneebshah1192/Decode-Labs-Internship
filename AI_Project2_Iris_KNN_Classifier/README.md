# AI Project 2: Iris Flower Classification Using KNN

A professional web-based Artificial Intelligence project for **Data Classification Using AI**. This project uses the Iris flower dataset and a supervised machine learning algorithm called **K-Nearest Neighbors (KNN)** to classify flowers into different species.

---

## Project Overview

This project is built as part of **Artificial Intelligence Project 2**. The main goal is to create a basic classification model using a small dataset, train it using supervised learning, and test its performance using evaluation metrics.

The project includes:

* Dataset loading
* Dataset understanding
* Train-test split
* Feature scaling
* KNN classification model
* Model prediction
* Confusion matrix
* Accuracy score
* F1 score
* Flask-based web interface

---

## Project Title

**Iris Flower Classification Using KNN Algorithm**

---

## Objective

The objective of this project is to build a supervised machine learning classification model that can predict the species of an Iris flower based on four input features:

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

The model predicts one of the following flower species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Pandas
* Scikit-learn
* Joblib
* Matplotlib
* Seaborn

---

## Machine Learning Algorithm

The algorithm used in this project is:

### K-Nearest Neighbors Classifier

KNN is a supervised machine learning algorithm. It classifies new data points based on the majority class of their nearest neighbors. In this project, KNN is used to classify Iris flowers based on their flower measurements.

---

## Dataset

The project uses the **Iris.csv** dataset downloaded from Kaggle.

The dataset contains:

* 150 samples
* 3 classes
* 4 input features
* Balanced flower categories

### Dataset Columns

| Column Name   | Description                 |
| ------------- | --------------------------- |
| SepalLengthCm | Sepal length in centimeters |
| SepalWidthCm  | Sepal width in centimeters  |
| PetalLengthCm | Petal length in centimeters |
| PetalWidthCm  | Petal width in centimeters  |
| Species       | Flower species              |

---

## Folder Structure

```text
AI_Project2_Iris_Website/
│
├── app.py
├── requirements.txt
├── README.md
├── SUBMISSION_REPORT.txt
├── run.bat
├── run.sh
│
├── data/
│   └── Iris.csv
│
├── models/
│   ├── iris_knn_model.pkl
│   ├── iris_scaler.pkl
│   └── iris_label_encoder.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
└── templates/
    ├── index.html
    ├── result.html
    └── about.html
```

---

## Required Files

Before running the website, make sure these files are placed correctly.

### Dataset File

Place the CSV file here:

```text
data/Iris.csv
```

### Model Files

Place your trained model files here:

```text
models/iris_knn_model.pkl
models/iris_scaler.pkl
models/iris_label_encoder.pkl
```

If the model files are missing, the website may use a fallback model depending on the project version.

---

## How to Run the Project

### Step 1: Extract the ZIP File

Extract the project ZIP folder.

```text
AI_Project2_Iris_Website.zip
```

Open the extracted folder in VS Code or any code editor.

---

### Step 2: Install Requirements

Open terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

---

### Step 3: Run Flask App

Run this command:

```bash
python app.py
```

---

### Step 4: Open Website

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How to Use the Website

Enter flower measurement values in the input form.

Example values:

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

The model will predict the flower species.

Expected result:

```text
Iris-setosa
```

---

## Model Training Process

The machine learning process follows these steps:

1. Load the Iris dataset
2. Understand dataset shape, columns, and classes
3. Separate input features and target labels
4. Convert species names into numeric labels
5. Split data into training and testing sets
6. Apply StandardScaler for feature scaling
7. Train the KNN classifier
8. Make predictions on test data
9. Evaluate the model using accuracy and F1 score
10. Display confusion matrix and classification report

---

## Evaluation Metrics

The model is evaluated using:

### Accuracy

Accuracy shows how many predictions were correct out of total predictions.

### Precision

Precision shows how many predicted positive results were actually correct.

### Recall

Recall shows how many actual positive results were correctly identified.

### F1 Score

F1 score is the harmonic mean of precision and recall.

### Confusion Matrix

The confusion matrix shows correct and incorrect predictions for each class.

---

## Sample Output

```text
Accuracy: 1.0
F1 Score: 1.0

Predicted Flower Species: Iris-setosa
```

The actual accuracy may vary depending on the train-test split and selected K value.

---

## Why Feature Scaling Is Used

KNN is distance-based. It calculates the distance between data points. If one feature has a larger scale than others, it can dominate the result.

To solve this, StandardScaler is used. It balances the feature values by converting them into a standard scale.

---

## Why Train-Test Split Is Used

The dataset is divided into two parts:

* Training set
* Testing set

The training set is used to teach the model. The testing set is used to check how well the model performs on unseen data.

This helps measure the real performance of the model.

---

## Conclusion

This project demonstrates the complete supervised learning pipeline for data classification. It uses the Iris dataset, applies feature scaling, trains a KNN classification model, and evaluates the output using accuracy, F1 score, classification report, and confusion matrix.

The Flask website makes the project more practical by allowing users to enter flower measurements and receive instant predictions through a clean web interface.

---

## Author

**Muneeb Haider**
AI Developer | Information Security Student | Web Developer

---

## Project Category

Artificial Intelligence
Machine Learning
Supervised Learning
Data Classification
Flask Web Application
