"""Used for uploading ticker data from disk to mongoDB."""
import pymongo
import pandas as pd

import logging

logger = logging.getLogger(__name__)


def upload_to_mongo(
    ticker_name: str, inserted_data: pd.DataFrame, mongodb_key: str, mongodb: str
) -> None:
    """Function used for uploading ticker from disk to mongoDB.

    Requires Ticker/collection name, inserted data and database with connection details.
    as input.
    """
    db = pymongo.MongoClient(mongodb_key)[mongodb]

    collection = db[ticker_name]

    try:
        collection.delete_many({})  # Clear database, faster than finding and updating
        logger.info(msg=str(ticker_name + " collection cleaned successfully."))
    except Exception:
        logger.error(msg=str(ticker_name + " collection clean failed."))

    try:
        collection.insert_many(inserted_data)
        logger.info(msg=str(ticker_name + " inserted successfully."))
    except Exception:
        logger.error(msg=str(ticker_name + "insertion failed."))
