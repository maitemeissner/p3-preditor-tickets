import { useEffect, useState } from 'react';
import { getRelatorioLGPD } from '../api';

interface Stats {
  total_tickets: number;
  tickets_negativos: number;
  taxa_negatividade: number;
  gargalos_por_setor: Record<string, number>;
}

export default function Dashboard() {
  const [stats, setStats] = useState<Stats | null>(null);

  useEffect(() => {
    getRelatorioLGPD().then(setStats).catch(console.error);
  }, []);

  if (!stats) return <p>Carregando dashboard...</p>;

  return (
    <div>
      <h1>Dashboard</h1>
      <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
        <Card label="Total de Tickets" value={stats.total_tickets} />
        <Card label="Tickets Negativos" value={stats.tickets_negativos} />
        <Card label="Taxa de Negatividade" value={`${(stats.taxa_negatividade * 100).toFixed(1)}%`} />
      </div>
      <h2>Gargalos por Setor</h2>
      <ul>
        {Object.entries(stats.gargalos_por_setor).map(([setor, qtd]) => (
          <li key={setor}>{setor}: {qtd} tickets</li>
        ))}
      </ul>
    </div>
  );
}

function Card({ label, value }: { label: string; value: string | number }) {
  return (
    <div style={{ border: '1px solid #ccc', borderRadius: 8, padding: '1rem', minWidth: 180 }}>
      <strong>{label}</strong>
      <p style={{ fontSize: '1.5rem', margin: '0.5rem 0' }}>{value}</p>
    </div>
  );
}
