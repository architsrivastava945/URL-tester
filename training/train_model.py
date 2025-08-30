import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os
from features.extract_features import extract_features_from_series

# 1. Load Dataset
df = pd.read_csv("data/malicious_phish.csv")
df = df[['url', 'type']]  # Keep only relevant columns

# 2. Encode Labels
df['label'] = df['type'].apply(lambda x: 1 if x == 'phishing' else 0)
df.drop('type', axis=1, inplace=True)

# 3. Extract Features
features = extract_features_from_series(df['url'])
X = pd.DataFrame(features)
y = df['label']

# 4. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# 6. Evaluate
y_pred = clf.predict(X_test)
print("✅ Model Evaluation:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Save Model
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/url_model.pkl")
print("✅ Model saved to models/url_model.pkl")
