## Supervised Learning — Classification Model

### 👩‍💻 Intern Information

**Name:** Fiza Zahid Ali  
**Discipline:** Bachelor of Science in Artificial Intelligence (BSAI)  
**Internship:** Machine Learning Internship – Zynxis  
**Week:** 3  

---

## 📌 Weekly Objective

The objective of Week 3 was to build supervised machine learning classification models to predict a real-world outcome.

For this task, the Titanic dataset was used to predict whether a passenger survived based on passenger-related features.

Three different classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 📂 Dataset

**Dataset:** Titanic Dataset

**Target Variable:** `Survived`

The target variable represents whether a passenger survived:

- `0` → Did not survive
- `1` → Survived

The cleaned dataset prepared during Week 2 was used for model training.

---

## 🛠️ Technologies and Libraries

- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab
- Jupyter Notebook

---

## 🔄 Machine Learning Workflow

The following steps were performed:

1. Loaded the cleaned Titanic dataset
2. Explored the dataset
3. Checked data types and missing values
4. Separated features (`X`) and target (`y`)
5. Split the dataset into training and testing sets
6. Trained Logistic Regression
7. Trained Decision Tree Classifier
8. Trained Random Forest Classifier
9. Generated predictions using each model
10. Evaluated the models using Accuracy, Precision, Recall, and F1 Score
11. Created a model comparison table
12. Analyzed the performance of the models

---

## 🤖 Models Used

### 1. Logistic Regression

Logistic Regression is a classification algorithm used to predict binary outcomes. In this project, it was used to predict whether a passenger survived or did not survive.

### 2. Decision Tree Classifier

Decision Tree Classifier makes predictions by creating a series of decision rules based on the input features.

### 3. Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to make predictions and improve generalization.

---

## 📊 Model Evaluation Results

The models were evaluated using four metrics:

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.7939 | 0.7458 | 0.6984 | 0.7213 |
| Decision Tree | 0.7939 | 0.7302 | 0.7302 | 0.7302 |
| Random Forest | 0.8061 | 0.7719 | 0.6984 | 0.7333 |

---

## 🏆 Model Analysis

Based on the evaluation results, Random Forest achieved the highest overall performance.

It obtained:

- Highest Accuracy: **80.61%**
- Highest Precision: **77.19%**
- Highest F1 Score: **73.33%**

The Decision Tree achieved a slightly higher Recall of **73.02%**, compared with **69.84%** for Random Forest.

Random Forest was considered the best overall-performing model because it achieved the highest accuracy, precision, and F1 score among the three models, while maintaining competitive recall.

---

## 📁 Project Files

The repository contains:

- `Week3_Supervised_Learning_Classification.ipynb` — Complete machine learning notebook
- `Cleaned_Titanic.csv` — Cleaned dataset used for model training
- `model_comparison.csv` — Classification model evaluation results
- `README.md` — Project documentation

---

## 📚 What I Learned

During Week 3, I learned how to:

- Understand supervised classification problems
- Prepare features and target variables
- Split data into training and testing sets
- Train multiple classification algorithms
- Generate predictions
- Evaluate classification models
- Understand Accuracy, Precision, Recall, and F1 Score
- Compare the performance of different classification models
- Select a suitable model based on evaluation metrics

## 🚀 Weekly Progress

Week 3 helped me strengthen my understanding of supervised machine learning and classification algorithms. I learned how different models perform on the same dataset and how evaluation metrics can be used to assess their performance.

---

**Author:** Fiza Zahid Ali  
**Discipline:** BS Artificial Intelligence  
**Organization:** Zynxis  
**Internship:** Machine Learning Internship
