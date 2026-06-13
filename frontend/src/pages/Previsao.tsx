import { useState } from 'react';

export default function Previsao() {
  const [form, setForm] = useState({ canal: 'Chat', categoria: 'suporte', prioridade: 'media', tma_minutos: 30, csat: 4 });
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch('/api/prever', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Prever Risco de Reabertura</h1>
      <form onSubmit={handleSubmit}>
        <div><label>Canal: <select value={form.canal} onChange={e => setForm({...form, canal: e.target.value})}>
          <option>Chat</option><option>Ticket</option><option>Voz</option><option>Email</option>
        </select></label></div>
        <div><label>Categoria: <select value={form.categoria} onChange={e => setForm({...form, categoria: e.target.value})}>
          <option>suporte</option><option>financeiro</option><option>tecnico</option><option>comercial</option>
        </select></label></div>
        <div><label>Prioridade: <select value={form.prioridade} onChange={e => setForm({...form, prioridade: e.target.value})}>
          <option>baixa</option><option>media</option><option>alta</option><option>critica</option>
        </select></label></div>
        <div><label>TMA (min): <input type="number" value={form.tma_minutos} onChange={e => setForm({...form, tma_minutos: +e.target.value})} /></label></div>
        <div><label>CSAT: <input type="number" step="0.1" value={form.csat} onChange={e => setForm({...form, csat: +e.target.value})} /></label></div>
        <button type="submit">Prever</button>
      </form>
      {result && (
        <div style={{ marginTop: '1rem', padding: '1rem', background: '#e9ecef' }}>
          <p>Probabilidade: {(result.probabilidade_reabertura * 100).toFixed(1)}%</p>
          <p>Risco: <strong>{result.risco}</strong></p>
        </div>
      )}
    </div>
  );
}