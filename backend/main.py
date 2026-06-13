import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ml.preditor import predizer_ticket, predizer_batch
from ml.treino import treinar_modelo as treinar
from lgpd.anonymizer import gerar_relatorio_anonimizado

app = FastAPI(title="P3 - Preditor de Tickets Negativos + Gargalos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TicketInput(BaseModel):
    setor: str
    descricao: str

class TreinoOutput(BaseModel):
    status: str
    acuracia: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/prever")
def prever(ticket: TicketInput):
    resultado = predizer_ticket(ticket.setor, ticket.descricao)
    return resultado

@app.post("/prever/batch")
async def prever_batch(file: UploadFile = File(...)):
    contents = await file.read()
    resultados = predizer_batch(contents)
    return {"resultados": resultados}

@app.get("/gargalos")
def gargalos():
    return [
        {"setor": "Suporte N1", "quantidade": 42, "criticidade": "alta"},
        {"setor": "Suporte N2", "quantidade": 18, "criticidade": "media"},
        {"setor": "Financeiro", "quantidade": 7, "criticidade": "baixa"},
        {"setor": "TI", "quantidade": 31, "criticidade": "alta"},
    ]

@app.get("/relatorio-lgpd")
def relatorio_lgpd():
    return gerar_relatorio_anonimizado()

@app.post("/treinar", response_model=TreinoOutput)
def treinar_modelo():
    acuracia = treinar()
    return {"status": "sucesso", "acuracia": acuracia}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
