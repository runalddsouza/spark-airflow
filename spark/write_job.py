from abc import abstractmethod

from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

from spark_job import SparkJob


class WriteJob(SparkJob):

    def __init__(self, config):
        super().__init__()
        self.output_prefix = config["spark"]["output-prefix"]
        self.app_name = config["spark"]["app-name"]
        self.master = config["spark"]["master"]

    def init_spark(self) -> SparkSession:
        return SparkSession.builder.appName(self.app_name).master(self.master).getOrCreate()

    def execute(self) -> None:
        self._write_parquet()

    def _write_parquet(self):
        self.load_df().write.partitionBy(*self.partition_cols()).parquet(self.output_prefix + "/" + self.table_name())

    @abstractmethod
    def load_df(self) -> DataFrame:
        pass

    @abstractmethod
    def partition_cols(self) -> list:
        pass

    @abstractmethod
    def table_name(self) -> str:
        pass
