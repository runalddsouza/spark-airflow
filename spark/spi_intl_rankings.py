from pyspark import SparkFiles
from pyspark.sql import DataFrame

from write_job import WriteJob


class SpiIntlRankWriteJob(WriteJob):

    def __init__(self, config):
        super().__init__(config)
        self.csv_dir = config["spi"]["global_rankings_intl"]["url"]
        self.csv_file = config["spi"]["global_rankings_intl"]["file"]
        self.table = config["spi"]["global_rankings_intl"]["name"]

    def load_df(self) -> DataFrame:
        self.spark.sparkContext.addFile(self.csv_dir + "/" + self.csv_file)
        return self.spark.read.csv(SparkFiles.get(self.csv_file), header=True)

    def partition_cols(self) -> list:
        return ["confed"]

    def table_name(self) -> str:
        return self.table
