def instrument_dictionary(json_request):
    """
    Decodes the json request and returns separate lists.

    :type json_request: http-request
    """
    # Create list of tickers with additional data
    names = []
    url = []
    instrument = []
    ticker = []
    sector = []
    market = []
    country = []
    ins_id = []

    for tickIterator in json_request["instruments"]:
        temp1 = tickIterator['name']
        temp2 = tickIterator['urlName']
        temp3 = tickIterator['instrument']
        temp4 = tickIterator['ticker']
        temp5 = tickIterator['sectorId']
        temp6 = tickIterator['marketId']
        temp7 = tickIterator['countryId']
        temp8 = tickIterator['insId']
        names.append(temp1)
        url.append(temp2)
        instrument.append(temp3)
        ticker.append(temp4)
        sector.append(temp5)
        market.append(temp6)
        country.append(temp7)
        ins_id.append(temp8)

    return names, url, instrument, ticker, sector, market, country, ins_id


def id_conv(ticker_list: str, ticker_name: str, ins_id: str):
    index_temp = ticker_list.index(ticker_name)
    return str(ins_id[index_temp])


def get_country(id: str, countries: list):
    for item in countries:
        if item['id'] == id:
            break
    return item['name']


def get_market(id: str, markets: list):
    for item in markets:
        if item['id'] == id:
            break
    return item['name']


def get_sector(id: str, sectors: list):
    for item in sectors:
        if item['id'] == id:
            break
    return item['name']
