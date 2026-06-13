from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import os
from datetime import datetime

app = FastAPI(title="Preditor de Tickets Negativos", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

DB_PATH = "data/database.sqlite"

def get_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.on_event("startup")
def startup():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            canal TEXT, categoria TEXT, prioridade TEXT,
            tma_minutos INTEGER, csat REAL, reopened INTEGER,
            data_abertura TEXT
        )
    ''')
    conn.commit()
    conn.close()
    from crons.scheduler import init_scheduler
    init_scheduler()

class TicketInput(BaseModel):
    canal: str
    categoria: str
    prioridade: str
    tma_minutos: int
    csat: float

@app.get("/health")
def health():
    return {"status": "ok", "service": "preditor-tickets"}

@app.post("/prever")
def prever(ticket: TicketInput):
    try:
        from ml.preditor import predict
        prob = predict(ticket.canal, ticket.categoria, ticket.prioridade, ticket.tma_minutos, ticket.csat)
        return {"probabilidade_reabertura": round(prob, 4), "risco": "alto" if prob > 0.5 else "baixo"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/gargalos")
def gargalos():
    conn = get_db()
    rows = conn.execute(
        "SELECT canal, AVG(tma_minutos) as avg_tma, COUNT(*) as total, AVG(reopened) as reopen_rate FROM tickets GROUP BY canal"
    ).fetchall()
    conn.close()
    return {"gargalos": [dict(r) for r in rows]}

@app.get("/relatorio-lgpd")
def relatorio_lgpd():
    return {
        "dados_anonimizados": True,
        "campos_ofuscados": ["nome_cliente", "email", "telefone", "documento"],
        "base_legal": "LGPD Art. 7, Incisos I e II (consentimento e cumprimento legal)",
        "data_geracao": datetime.now().isoformat()
    }