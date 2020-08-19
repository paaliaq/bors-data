import pymongo

def upload_to_mongo(tickers, dataset):
    f = open("./mongodbkey.txt", "r")
    mongodbkey = f.read()

    client = pymongo.MongoClient(mongodbkey)
    collection = client["bors-data"]["financials"]
    collection.delete_many({})  # Clear database as inserting each entry is faster than finding and updating

    i = 0
    lengthticks = len(tickers)
    for ticker_index in range(0, lengthticks):
        new_entry = {"Ticker": tickers["Ticker"][ticker_index],
                     "Name": tickers["Name"][ticker_index],
                     "Sector": tickers["Sector"][ticker_index],
                     "Market": tickers["Market"][ticker_index],
                     "Country": tickers["Country"][ticker_index],
                     "Daily data": dataset[tickers["Ticker"][ticker_index] + "_price"].to_dict('records'),
                     "Quarterly data": dataset[tickers["Ticker"][ticker_index] + "_quarter"].to_dict('records'),
                     "Yearly data": dataset[tickers["Ticker"][ticker_index] + "_year"].to_dict('records')}
        try:
            # collection.replace_one({"Ticker": tickers["Ticker"][ticker_index]}, new_entry, True)
            collection.insert_one(new_entry)
            print("Ticker " + str(i) + " of " + str(lengthticks) + " ,  " + tickers["Ticker"][ticker_index] + " Updated")
        except Exception:
            print("Ticker " + str(i) + " of " + str(lengthticks) + " ,  " + tickers["Ticker"][ticker_index] + ", not able to update")
        i += 1

