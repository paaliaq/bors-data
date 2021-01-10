"""Utility functions used in datacollection and main."""
from typing import Tuple


def instrument_dictionary(
    json_request: dict,
) -> Tuple[list, list, list, list, list, list, list, list]:
    """Decodes the json request and returns each item as separate lists."""
    # Create list of tickers with additional data
    names = []
    url = []
    instrument = []
    ticker = []
    sector = []
    market = []
    country = []
    ins_id = []

    for tick_iterator in json_request["instruments"]:
        temp1 = tick_iterator["name"]
        temp2 = tick_iterator["urlName"]
        temp3 = tick_iterator["instrument"]
        temp4 = tick_iterator["ticker"]
        temp5 = tick_iterator["sectorId"]
        temp6 = tick_iterator["marketId"]
        temp7 = tick_iterator["countryId"]
        temp8 = tick_iterator["insId"]
        names.append(temp1)
        url.append(temp2)
        instrument.append(temp3)
        ticker.append(temp4)
        sector.append(temp5)
        market.append(temp6)
        country.append(temp7)
        ins_id.append(temp8)

    return names, url, instrument, ticker, sector, market, country, ins_id


def id_conv(ticker_list: list, ticker_name: str, ins_id: list) -> str:
    """Return id from ticker name and list of tickers."""
    index_temp = ticker_list.index(ticker_name)
    return str(ins_id[index_temp])


def get_country(id: str, countries: list) -> str:
    """Return country for one ticker using id."""
    for item in countries:
        if item["id"] == id:
            break
    return item["name"]


def get_market(id: str, markets: list) -> str:
    """Return market for one ticker using id."""
    for item in markets:
        if item["id"] == id:
            break
    return item["name"]


def get_sector(id: str, sectors: list) -> str:
    """Return sector for one ticker using id."""
    for item in sectors:
        if item["id"] == id:
            break
    return item["name"]
