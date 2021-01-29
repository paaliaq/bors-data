"""Utility functions used in datacollection and main."""
import logging
from typing import Tuple

logger = logging.getLogger(__name__)


def instrument_dictionary(
    json_request: dict,
) -> Tuple[list, list, list, list, list, list, list, list]:
    """Decodes the json request and returns each item as separate lists."""
    # Create list of tickers with additional data
    names = []
    urls = []
    instruments = []
    tickers = []
    sectors = []
    markets = []
    countries = []
    ins_ids = []

    for tick_iterator in json_request["instruments"]:
        try:
            name = tick_iterator["name"]
            url = tick_iterator["urlName"]
            instrument = tick_iterator["instrument"]
            ticker = tick_iterator["ticker"]
            sector_id = tick_iterator["sectorId"]
            market_id = tick_iterator["marketId"]
            country_id = tick_iterator["countryId"]
            ins_id = tick_iterator["insId"]
            names.append(name)
            urls.append(url)
            instruments.append(instrument)
            tickers.append(ticker)
            sectors.append(sector_id)
            markets.append(market_id)
            countries.append(country_id)
            ins_ids.append(ins_id)
            logger.info(msg=str(ticker) + "json decoded.")
        except Exception:
            logger.error(msg=str(ticker) + "json decode failed.")

    return names, urls, instruments, tickers, sectors, markets, countries, ins_ids


def id_conv(ticker_list: list, ticker_name: str, ins_id: list) -> str:
    """Return id from ticker name and list of tickers."""
    try:
        index_temp = ticker_list.index(ticker_name)
        logger.info(msg=str(ticker_name + "id_conv succeeded."))
    except Exception:
        logger.error(msg=str(ticker_name + "id_conv failed."))

    return str(ins_id[index_temp])


def get_country(id: int, countries: list) -> str:
    """Return country for one ticker using id."""
    try:
        for item in countries:
            if item["id"] == id:
                break
        logger.info(msg=str(id) + "get_country succeeded.")
    except Exception:
        logger.error(msg=str(id) + "get_country failed.")

    return item["name"]


def get_market(id: int, markets: list) -> str:
    """Return market for one ticker using id."""
    try:
        for item in markets:
            if item["id"] == id:
                break
        logger.info(msg=str(id) + "get_market succeeded.")
    except Exception:
        logger.error(msg=str(id) + "get_market failed.")

    return item["name"]


def get_sector(id: int, sectors: list) -> str:
    """Return sector for one ticker using id."""
    try:
        for item in sectors:
            if item["id"] == id:
                break
        logger.info(msg=str(id) + "get_sector succeeded.")
    except Exception:
        logger.error(msg=str(id) + "get_sector failed.")

    return item["name"]
