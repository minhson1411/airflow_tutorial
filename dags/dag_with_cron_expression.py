from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'minhson',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
    
}
# Tue-Fri from tue to fri
# Tue, Fri tue and fri

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_v03",
    start_date=datetime(2023, 11, 15),
    schedule_interval='0 3 * * Tue'
    
    ) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )
    task1