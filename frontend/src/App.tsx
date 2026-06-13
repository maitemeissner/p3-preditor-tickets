import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Previsao from './pages/Previsao';
import Gargalos from './pages/Gargalos';

function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: '1rem', background: '#f8f9fa', display: 'flex', gap: '1rem' }}>
        <Link to="/">Dashboard</Link>
        <Link to="/prever">Prever Ticket</Link>
        <Link to="/gargalos">Gargalos</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/prever" element={<Previsao />} />
        <Route path="/gargalos" element={<Gargalos />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;