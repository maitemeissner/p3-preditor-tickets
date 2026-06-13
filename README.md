# P3 — Preditor de Tickets Negativos + Gargalos

ML que prevê tickets negativos antes que aconteçam e diagnostica gargalos operacionais.

## Stack
- **Frontend:** React (Vite) + TypeScript
- **Backend:** Python FastAPI + ML (scikit-learn)
- **MCP Server:** Node + TypeScript + Express
- **Banco:** SQLite (Fly.io PostgreSQL em produção)
- **Cron:** APScheduler interno
- **LGPD:** Presidio anonymizer
- **Deploy:** Fly.io

## Estrutura
```
├── frontend/           # React app
├── backend/            # FastAPI + ML + LGPD + Crons
├── mcp-server/         # MCP para OpenClaw
├── docker-compose.yml  # Orquestração Fly.io
└── fly.toml            # Config deploy
```