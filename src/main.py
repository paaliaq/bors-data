import os
import pandas as pd

import datacollection as dc
import mongodbconnection as mdbc


def main():
    # Global variables
    current_wd = os.getcwd()
    f = open("./apikey.txt", "r")
    apikey = f.read()

    # Collect ticker metadata
    names, url_name, instrument, ticker, sector_id, market_id, country_id, ins_id \
        = dc.collect_ticker_metadata(apikey, current_wd)

    tickers = pd.read_csv(filepath_or_buffer=current_wd + "/data/Tickers.csv")

    # Retrieve all ticker data into memory
    dc.download_all_data(read_tickers=tickers, ticker_list=ticker, ins_id=ins_id,
                         apikey=apikey, current_wd=current_wd)

    read_data = dc.read_files_from_disk(ticker_list=tickers, current_wd=current_wd)

    # Upload data to database
    mdbc.upload_to_mongo(tickers, read_data)


if __name__ == "__main__":
    main()
