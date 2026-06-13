import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "modelo.pkl")

def treinar_modelo() -> float:
    np.random.seed(42)

    X = np.random.rand(200, 5)
    y = (X[:, 0] + X[:, 1] * 0.5 > 0.8).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    return round(acuracia, 4)
