import os
import pandas as pd

import src.datacollection as dc


def main():
    # Global variables
    current_wd = os.getcwd()
    f = open("./src/apikey.txt", "r")
    apikey = f.read()

    # Collect ticker metadata
    names, url_name, instrument, ticker, sector_id, market_id, country_id, ins_id \
        = dc.collect_ticker_metadata(apikey, current_wd)

    tickers = pd.read_csv(filepath_or_buffer=current_wd + "/data/Tickers.csv")

    # Fetch all ticker data
    dc.download_all_data(tickerReadSet=tickers, ticker_list=ticker, insId_list=ins_id,
                         apiKey=apikey, currentWD=current_wd)

    readData = dc.read_files_from_disk(ticker_list=tickers)

    upload_to_mongo(names, ticker, sector_id, market_id, country_id, readData)


# TODO add upload to mongoDB 
if __name__ == "__main__":
    main()

