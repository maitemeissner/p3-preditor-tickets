import re

PII_PATTERNS = {
    'email': r'[\w\.-]+@[\w\.-]+\.\w+',
    'phone': r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}',
    'cpf': r'\d{3}\.\d{3}\.\d{3}-\d{2}',
    'rg': r'\d{2}\.\d{3}\.\d{3}-\d{1}',
    'cep': r'\d{5}-?\d{3}',
}

def anonimizar(texto: str) -> str:
    resultado = texto
    for tipo, pattern in PII_PATTERNS.items():
        resultado = re.sub(pattern, f'[{tipo.upper()}_OFUSCADO]', resultado)
    return resultado

def anonimizar_dataset(df, colunas_sensiveis=None):
    if colunas_sensiveis is None:
        colunas_sensiveis = ['nome', 'email', 'telefone', 'documento', 'endereco']

    for col in colunas_sensiveis:
        if col in df.columns:
            df[col] = df[col].astype(str).apply(anonimizar)

    return df