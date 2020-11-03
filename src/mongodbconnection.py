import pymongo


def upload_to_mongo(tickers, dataset, mongodbkey, mongodbDB, mongodbColl):
    """
    Upload data in cache to mongoDB.
    :type tickers: Pandas DataFrame
    :type dataset: Dictionaries of Pandas DataFrames
    :type mongodbkey: str
    :type mongodbDB: str
    :type mongodbColl: str
    """

    collection = pymongo.MongoClient(mongodbkey)[mongodbDB][mongodbColl]

    collection.delete_many({})  # Clear database as inserting each entry is faster than finding and updating

    i = 0
    lengthticks = len(tickers)
    for ticker_index in range(0, lengthticks):
        new_entry = {"Ticker": tickers["Ticker"][ticker_index],
                     "Name": tickers["Name"][ticker_index],
                     "Sector": tickers["Sector"][ticker_index],
                     "Market": tickers["Market"][ticker_index],
                     "Country": tickers["Country"][ticker_index],
                     "Daily_data": dataset[tickers["Ticker"][ticker_index] + "_price"].to_dict('records'),
                     "Quarterly_data": dataset[tickers["Ticker"][ticker_index] + "_quarter"].to_dict('records'),
                     "Yearly_data": dataset[tickers["Ticker"][ticker_index] + "_year"].to_dict('records')}
        try:
            collection.insert_one(new_entry)
            print(
                "Ticker " + str(i) + " of " + str(lengthticks) + " ,  " + tickers["Ticker"][ticker_index] + " Updated")
        except Exception:
            print("Ticker " + str(i) + " of " + str(lengthticks) + " ,  " + tickers["Ticker"][
                ticker_index] + ", not able to update")
        i += 1
