from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

dag = DAG()

task1 = BashOperator(
    task_id='',
    bash_command='',
    retries='',
    dag=dag)
