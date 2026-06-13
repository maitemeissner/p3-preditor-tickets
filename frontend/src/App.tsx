import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Previsao from './pages/Previsao';
import Gargalos from './pages/Gargalos';

function App() {
  return (
    <BrowserRouter>
      <nav style={{ display: 'flex', gap: '1rem', padding: '1rem', background: '#1a1a2e', color: '#eee' }}>
        <h2 style={{ margin: 0 }}>P3 - Preditor de Tickets</h2>
        <NavLink to="/" style={{ color: '#eee' }}>Dashboard</NavLink>
        <NavLink to="/previsao" style={{ color: '#eee' }}>Previsão</NavLink>
        <NavLink to="/gargalos" style={{ color: '#eee' }}>Gargalos</NavLink>
      </nav>
      <main style={{ padding: '1rem' }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/previsao" element={<Previsao />} />
          <Route path="/gargalos" element={<Gargalos />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
