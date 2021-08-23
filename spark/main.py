import json
from pathlib import Path

from write_job import WriteJob
from spi_club_rankings import SpiClubRankWriteJob
from spi_club_ratings import SpiRatingsWriteJob
from spi_intl_rankings import SpiIntlRankWriteJob


def run_job(job: WriteJob):
    job.run()


if __name__ == '__main__':
    # configuration
    with open(Path(__file__).parent / "resources/config.json") as config_file:
        config = json.load(config_file)

    run_job(SpiRatingsWriteJob(config))
    run_job(SpiClubRankWriteJob(config))
    run_job(SpiIntlRankWriteJob(config))
