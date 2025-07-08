import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_excel(r"C:\Users\Ishika\project\pcos_pcod_analysis_results.xlsx")

# Ensure 'unusual_bleeding' column is correctly processed
df['unusual_bleeding'] = df['unusual_bleeding'].str.lower()
label_encoder = LabelEncoder()
df['unusual_bleeding'] = label_encoder.fit_transform(df['unusual_bleeding'])

# Define Features (X) and Target (Y)
X = df[['age', 'length_of_cycle', 'unusual_bleeding', 'bmi']]
Y = df['pcos_pcod_risk']

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression()
model.fit(X_train, Y_train)

# Save Model & Encoder
joblib.dump(model, "logistic_regression_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

# Load Model & Test Prediction
model = joblib.load("logistic_regression_model.pkl")
y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

print("Model training and saving completed successfully!")
