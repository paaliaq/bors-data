"""Main file for the whole collection and uploading sequence."""
import json
import logging
import os
import sys

import alnair
import pandas as pd

import datacollection as dc
import mongodbconnection as mdbc

logger = logging.getLogger(__name__)


def main() -> None:
    """Main function running the whole collection and uploading sequence."""
    if len(sys.argv[1:]) >= 1:  # Get config path
        config_name = sys.argv[1]
    else:
        config_name = "config.dev.json"

        # Extract variables from config
    with open(os.path.join(os.path.dirname(__file__), config_name)) as config_file:
        config = json.load(config_file)

    # Initialize logging services
    alnair.initialize("bors-data-data-fetcher")
    alnair.attach_console_handler()
    alnair.attach_mattermost_handler(
        config["MATTERMOST"], channel="logging", log_level=logging.ERROR
    )
    alnair.attach_mongodb_handler(
        connection_string=config["MONGODB_KEY"], log_level=logging.WARNING
    )

    alnair.start()

    logger.info("Database update started.")

    # Import path
    current_wd = os.getcwd()

    # Collect ticker metadata
    (
        names,
        url_name,
        instrument,
        ticker,
        sector_id,
        market_id,
        country_id,
        ins_id,
    ) = dc.collect_ticker_metadata(config["BORSDATA_KEY"], current_wd)

    tickers = pd.read_csv(filepath_or_buffer=current_wd + "/data/Tickers.csv")

    # If test take subset
    if config["TEST_MODE"] == "yes":
        logger.info(msg="Test mode set, using subset")
        tickers = tickers.iloc[0:10]
        ticker = ticker[0:10]

    # Retrieve all ticker data into disk from download
    dc.download_all_data(
        read_tickers=tickers,
        ticker_list=ticker,
        ins_id=ins_id,
        apikey=config["BORSDATA_KEY"],
        current_wd=current_wd,
    )

    i = 0
    for ticker_iter in tickers["Ticker"]:
        logger.info(
            msg="Uploading ticker:"
            + str(ticker_iter)
            + ", "
            + str(i)
            + "of"
            + str(len(tickers["Ticker"]))
        )
        i += 1
        yearly, quarterly, daily = dc.read_csv_from_disk(ticker_iter, current_wd)

        # Upload data to database
        mdbc.upload_to_mongo(
            ticker_name=ticker_iter,
            inserted_data=yearly.to_dict("records"),
            mongodb_key=config["MONGODB_KEY"],
            mongodb=config["MONGODB_DATABASE_YEARLY"],
        )

        mdbc.upload_to_mongo(
            ticker_name=ticker_iter,
            inserted_data=quarterly.to_dict("records"),
            mongodb_key=config["MONGODB_KEY"],
            mongodb=config["MONGODB_DATABASE_QUARTERLY"],
        )

        mdbc.upload_to_mongo(
            ticker_name=ticker_iter,
            inserted_data=daily.to_dict("records"),
            mongodb_key=config["MONGODB_KEY"],
            mongodb=config["MONGODB_DATABASE_DAILY"],
        )

    logger.info("Database update finished.")

    alnair.stop()


if __name__ == "__main__":
    main()
