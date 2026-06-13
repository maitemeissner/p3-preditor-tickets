import { useState, useEffect } from 'react';

export default function Gargalos() {
  const [gargalos, setGargalos] = useState<any[]>([]);

  useEffect(() => {
    fetch('/api/gargalos')
      .then(r => r.json())
      .then(d => setGargalos(d.gargalos || []))
      .catch(() => {});
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Diagnóstico de Gargalos</h1>
      <table border={1} cellPadding={8} style={{ borderCollapse: 'collapse' }}>
        <thead><tr><th>Canal</th><th>TMA Médio</th><th>Total Tickets</th><th>Reopening Rate</th></tr></thead>
        <tbody>
          {gargalos.map((g: any, i: number) => (
            <tr key={i}>
              <td>{g.canal}</td>
              <td>{g.avg_tma?.toFixed(0)} min</td>
              <td>{g.total}</td>
              <td>{(g.reopen_rate * 100).toFixed(1)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}