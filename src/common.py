def instrumentDictionary(json_request):

    # Create list of tickers with additional data
    names = []
    url = []
    instrument = []
    ticker = []
    sector = []
    market = []
    country = []
    ins_Id = []

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
        ins_Id.append(temp8)

    return names, url, instrument, ticker, sector, market, country, ins_Id;


def idConv(ticker_name, ticker_list, ins_Id):
    indexTemp = ticker_list.index(ticker_name)
    return str(ins_Id[indexTemp])


def getCountry(id, countries):
    for item in countries:
        if item['id'] == id:
            break
    return item['name']


def getMarket(id, markets):
    for item in markets:
        if item['id'] == id:
            break
    return item['name']


def getSector(id, sectors):
    for item in sectors:
        if item['id'] == id:
            break
    return item['name']
