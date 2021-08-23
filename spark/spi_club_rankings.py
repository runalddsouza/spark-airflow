from spi_csv import SpiCsv


class SpiClubRankWriteJob(SpiCsv):

    def __init__(self, config):
        super().__init__(config, "global_rankings")

    def partition_cols(self) -> list:
        return ["league"]
