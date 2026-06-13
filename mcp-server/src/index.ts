import express from 'express';
import cors from 'cors';

const app = express();
const PORT = process.env.PORT ? parseInt(process.env.PORT) : 3001;

app.use(cors());
app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({ status: 'ok' });
});

app.post('/prever', (req, res) => {
  const { setor, descricao } = req.body;
  res.json({
    setor,
    descricao,
    negativo: Math.random() > 0.6,
    probabilidade: Math.round(Math.random() * 100) / 100,
  });
});

app.get('/gargalos', (_req, res) => {
  res.json([
    { setor: 'Suporte N1', quantidade: 42, criticidade: 'alta' },
    { setor: 'Suporte N2', quantidade: 18, criticidade: 'media' },
    { setor: 'Financeiro', quantidade: 7, criticidade: 'baixa' },
    { setor: 'TI', quantidade: 31, criticidade: 'alta' },
  ]);
});

app.post('/treinar', (_req, res) => {
  res.json({ status: 'sucesso', acuracia: Math.round(Math.random() * 30 + 70) / 100 });
});

app.listen(PORT, () => {
  console.log(`MCP Server rodando na porta ${PORT}`);
});
