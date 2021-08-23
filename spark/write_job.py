import time
from abc import abstractmethod

from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql import functions as f

from spark_job import SparkJob


class WriteJob(SparkJob):

    def __init__(self, config):
        super().__init__()
        self.output_prefix = config["spark"]["output-prefix"]
        self.app_name = config["spark"]["app-name"]
        self.processed_date_col = "processed_date"

    def init_spark(self) -> SparkSession:
        return SparkSession.builder.appName(self.app_name).getOrCreate()

    def execute(self) -> None:
        self._write_parquet(self._with_processed_date(self.load_df()))

    def _write_parquet(self, df):
        df.write.mode("append").partitionBy(self.processed_date_col, *self.partition_cols()).parquet(
            self.output_prefix + "/" + self.table_name())

    def _with_processed_date(self, df) -> DataFrame:
        dt = round(time.time() * 1000)
        return df.withColumn(self.processed_date_col, f.lit(dt))

    @abstractmethod
    def load_df(self) -> DataFrame:
        pass

    @abstractmethod
    def partition_cols(self) -> list:
        pass

    @abstractmethod
    def table_name(self) -> str:
        pass
