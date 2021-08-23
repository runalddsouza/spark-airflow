from spi_csv import SpiCsv


class SpiIntlRankWriteJob(SpiCsv):

    def __init__(self, config):
        super().__init__(config, "global_rankings_intl")

    def partition_cols(self) -> list:
        return ["confed"]
