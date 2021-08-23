from abc import ABC

import pandas as pd
from pyspark.sql import DataFrame

from write_job import WriteJob


class SpiCsv(WriteJob, ABC):

    def __init__(self, config, spi_type):
        super().__init__(config)
        self.csv_url = config["spi"][spi_type]["url"]
        self.table = config["spi"][spi_type]["name"]

    def load_df(self) -> DataFrame:
        return self.spark.createDataFrame(pd.read_csv(self.csv_url))

    def table_name(self) -> str:
        return self.table
