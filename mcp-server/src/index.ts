import express from "express";
const app = express();
const PORT = parseInt(process.env.PORT || "3001");
app.use(express.json());

app.get("/health", (_req, res) => res.json({ status: "ok" }));

app.post("/mcp/prever", (req, res) => {
  const { canal, categoria, prioridade, tma_minutos, csat } = req.body;
  res.json({
    resultado: `Probabilidade simulada para ticket ${canal}/${categoria}: ${Math.random().toFixed(2)}`
  });
});

app.get("/mcp/diagnosticar", (_req, res) => {
  res.json({ gargalos: ["Canal Voz com maior TMA", "Categoria técnica com maior reopening"] });
});

app.listen(PORT, () => console.log(`MCP Preditor running on ${PORT}`));