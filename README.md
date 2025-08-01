# 🧠 Salary Predictor — Simple Linear Regression Project

A small project where I used Python and Linear Regression to predict salaries based on years of experience.

This was one of my first machine learning experiments — just wanted to understand how models learn from data and make predictions.

---

## 📁 What’s Inside

- `Salary.csv`: The dataset (Years of Experience vs Salary)
- Python script that:
  - Loads the data using Pandas
  - Splits it into train/test sets
  - Trains a Linear Regression model (from scikit-learn)
  - Visualizes both the training and test set results
  - Evaluates accuracy using R² Score

---

## 🛠 Tools & Libraries

- Python 🐍
- NumPy
- Pandas
- Matplotlib
- scikit-learn

---

## 📊 Model Performance

- **R² Score**: `0.94` — pretty good for a simple straight-line fit!

---

## 📸 Sample Visuals

Training set plot:
_(Experience vs Salary with regression line)_

Test set plot:
_(How well the model generalizes on unseen data)_

> I haven’t included the `.png` files here, but the code generates them when you run it.

---

## 🚀 How to Run

1. Clone this repo  
2. Make sure you have Python + pip installed  
3. Run:

```bash
pip install numpy pandas matplotlib scikit-learn
python main.py
