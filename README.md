# 💼 Salary Predictor — ML + Streamlit App

A mini machine learning project where I trained a simple **Linear Regression model** to predict salaries based on years of experience. The app is deployed using **Streamlit**, with a clean and minimal interface.

Built to practice the full ML pipeline: data → model → deployment.

## 🔗 Live App

👉 [Open the App](https://salarypredictor914.streamlit.app/)

## 📌 What This Does

- Takes user input: **Years of Experience**
- Uses a trained **Linear Regression model**
- Predicts the **estimated salary**
- Displays the result with a modern UI

## 🧠 Why I Built This

I wanted to go beyond notebooks and build something usable — a small tool where I could practice:
- Cleaning and training models
- Saving with `pickle`
- Building a real app with **Streamlit**
- Deploying it so anyone can use it

It’s basic, but real.

## ⚙️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/salary-predictor.git
cd salary-predictor
````

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Train the model

```bash
python train_model.py
```

### 4. Launch the app

```bash
streamlit run app.py
```

Open your browser → `http://localhost:8501`

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Pickle
* Streamlit

## 📦 `requirements.txt`

```txt
streamlit
scikit-learn
pandas
numpy
```

## 🧪 Model Info

* **Model**: Linear Regression
* **Input**: `YearsExperience` (float)
* **Output**: `Salary` (float)
* **Training**: Model is trained on 100% of the dataset (for real-world use)

## ✅ How It Works (Code)

### `train_model.py`

* Reads `Salary.csv`
* Uses `"YearsExperience"` as input
* Trains a `LinearRegression` model
* Saves it with `pickle` for later use in the app

### `app.py`

* Loads the model using `pickle`
* Streamlit UI asks user for years of experience
* Predicts salary using `.predict()`
* Shows the result in real-time

## 🧠 What I Learned

* Full ML pipeline (training → saving → deployment)
* Working with `pickle` and model serialisation
* Streamlit for fast app development
* Clean deployment setup with `requirements.txt`

