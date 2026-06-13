import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE,
  timeout: 30000,
});

export async function preverTicket(ticket: Record<string, unknown>) {
  const { data } = await api.post('/prever', ticket);
  return data;
}

export async function preverBatch(file: File) {
  const form = new FormData();
  form.append('file', file);
  const { data } = await api.post('/prever/batch', form);
  return data;
}

export async function getGargalos() {
  const { data } = await api.get('/gargalos');
  return data;
}

export async function getRelatorioLGPD() {
  const { data } = await api.get('/relatorio-lgpd');
  return data;
}

export async function treinarModelo() {
  const { data } = await api.post('/treinar');
  return data;
}

export default api;
