from spi_csv import SpiCsv


class SpiRatingsWriteJob(SpiCsv):

    def __init__(self, config):
        super().__init__(config, "matches_latest")

    def partition_cols(self) -> list:
        return ["season", "league"]
