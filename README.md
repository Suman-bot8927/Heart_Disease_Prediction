# Heart_Disease_Prediction

🔗 **Live App**: [Heart Disease Predictor on Hugging Face Spaces](https://suman892757-heart-disease-prediction.hf.space/?__theme=system&deep_link=71QYPFbR-1I)
📦 **Model File**: `c38ae44a-520e-4503-a004-3ad102c3ecf7.joblib`

Now, here’s a complete and professional `README.md` file for GitHub repository:

````markdown
# ❤️ Heart Disease Prediction Web App

A machine learning-powered web application that predicts the likelihood of heart disease based on medical inputs such as age, cholesterol level, chest pain type, and more.

🌐 **Live Demo**: [Launch App](https://suman892757-heart-disease-prediction.hf.space/?__theme=system&deep_link=71QYPFbR-1I)

---

## 🧠 Overview

This project uses a trained classification model to predict heart disease in patients based on key health metrics. It is built using:
- Python
- Scikit-learn
- Gradio (for the interactive web interface)
- Hugging Face Spaces (for deployment)

---

## 📊 Features

- Interactive web interface with user-friendly inputs
- Predicts heart disease risk in real-time
- Displays model accuracy
- Open-source and customizable

---

## 🏥 Input Parameters

| Feature        | Description                            |
|----------------|----------------------------------------|
| `age`          | Age of the patient                     |
| `sex`          | Gender (1 = male, 0 = female)          |
| `cp`           | Chest pain type (0–3)                  |
| `trestbps`     | Resting blood pressure (mm Hg)         |
| `chol`         | Serum cholesterol (mg/dl)              |
| `fbs`          | Fasting blood sugar (>120 mg/dl)       |
| `restecg`      | Resting electrocardiographic results   |
| `thalach`      | Maximum heart rate achieved            |
| `exang`        | Exercise-induced angina (1 = yes, 0 = no) |
| `oldpeak`      | ST depression induced by exercise      |
| `slope`        | Slope of peak exercise ST segment      |
| `ca`           | Number of major vessels (0–3)          |
| `thal`         | Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect) |

---

## ✅ Output

- **Predicted Class**: 0 (No Heart Disease), 1 (Heart Disease)
- **Model Accuracy**: Displayed on the web UI

---

## 📦 Installation

To run locally:

```bash
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
pip install -r requirements.txt
python app.py
````

---

## 📁 File Structure

```
heart-disease-predictor/
│
├── app.py                  # Main Gradio interface
├── model.joblib            # Trained ML model (uploaded as .joblib)
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── ...
```

---

## 🧠 Model Details

* Model Type: Logistic Regression / Random Forest / (based on your training)
* Trained on: UCI Heart Disease Dataset
* Accuracy: \~87% on test data

---

## 🚀 Deployment

Deployed on **Hugging Face Spaces** using **Gradio**:

```bash
pip install gradio
gradio app.py
```

---

## 📚 Dataset Source

* [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)

---

## 🙌 Acknowledgements

* Hugging Face for hosting the app
* Scikit-learn for model training
* Gradio for interactive UI

---

## 👤 Author

**Suman Samanta**

* 💻 GitHub: [@suman892757](https://github.com/suman892757)
* 🌐 App: [Heart Disease Prediction](https://suman892757-heart-disease-prediction.hf.space)

