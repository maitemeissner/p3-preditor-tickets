import re
import hashlib

PII_FIELDS = ["nome", "email", "cpf", "telefone", "endereco", "cep"]

def mascarar(valor: str) -> str:
    if not valor:
        return valor
    if "@" in valor:
        partes = valor.split("@")
        return partes[0][0] + "***@" + partes[1]
    if len(valor) >= 4:
        return valor[:2] + "***" + valor[-2:]
    return "***"

def hash_valor(valor: str) -> str:
    return hashlib.sha256(valor.encode()).hexdigest()[:16]

def anonimizar_registro(registro: dict) -> dict:
    anon = {}
    for chave, valor in registro.items():
        chave_lower = chave.lower()
        if any(p in chave_lower for p in PII_FIELDS):
            anon[chave] = mascarar(str(valor))
            anon[f"{chave}_hash"] = hash_valor(str(valor))
        else:
            anon[chave] = valor
    return anon

def gerar_relatorio_anonimizado() -> dict:
    dados_mock = [
        {"id": 1, "nome": "João Silva", "email": "joao@email.com", "cpf": "12345678900", "setor": "Suporte N1", "ticket_negativo": True},
        {"id": 2, "nome": "Maria Souza", "email": "maria@email.com", "cpf": "98765432100", "setor": "Financeiro", "ticket_negativo": False},
        {"id": 3, "nome": "Carlos Pereira", "email": "carlos@email.com", "cpf": "45678912300", "setor": "TI", "ticket_negativo": True},
    ]

    relatorio = {
        "total_registros": len(dados_mock),
        "campos_anonimizados": PII_FIELDS,
        "dados": [anonimizar_registro(r) for r in dados_mock],
    }

    return relatorio
