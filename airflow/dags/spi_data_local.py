from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

###############################################
# Parameters
###############################################
spark_app_name = "spi_write_to_hdfs"
spark_main = "/usr/local/spark/app/main.py"
spark_standalone_conn_id = "spark_standalone"
now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    "spi_data_local",
    default_args=default_args,
    schedule_interval=timedelta(1)
)

start = DummyOperator(task_id="start", dag=dag)

spark_job = SparkSubmitOperator(
    conn_id=spark_standalone_conn_id,
    task_id="spark_to_hdfs",
    application=spark_main,
    name=spark_app_name,
    verbose=True,
    conf={"spark.hadoop.fs.defaultFS": "hdfs://namenode:8020"},
    dag=dag)

end = DummyOperator(task_id="end", dag=dag)

start >> spark_job >> end
