# spark-airflow

Simple Docker setup for Airflow with Spark and Hadoop 

| App| Version |
| --- | --- |
| Airflow | 2.1.2 |
| Spark/PySpark | 3.1.1 |
| Hadoop | 3.2.1 |

The pipeline submits a spark application to a standalone spark cluster which creates an output on HDFS

<b>Docker:</b>
- Airflow
- Hadoop: NameNode and DataNode
- Spark Standalone: Master with 2 worker nodes
- Postgres

<b>Steps to run:</b>
- Clone repository
- Run: `cd docker`
- Start services: `docker-compose up`
- Login Airflow on http://localhost:8080
  - user: airflow
  - password: airflow

Access WebUI for:
- Namenode: http://localhost:9870
- Spark Standalone: http://localhost:4040

