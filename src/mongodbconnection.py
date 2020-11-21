import pymongo

def upload_to_mongo(ticker_name, inserted_data, mongodbkey, mongodbDB):
    """
    Upload data in cache to mongoDB.
    :type ticker_name: string
    :type inserted_data: Pandas DataFrames
    :type mongodbkey: str
    :type mongodbDB: str
    """

    print("test 1")

    db = pymongo.MongoClient(mongodbkey)[mongodbDB]

    collection = db[ticker_name]

    try:
        db.create_collection(ticker_name)
    except Exception:
        print("Collection creation failed failed for ", ticker_name)

    try:
        collection.delete_many({})  # Clear database as inserting each entry is faster than finding and updating
    except Exception:
        print("Delete failed for ", ticker_name)

    try:
        collection.insert_many(inserted_data)
    except Exception:
        print("Insert failed for ", ticker_name)