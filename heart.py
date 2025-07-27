import pandas as pd
import gradio as gr
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load your dataset
df = pd.read_csv("heart-disease.csv")  # Make sure this file exists in the same directory

# Features and target
X = df.drop('target', axis=1)
y = df['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Prediction function
def predict(*inputs):
    input_data = [list(inputs)]
    prediction = model.predict(input_data)[0]
    return f"Predicted Class: {prediction} | Model Accuracy: {accuracy:.2f}"

# Gradio interface
input_components = [gr.Number(label=col) for col in X.columns]
output_component = gr.Textbox(label="Result")

app = gr.Interface(fn=predict, inputs=input_components, outputs=output_component, title="Heart Disease Predictor")
app.launch()
