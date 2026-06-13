import pickle
import os
import numpy as np
import pandas as pd
from io import BytesIO

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "modelo.pkl")

def _carregar_modelo():
    if not os.path.exists(MODEL_PATH):
        return None
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def predizer_ticket(setor: str, descricao: str) -> dict:
    model = _carregar_modelo()
    features = np.random.rand(5).reshape(1, -1)

    if model:
        proba = model.predict_proba(features)[0]
        negativo = bool(model.predict(features)[0])
    else:
        proba = [0.7, 0.3]
        negativo = False

    return {
        "setor": setor,
        "descricao": descricao[:50],
        "negativo": negativo,
        "probabilidade": round(float(proba[1]), 4),
        "status": "modelo_nao_encontrado" if model is None else "sucesso",
    }

def predizer_batch(csv_bytes: bytes) -> list:
    df = pd.read_csv(BytesIO(csv_bytes))
    model = _carregar_modelo()

    resultados = []
    for _, row in df.iterrows():
        features = np.random.rand(5).reshape(1, -1)
        if model:
            proba = model.predict_proba(features)[0]
            negativo = bool(model.predict(features)[0])
        else:
            proba = [0.7, 0.3]
            negativo = False

        resultados.append({
            "setor": row.get("setor", "desconhecido"),
            "descricao": str(row.get("descricao", ""))[:50],
            "negativo": negativo,
            "probabilidade": round(float(proba[1]), 4),
        })

    return resultados
