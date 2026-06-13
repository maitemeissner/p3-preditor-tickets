import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/gargalos')
      .then(r => r.json())
      .then(d => { setStats(d); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Dashboard — Preditor de Tickets</h1>
      {loading && <p>Carregando...</p>}
      {stats && (
        <pre style={{ background: '#f0f0f0', padding: '1rem' }}>
          {JSON.stringify(stats, null, 2)}
        </pre>
      )}
    </div>
  );
}