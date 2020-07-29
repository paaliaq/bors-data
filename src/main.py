import os
import pandas as pd

import src.datacollection as dc
import src.mongodbconnection as mdbc

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
    dc.download_all_data(read_tickers=tickers, ticker_list=ticker, ins_id=ins_id,
                         apikey=apikey, current_wd=current_wd)

    readData = dc.read_files_from_disk(ticker_list=tickers, current_wd=current_wd)

    mdbc.upload_to_mongo(tickers, readData)


# TODO add upload to mongoDB 
if __name__ == "__main__":
    main()

