import pymongo

def upload_to_mongo(ticker_name, inserted_data, mongodbkey, mongodbDB):
    """
    Upload data in cache to mongoDB.
    :type ticker_name: string
    :type inserted_data: Pandas DataFrames
    :type mongodbkey: str
    :type mongodbDB: str
    """

    db = pymongo.MongoClient(mongodbkey)[mongodbDB]

    collection = db[ticker_name]

    collection.delete_many({})  # Clear database as inserting each entry is faster than finding and updating

    collection.insert_many(inserted_data)



