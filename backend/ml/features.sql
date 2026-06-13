-- Feature engineering queries for ticket prediction
-- Canal: Chat=0, Ticket=1, Voz=2, Email=3
-- Categoria: suporte=0, financeiro=1, tecnico=2, comercial=3
-- Prioridade: baixa=0, media=1, alta=2, critica=3
-- Features derivadas:
--   - tma_minutos (tempo médio de atendimento)
--   - csat (satisfação do cliente)
--   - hora_abertura (hora do dia)
--   - dia_semana (dia da semana)

CREATE VIEW features AS
SELECT
  CASE canal WHEN 'Chat' THEN 0 WHEN 'Ticket' THEN 1 WHEN 'Voz' THEN 2 WHEN 'Email' THEN 3 ELSE 0 END as canal_enc,
  CASE categoria WHEN 'suporte' THEN 0 WHEN 'financeiro' THEN 1 WHEN 'tecnico' THEN 2 WHEN 'comercial' THEN 3 ELSE 0 END as categoria_enc,
  CASE prioridade WHEN 'baixa' THEN 0 WHEN 'media' THEN 1 WHEN 'alta' THEN 2 WHEN 'critica' THEN 3 ELSE 0 END as prioridade_enc,
  tma_minutos,
  csat,
  reopened as target
FROM tickets;