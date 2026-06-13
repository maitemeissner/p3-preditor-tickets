import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dataset(qtd=500):
    np.random.seed(42)
    canais = ['Chat', 'Ticket', 'Voz', 'Email']
    categorias = ['suporte', 'financeiro', 'tecnico', 'comercial']
    prioridades = ['baixa', 'media', 'alta', 'critica']

    data = []
    for i in range(qtd):
        canal = np.random.choice(canais)
        categoria = np.random.choice(categorias)
        prioridade = np.random.choice(prioridades)
        tma = int(np.random.exponential(30) + 5)
        csat = round(np.random.uniform(1, 5), 2)
        reopened = int(np.random.random() < 0.12)

        if csat < 2.5:
            reopened = 1
        if prioridade == 'critica' and tma > 120:
            reopened = 1

        data.append({
            'canal': canal, 'categoria': categoria, 'prioridade': prioridade,
            'tma_minutos': min(tma, 300), 'csat': min(csat, 5.0), 'reopened': reopened,
            'data_abertura': (datetime.now() - timedelta(days=int(np.random.random() * 90))).isoformat()
        })

    return pd.DataFrame(data)