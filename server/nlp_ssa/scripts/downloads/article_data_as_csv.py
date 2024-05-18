import csv
import logging
import os
from sqlalchemy import select

from config import configure_logging
from db import db_session
from models.article_data import ArticleDataDB


configure_logging(app_name="stash_db")
logger = logging.getLogger(__name__)
raw_window_width, _ = os.get_terminal_size()
window_width = (
    raw_window_width - 100
)  # to account for characters added by logging handlers


def print_section_start(entity_name: str):
    logger.info(f" 'Getting `{entity_name}` records...' ".center(window_width, "="))


def print_section_end(entity_name: str, entity_count: int):
    logger.info(
        f" 'Done retrieving `{entity_name}` records! Total: {entity_count}' ".center(
            window_width, "="
        )
    )


def download_article_data_as_csv():
    with open(
        "nlp_ssa/scripts/downloads/files/article_data.csv", "w", newline=""
    ) as csvfile:
        fieldnames = [c.key for c in ArticleDataDB.__table__.columns]

        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        print_section_start("article_data")
        total_count = 0
        article_data_records_stmt = select(ArticleDataDB).execution_options(
            yield_per=20
        )
        article_data = []
        for i, data_row in enumerate(
            db_session.scalars(article_data_records_stmt), start=1
        ):
            ad = data_row.__dict__

            try:
                del ad["_sa_instance_state"]
            except KeyError:
                pass

            article_data.append(ad)

            logger.info(f" Writing '{i}' rows... ".center(window_width, "="))
            csv_writer.writerow(ad)
            total_count = i

        print_section_end("article_data", total_count)


if __name__ == "__main__":
    download_article_data_as_csv()
