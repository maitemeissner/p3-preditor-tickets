import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from apscheduler.schedulers.background import BackgroundScheduler
from ml.treino import treinar_modelo
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def job_treinar():
    logger.info("Iniciando treinamento agendado...")
    acuracia = treinar_modelo()
    logger.info(f"Treinamento concluído. Acurácia: {acuracia}")

def job_etl():
    logger.info("Executando ETL agendado...")

def iniciar():
    scheduler.add_job(job_treinar, "cron", hour=2, minute=0, id="treino_diario")
    scheduler.add_job(job_etl, "cron", hour=3, minute=0, id="etl_diario")
    scheduler.start()
    logger.info("Scheduler iniciado com jobs: treino_diario, etl_diario")

if __name__ == "__main__":
    iniciar()
