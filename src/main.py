import os
import pandas as pd
import json
import sys

import datacollection as dc
import mongodbconnection as mdbc


def main():

    # Get config path
    if len(sys.argv[1:]) >= 1:
        config_name = sys.argv[1]
    else:
        config_name = "config.dev.json"

    # Extract variables from config
    with open(os.path.join(os.path.dirname(__file__), config_name)) as config_file:
        config = json.load(config_file)

    # Global variables
    current_wd = os.getcwd()

    # Collect ticker metadata
    names, url_name, instrument, ticker, sector_id, market_id, country_id, ins_id \
        = dc.collect_ticker_metadata(config["BORSDATA_KEY"], current_wd)

    tickers = pd.read_csv(filepath_or_buffer=current_wd + "/data/Tickers.csv")

    # If test take subset
    if config["TEST_MODE"] == "yes":
        print("Test mode set, using subset")
        tickers = tickers.iloc[0:50]
        ticker = ticker[0:50]

    # Retrieve all ticker data into disk from download
    dc.download_all_data(read_tickers=tickers, ticker_list=ticker, ins_id=ins_id,
                         apikey=config["BORSDATA_KEY"], current_wd=current_wd)

    i = 0
    for ticker_iter in tickers["Ticker"]:
        print("Uploading ticker:", ticker_iter, ", ", i, "of", len(tickers["Ticker"]))
        i += 1
        yearly, quarterly, daily = dc.read_csv_from_disk(ticker_iter, current_wd)  # Ticker, Sector or Market

        # Upload data to database
        mdbc.upload_to_mongo(ticker_name=ticker_iter, inserted_data=yearly.to_dict('records'),
                             mongodbkey=config["MONGODB_KEY"], mongodbDB=config["MONGODB_DATABASE_YEARLY"])

        mdbc.upload_to_mongo(ticker_name=ticker_iter, inserted_data=quarterly.to_dict('records'),
                             mongodbkey=config["MONGODB_KEY"], mongodbDB=config["MONGODB_DATABASE_QUARTERLY"])

        mdbc.upload_to_mongo(ticker_name=ticker_iter, inserted_data=daily.to_dict('records'),
                             mongodbkey=config["MONGODB_KEY"], mongodbDB=config["MONGODB_DATABASE_DAILY"])


if __name__ == "__main__":
    main()
