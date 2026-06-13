import { useState } from 'react';
import { preverTicket, preverBatch } from '../api';

export default function Previsao() {
  const [ticket, setTicket] = useState({ setor: '', descricao: '' });
  const [resultado, setResultado] = useState<Record<string, unknown> | null>(null);
  const [file, setFile] = useState<File | null>(null);
  const [batchResult, setBatchResult] = useState<Record<string, unknown> | null>(null);

  const handlePrever = async () => {
    const res = await preverTicket(ticket);
    setResultado(res);
  };

  const handleBatch = async () => {
    if (!file) return;
    const res = await preverBatch(file);
    setBatchResult(res);
  };

  return (
    <div>
      <h1>Previsão de Tickets</h1>

      <section style={{ marginBottom: '2rem' }}>
        <h2>Previsão Individual</h2>
        <input placeholder="Setor" value={ticket.setor} onChange={e => setTicket(p => ({ ...p, setor: e.target.value }))} />
        <input placeholder="Descrição" value={ticket.descricao} onChange={e => setTicket(p => ({ ...p, descricao: e.target.value }))} />
        <button onClick={handlePrever}>Prever</button>
        {resultado && <pre>{JSON.stringify(resultado, null, 2)}</pre>}
      </section>

      <section>
        <h2>Previsão em Lote (CSV)</h2>
        <input type="file" accept=".csv" onChange={e => setFile(e.target.files?.[0] || null)} />
        <button onClick={handleBatch} disabled={!file}>Enviar</button>
        {batchResult && <pre>{JSON.stringify(batchResult, null, 2)}</pre>}
      </section>
    </div>
  );
}
