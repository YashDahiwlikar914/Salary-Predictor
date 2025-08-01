# Final clean training script for deployment
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("Salary.csv")
X = data[["YearsExperience"]]
y = data["Salary"]

# Train on full dataset
model = LinearRegression()
model.fit(X, y)

# Save for Streamlit app
with open("salary_model.pkl", "wb") as f:
    pickle.dump(model, f)
