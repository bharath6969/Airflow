from airflow import DAG
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator

def vishnu():
    print("love")

with DAG('my_dag', start_date=datetime(2023, 4, 12), schedule_interval="@hourly", catchup=False) as dag:
    t1= DummyOperator(task_id='start')
    t2 = BashOperator(
         task_id = "bash_task",
         bash_command="echo 1"
     )
    t3 = PythonOperator(
         task_id= "py_task",
         python_callable= vishnu
     )
    t4= DummyOperator(task_id='end')

t1>>t2>>t3>>t4
