-- Extração de features para modelo preditivo de tickets negativos

-- Feature 1: Volume de tickets por setor nos últimos 30 dias
SELECT
    setor,
    COUNT(*) AS volume_30d
FROM tickets
WHERE data_criacao >= DATE('now', '-30 days')
GROUP BY setor;

-- Feature 2: Taxa de reabertura por cliente
SELECT
    cliente_id,
    COUNT(CASE WHEN reaberto = 1 THEN 1 END) * 1.0 / COUNT(*) AS taxa_reabertura
FROM tickets
GROUP BY cliente_id;

-- Feature 3: Tempo médio de resolução por setor (em horas)
SELECT
    setor,
    AVG(CAST(STRFTIME('%s', data_resolucao) - STRFTIME('%s', data_criacao) AS REAL) / 3600) AS tempo_medio_horas
FROM tickets
WHERE data_resolucao IS NOT NULL
GROUP BY setor;

-- Feature 4: Palavras-chave negativas na descrição
SELECT
    id,
    CASE
        WHEN descricao LIKE '%reclamação%' THEN 1
        WHEN descricao LIKE '%cancelar%' THEN 1
        WHEN descricao LIKE '%problema%' THEN 1
        WHEN descricao LIKE '%erro%' THEN 1
        ELSE 0
    END AS contem_palavra_negativa
FROM tickets;

-- Feature 5: Quantidade de interações por ticket
SELECT
    ticket_id,
    COUNT(*) AS total_interacoes
FROM interacoes
GROUP BY ticket_id;
