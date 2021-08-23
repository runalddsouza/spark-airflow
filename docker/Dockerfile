FROM apache/airflow:2.1.2-python3.7

USER root

# Postgres
RUN apt-get update \
  && apt-get -y install libaio-dev \
  && apt-get install postgresql-client

# OpenJdk for spark-submit
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-11-jdk;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow
# PySpark
RUN pip install pyspark==3.1.1
RUN pip install apache-airflow-providers-apache-spark==2.0.0

RUN mkdir extra
COPY airflow/init.sh ./init.sh
COPY airflow/airflow.cfg ./airflow.cfg
COPY airflow/setup_connection.py ./setup_connection.py

USER root
RUN chmod +x ./init.sh

USER airflow
EXPOSE 8080 5555 8793

ENTRYPOINT ["./init.sh"]
