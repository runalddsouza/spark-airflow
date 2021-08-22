from pyspark import SparkFiles
from pyspark.sql import DataFrame

from write_job import WriteJob


class SpiRatingsWriteJob(WriteJob):

    def __init__(self, config):
        super().__init__(config)
        self.csv_dir = config["spi"]["matches_latest"]["url"]
        self.csv_file = config["spi"]["matches_latest"]["file"]
        self.table = config["spi"]["matches_latest"]["name"]

    def load_df(self) -> DataFrame:
        self.spark.sparkContext.addFile(self.csv_dir + "/" + self.csv_file)
        return self.spark.read.csv(SparkFiles.get(self.csv_file), header=True)

    def partition_cols(self) -> list:
        return ["season", "league"]

    def table_name(self) -> str:
        return self.table
