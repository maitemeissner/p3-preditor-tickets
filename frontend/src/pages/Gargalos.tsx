import { useEffect, useState } from 'react';
import { getGargalos } from '../api';

interface Gargalo {
  setor: string;
  quantidade: number;
  criticidade: string;
}

export default function Gargalos() {
  const [gargalos, setGargalos] = useState<Gargalo[]>([]);

  useEffect(() => {
    getGargalos().then(setGargalos).catch(console.error);
  }, []);

  return (
    <div>
      <h1>Gargalos por Setor</h1>
      <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
        {gargalos.map(g => (
          <div
            key={g.setor}
            style={{
              border: '1px solid #999',
              borderRadius: 8,
              padding: '1rem',
              background: g.criticidade === 'alta' ? '#fdd' : g.criticidade === 'media' ? '#ffd' : '#dfd',
              minWidth: 150,
            }}
          >
            <strong>{g.setor}</strong>
            <p>{g.quantidade} tickets</p>
            <small>Criticidade: {g.criticidade}</small>
          </div>
        ))}
      </div>
    </div>
  );
}
