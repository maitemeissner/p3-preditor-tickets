import joblib
import numpy as np
import os

MODEL_PATH = "backend/ml/modelo.pkl"

def predict(canal: str, categoria: str, prioridade: str, tma_minutos: int, csat: float) -> float:
    mapping = {'Chat': 0, 'Ticket': 1, 'Voz': 2, 'Email': 3}
    cat_map = {'suporte': 0, 'financeiro': 1, 'tecnico': 2, 'comercial': 3}
    prio_map = {'baixa': 0, 'media': 1, 'alta': 2, 'critica': 3}

    if not os.path.exists(MODEL_PATH):
        from ml.treino import treinar
        treinar()

    model = joblib.load(MODEL_PATH)

    features = np.array([[
        mapping.get(canal, 0),
        cat_map.get(categoria, 0),
        prio_map.get(prioridade, 0),
        tma_minutos,
        csat
    ]])

    prob = model.predict_proba(features)[0][1]
    return float(prob)