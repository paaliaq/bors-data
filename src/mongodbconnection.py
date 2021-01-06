"""Used for uploading ticker data from disk to mongoDB."""
import pymongo
import pandas as pd


def upload_to_mongo(
    ticker_name: str, inserted_data: pd.DataFrame, mongodbkey: str, mongodbDB: str
) -> None:
    """Function used for uploading ticker from disk to mongoDB.

    Requires Ticker/collection name, inserted data and database with connection details.
    as input.
    """
    db = pymongo.MongoClient(mongodbkey)[mongodbDB]

    collection = db[ticker_name]

    try:
        db.create_collection(ticker_name)
    except Exception:
        print("Collection already exists, ", ticker_name)

    try:
        collection.delete_many({})  # Clear database, faster than finding and updating
    except Exception:
        print("Delete failed for ", ticker_name)

    try:
        collection.insert_many(inserted_data)
    except Exception:
        print("Insert failed for ", ticker_name)
