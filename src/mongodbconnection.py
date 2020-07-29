import pymongo


def upload_to_mongo(tickers, dataset):
    # create new dictionary
    f = open("./src/mongodbkey.txt", "r")
    mongodbkey = f.read()

    client = pymongo.MongoClient(mongodbkey)
    collection = client["bors-data"]["financials"]



    for ticker_index in range(0,1):
        # TODO MAKE SURE REPLACE
        new_entry = {"Ticker": tickers["Ticker"][ticker_index],
                     "Name": tickers["Name"][ticker_index],
                     "Sector": tickers["Sector"][ticker_index],
                     "Market": tickers["Market"][ticker_index],
                     "Country": tickers["Country"][ticker_index],
                     "Daily data": dataset[tickers["Ticker"][ticker_index] + "_price"],
                     "Quarterly data": dataset[tickers["Ticker"][ticker_index] + "_quarter"],
                     "Yearly data": dataset[tickers["Ticker"][ticker_index] + "_year"]}

        collection.insert_one(new_entry)


