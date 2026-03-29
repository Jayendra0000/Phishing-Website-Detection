import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from features.url_features import extract_url_features

print("📥 Loading dataset...")
df = pd.read_csv("dataset/processed/full_dataset.csv")

# Extract features
print("🔍 Extracting features (this may take time)...")
X = np.array([extract_url_features(url) for url in df["url"]])
y = df["label"].values

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("🧠 Training RandomForest model...")
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    class_weight={0: 1, 1: 2},  # Penalize missing phishing
    random_state=42,
    n_jobs=-1
)


model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-score : {f1:.4f}")

# Save model
joblib.dump(model, "model/phishing_model.pkl")
print("\n💾 Model saved to model/phishing_model.pkl")
