from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random
import time

# ==========================================
# 1. Funções que simulam as regras de negócio
# ==========================================

def extrair_metadados_sql():
    """Simula uma query SQL no banco da Serasa buscando novas tentativas de onboarding."""
    print("Conectando ao banco de dados OCI...")
    time.sleep(2) # Simula o tempo de processamento
    transacoes = [
        {"id_cliente": "1001", "dispositivo": "mobile_android", "hora": "14:02"},
        {"id_cliente": "1002", "dispositivo": "desktop_web", "hora": "14:05"}
    ]
    print(f"Extração concluída: {len(transacoes)} novas transações encontradas.")
    return transacoes

def inferencia_modelo_cnn(**context):
    """Simula o carregamento do modelo.h5 e a pontuação das imagens."""
    print("Carregando pesos do modelo_liveness.h5...")
    time.sleep(3)
    
    # Gera scores simulados para as transações capturadas na tarefa anterior
    score_cliente_1 = random.uniform(0.0, 0.15) # Risco baixo (Authentic)
    score_cliente_2 = random.uniform(0.70, 0.99) # Risco alto (Spoofing detectado)
    
    resultados = {
        "1001": {"liveness_score": score_cliente_1, "status": "Aprovado"},
        "1002": {"liveness_score": score_cliente_2, "status": "Mesa_de_Fraude"}
    }
    
    print(f"Inferência concluída. Resultados: {resultados}")
    return resultados

def atualizar_decisao_banco(**context):
    """Simula o UPDATE no banco de dados com a decisão do modelo."""
    print("Gravando decisão final no banco de dados relacional...")
    time.sleep(1)
    print("Pipeline executado com sucesso. Trilha de auditoria gerada.")

# ==========================================
# 2. Configuração e Orquestração da DAG
# ==========================================

default_args = {
    'owner': 'cientista_dados',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Criando a DAG
with DAG(
    'serasa_liveness_detection_mvp',
    default_args=default_args,
    description='Pipeline de Validacao Facial (Anti-Spoofing)',
    schedule_interval=timedelta(minutes=15), # Rodaria a cada 15 min em produção
    catchup=False,
    tags=['serasa', 'fraude', 'biometria', 'cnn'],
) as dag:

    # Definindo as Tarefas (Tasks)
    task_extracao_sql = PythonOperator(
        task_id='extracao_metadados_sql',
        python_callable=extrair_metadados_sql,
    )

    task_inferencia = PythonOperator(
        task_id='inferencia_modelo_cnn',
        python_callable=inferencia_modelo_cnn,
    )

    task_update_sql = PythonOperator(
        task_id='atualizacao_decisao_banco',
        python_callable=atualizar_decisao_banco,
    )

    # Definindo a ordem de execução (Dependências)
    task_extracao_sql >> task_inferencia >> task_update_sql