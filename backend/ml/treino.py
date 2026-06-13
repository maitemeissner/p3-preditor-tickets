import sqlite3
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

DB_PATH = "data/database.sqlite"
MODEL_PATH = "backend/ml/modelo.pkl"

def treinar():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM tickets", conn)
    conn.close()

    if len(df) < 10:
        print("Dados insuficientes para treino. Gerando dados sintéticos...")
        from ml.dataset_generator import gerar_dataset
        df = gerar_dataset(500)

    mapping = {'Chat': 0, 'Ticket': 1, 'Voz': 2, 'Email': 3}
    cat_map = {'suporte': 0, 'financeiro': 1, 'tecnico': 2, 'comercial': 3}
    prio_map = {'baixa': 0, 'media': 1, 'alta': 2, 'critica': 3}

    df['canal_enc'] = df['canal'].map(mapping).fillna(0)
    df['categoria_enc'] = df['categoria'].map(cat_map).fillna(0)
    df['prioridade_enc'] = df['prioridade'].map(prio_map).fillna(0)

    feature_cols = ['canal_enc', 'categoria_enc', 'prioridade_enc', 'tma_minutos', 'csat']
    X = df[feature_cols].fillna(0)
    y = df['reopened']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    acc = model.score(X, y)
    print(f"Modelo treinado com acurácia: {acc:.2%}")
    return acc

if __name__ == "__main__":
    treinar()