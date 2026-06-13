from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = "data/database.sqlite"

def job_retreino():
    print(f"[{datetime.now()}] Iniciando retreino agendado...")
    try:
        from ml.treino import treinar
        acc = treinar()
        print(f"[{datetime.now()}] Retreino concluído. Acurácia: {acc:.2%}")
    except Exception as e:
        print(f"[{datetime.now()}] Erro no retreino: {e}")

def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_retreino, 'interval', hours=24, id='retreino_diario')
    scheduler.start()
    print("Scheduler iniciado. Retreino automático a cada 24h.")