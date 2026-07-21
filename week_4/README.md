## Supervised Learning — Regression Model

### 👩‍💻 Intern Information

**Name:** Fiza Zahid Ali  
**Discipline:** Bachelor of Science in Artificial Intelligence (BSAI)  
**Internship:** Machine Learning Internship – Zynxis  
**Week:** 4  

---

## 📌 Weekly Objective

The objective of Week 4 was to build supervised machine learning regression models to predict a continuous numerical value.

For this task, the California Housing dataset was used to predict median house values based on different housing-related features.

Three regression algorithms were implemented:

1. Linear Regression
2. Ridge Regression
3. Random Forest Regressor

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

Actual vs predicted values were also visualized for each regression model.

---

## 📂 Dataset

**Dataset:** California Housing Dataset

**Target Variable:** `MedHouseVal`

The target variable represents the median house value.

The dataset contains housing-related features including:

- Median Income
- House Age
- Average Number of Rooms
- Average Number of Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

---

## 🛠️ Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- Jupyter Notebook

---

## 🔄 Machine Learning Workflow

The following steps were performed:

1. Loaded the California Housing dataset
2. Explored the dataset structure
3. Checked for missing values
4. Checked for duplicate records
5. Separated features (`X`) and target (`y`)
6. Split the dataset into training and testing sets
7. Trained Linear Regression
8. Trained Ridge Regression
9. Trained Random Forest Regressor
10. Generated predictions for each model
11. Evaluated the models using MAE, MSE, and R² Score
12. Created Actual vs Predicted visualizations
13. Saved the visualizations as PNG files

---

## 🤖 Models Used

### 1. Linear Regression

Linear Regression is a supervised learning algorithm that models the relationship between input features and a continuous target variable.

It was used as a baseline regression model for predicting median house values.

### 2. Ridge Regression

Ridge Regression is a regularized version of Linear Regression. It adds a penalty to large model coefficients, which can help reduce overfitting and improve model stability.

### 3. Random Forest Regressor

Random Forest Regressor is an ensemble learning algorithm that combines multiple decision trees to predict continuous numerical values.

It can capture complex and nonlinear relationships between input features and the target variable.

---

## 📊 Model Evaluation Results

The models were evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score.

| Model | MAE | MSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.5332 | 0.5559 | 0.5758 |
| Ridge Regression | 0.5332 | 0.5558 | 0.5759 |
| Random Forest Regressor | 0.3275 | 0.2554 | 0.8051 |

### Understanding the Metrics

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted values. Lower values indicate smaller errors.
- **MSE (Mean Squared Error):** Measures the average squared difference between actual and predicted values. Lower values indicate better performance.
- **R² Score:** Measures how well the model explains the variation in the target variable. Higher values indicate better performance.

---

## 📈 Actual vs Predicted Visualization

Actual vs Predicted graphs were created for all three regression models.

The graphs compare:

- **Actual Values** — The real target values from the testing dataset.
- **Predicted Values** — The values predicted by each regression model.

A diagonal reference line was included to represent perfect predictions. Predictions closer to this line indicate better agreement between actual and predicted values.

The following graphs were generated:

- `linear_regression_actual_vs_predicted.png`
- `ridge_regression_actual_vs_predicted.png`
- `random_forest_actual_vs_predicted.png`

---

## 📁 Project Files

The repository contains:

- `Week4__Regression_model.ipynb` — Complete regression notebook
- `linear_regression_actual_vs_predicted.png` — Linear Regression visualization
- `ridge_regression_actual_vs_predicted.png` — Ridge Regression visualization
- `random_forest_actual_vs_predicted.png` — Random Forest visualization
- `README.md` — Project documentation

---

## 📚 What I Learned

During Week 4, I learned how to:

- Understand supervised regression problems
- Predict continuous numerical values
- Prepare features and target variables
- Split datasets into training and testing sets
- Train Linear Regression models
- Apply Ridge Regression
- Train Random Forest Regressors
- Generate predictions
- Evaluate regression models using MAE, MSE, and R² Score
- Visualize actual vs predicted values
- Save Matplotlib visualizations as PNG files

---

## 🚀 Weekly Progress

Week 4 helped me strengthen my understanding of supervised learning for continuous prediction problems. I learned the difference between classification and regression and gained practical experience in training multiple regression algorithms and evaluating their predictions using appropriate regression metrics.

---

**Author:** Fiza Zahid Ali  
**Discipline:** BS Artificial Intelligence  
**Organization:** Zynxis  
**Internship:** Machine Learning Internship
