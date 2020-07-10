import requests
import os
from common import id_conv
from common import instrument_dictionary
from common import get_sector
from common import get_market
from common import get_country
from time import sleep
import numpy as np
import pandas as pd


class CollectTickerData:
    def __init__(self, ticker_name, ticker_list, ins_id, apikey):
        self.name = ticker_name

        sleep(0.5)  # Due to data api time constraint

        """Collect Price data """
        temp_price_data = requests.get("https://apiservice.borsdata.se/v1/instruments/" + id_conv(
            ticker_name, ticker_list, ins_id) + "/stockprices?authKey=" + apikey).json()
        ticker_price_data = []

        for item in temp_price_data["stockPricesList"]:
            temp_price = [item["d"], item["c"], item["o"], item["h"], item["l"], item["v"]]
            ticker_price_data.append(temp_price)
            
        ticker_price_data_frame = pd.DataFrame(data=ticker_price_data,
                                               columns=("Time", "Close", "Open", "High", "Low", "volume"))
        self.priceData = ticker_price_data_frame
        
        sleep(0.5)
        
        """ Year Data """
        temp_year = requests.get(
            "https://apiservice.borsdata.se/v1/instruments/" + id_conv(ticker_name, ticker_list, ins_id) +
            "/reports/year?authKey=" + apikey).json()
        
        year_data = []

        try:
            for item in temp_year["reports"]:
                year_temp = [item["report_End_Date"], item["revenues"], item["gross_Income"], item["operating_Income"],
                             item["profit_Before_Tax"], item["profit_To_Equity_Holders"], item["earnings_Per_Share"],
                             item["number_Of_Shares"], item["dividend"], item["intangible_Assets"],
                             item["tangible_Assets"], item["financial_Assets"], item["non_Current_Assets"],
                             item["cash_And_Equivalents"], item["current_Assets"], item["total_Assets"],
                             item["total_Equity"], item["non_Current_Liabilities"], item["current_Liabilities"],
                             item["total_Liabilities_And_Equity"], item["net_Debt"],
                             item["cash_Flow_From_Operating_Activities"], item["cash_Flow_From_Investing_Activities"],
                             item["cash_Flow_From_Financing_Activities"], item["cash_Flow_For_The_Year"],
                             item["free_Cash_Flow"], item["stock_Price_Average"], item["stock_Price_High"],
                             item["stock_Price_Low"]]
                year_data.append(year_temp)
                
            year_data_frame = pd.DataFrame(data=year_data,
                                           columns=("report_End_Date", "revenues", "gross_Income", "operating_Income",
                                                    "profit_Before_Tax", "profit_To_Equity_Holders",
                                                    "earnings_Per_Share",
                                                    "number_Of_Shares", "dividend", "intangible_Assets",
                                                    "tangible_Assets",
                                                    "financial_Assets", "non_Current_Assets", "cash_And_Equivalents",
                                                    "current_Assets", "total_Assets", "total_Equity",
                                                    "non_Current_Liabilities",
                                                    "current_Liabilities", "total_Liabilities_And_Equity", "net_Debt",
                                                    "cash_Flow_From_Operating_Activities",
                                                    "cash_Flow_From_Investing_Activities",
                                                    "cash_Flow_From_Financing_Activities", "cash_Flow_For_The_Year",
                                                    "free_Cash_Flow", "stock_Price_Average", "stock_Price_High",
                                                    "stock_Price_Low"))
            
            self.yearData = year_data_frame

            print("Year data read")
            
        except Exception:
            print("couldn't read year data")
            print(temp_year)
            
        sleep(0.5)

        """Quarter data"""
        temp_quarter = requests.get(
            "https://apiservice.borsdata.se/v1/instruments/" + id_conv(ticker_name, ticker_list, ins_id) +
            "/reports/quarter?authKey=" + apikey).json()
        
        quarter_data = []

        try:
            for item in temp_quarter["reports"]:
                quarter_temp = [item["report_End_Date"], item["revenues"], item["gross_Income"],
                                item["operating_Income"], item["profit_Before_Tax"], item["profit_To_Equity_Holders"],
                                item["earnings_Per_Share"], item["number_Of_Shares"], item["dividend"],
                                item["intangible_Assets"], item["tangible_Assets"], item["financial_Assets"],
                                item["non_Current_Assets"], item["cash_And_Equivalents"], item["current_Assets"],
                                item["total_Assets"], item["total_Equity"], item["non_Current_Liabilities"],
                                item["current_Liabilities"], item["total_Liabilities_And_Equity"], item["net_Debt"],
                                item["cash_Flow_From_Operating_Activities"],
                                item["cash_Flow_From_Investing_Activities"],
                                item["cash_Flow_From_Financing_Activities"], item["cash_Flow_For_The_Year"],
                                item["free_Cash_Flow"], item["stock_Price_Average"], item["stock_Price_High"],
                                item["stock_Price_Low"]]
                quarter_data.append(quarter_temp)
                
            quarter_data_frame = pd.DataFrame(data=quarter_data,
                                              columns=(
                                                  "report_End_Date", "revenues", "gross_Income", "operating_Income",
                                                  "profit_Before_Tax", "profit_To_Equity_Holders",
                                                  "earnings_Per_Share",
                                                  "number_Of_Shares", "dividend", "intangible_Assets",
                                                  "tangible_Assets",
                                                  "financial_Assets", "non_Current_Assets", "cash_And_Equivalents",
                                                  "current_Assets", "total_Assets", "total_Equity",
                                                  "non_Current_Liabilities",
                                                  "current_Liabilities", "total_Liabilities_And_Equity", "net_Debt",
                                                  "cash_Flow_From_Operating_Activities",
                                                  "cash_Flow_From_Investing_Activities",
                                                  "cash_Flow_From_Financing_Activities", "cash_Flow_For_The_Year",
                                                  "free_Cash_Flow", "stock_Price_Average", "stock_Price_High",
                                                  "stock_Price_Low"))
            print("Quarter data read")
            self.quarterData = quarter_data_frame
            
        except Exception:
            print("couldn't read quarter data")
            print(temp_quarter)


def read_files_from_disk(ticker_list,
                         selected_tickers=("ATRE", "AZN", "BILL"),
                         selected_sectors="all",
                         selected_countries="all",
                         selected_market="all"):  # Ticker, Sector or Market
    read_datasets = {}
    if selected_market == "all" and selected_countries == "all" and selected_sectors == "all" and \
            selected_tickers == "all":
        for ticker in ticker_list["Ticker"]:
            year = pd.read_csv(
                filepath_or_buffer="/Users/august/PycharmProjects/-BorsData-master/data/" + ticker + "/" + ticker +
                                   "Year" + ".csv")
            quarter = pd.read_csv(
                filepath_or_buffer="/Users/august/PycharmProjects/-BorsData-master/data/" + ticker + "/" + ticker +
                                   "Quarter" + ".csv")
            price = pd.read_csv(
                filepath_or_buffer="/Users/august/PycharmProjects/-BorsData-master/data/" + ticker + "/" + ticker +
                                   "price" + ".csv")

            read_datasets[ticker + "_year"] = year
            read_datasets[ticker + "_quarter"] = quarter
            read_datasets[ticker + "_price"] = price
    else:
        indeces_tickers = np.array(None)
        indeces_sectors = np.array(None)
        indeces_countries = np.array(None)
        indeces_markets = np.array(None)

        if selected_tickers != "all":
            ticker_bool = ticker_list['Ticker'].isin(selected_tickers)
            indeces_tickers = np.where(ticker_bool == True)

        if selected_sectors != "all":
            sectors_bool = ticker_list['Sector'].isin(selected_sectors)
            indeces_sectors = np.where(sectors_bool == True)

        if selected_countries != "all":
            countries_bool = ticker_list['Country'].isin(selected_countries)
            indeces_countries = np.where(countries_bool == True)

        if selected_market != "all":
            market_bool = ticker_list['Market'].isin(selected_market)
            indeces_markets = np.where(market_bool == True)

        # Todo this isn't working as expected, returns indecis and should give union

        kept_indices = np.concatenate((indeces_tickers, indeces_sectors, indeces_countries, indeces_markets), axis=None)
        kept_indices = kept_indices[kept_indices != np.array(None)]
        kept_indices = np.unique(kept_indices)
        ticker_subset_selected = ticker_list.iloc[kept_indices]

        for ticker in ticker_subset_selected["Ticker"]:
            year = pd.read_csv(
                filepath_or_buffer="/Users/august/PycharmProjects/-BorsData-master/data/" + ticker + "/" + ticker +
                                   "Year" + ".csv")
            quarter = pd.read_csv(
                filepath_or_buffer="/Users/august/PycharmProjects/-BorsData-master/data/" + ticker + "/" + ticker +
                                   "Quarter" + ".csv")
            price = pd.read_csv(
                filepath_or_buffer="/Users/august/PycharmProjects/-BorsData-master/data/" + ticker + "/" + ticker +
                                   "price" + ".csv")
            read_datasets[ticker + "_year"] = year
            read_datasets[ticker + "_quarter"] = quarter
            read_datasets[ticker + "_price"] = price
    return read_datasets


def collect_ticker_metadata(apikey, current_wd):
    request_instrument = requests.get("https://apiservice.borsdata.se/v1/instruments?authKey=" + apikey)
    data_instruments = request_instrument.json()

    sleep(1)

    request_countries = requests.get("https://apiservice.borsdata.se/v1/countries?authKey=" + apikey)
    data_countries = request_countries.json()

    sleep(1)

    request_markets = requests.get("https://apiservice.borsdata.se/v1/markets?authKey=" + apikey)
    data_markets = request_markets.json()

    sleep(1)

    request_sectors = requests.get("https://apiservice.borsdata.se/v1/sectors?authKey=" + apikey)
    data_sectors = request_sectors.json()

    sleep(1)

    names_list, url_name_list, instrument_list, ticker_list, sector_id_list, market_id_list, country_id_list, \
    ins_id_list = instrument_dictionary(data_instruments)  # Fetch all ticker data

    sector_id_list_transl = []
    for value in sector_id_list:
        temp = get_sector(value, data_sectors['sectors'])
        sector_id_list_transl.append(temp)

    market_id_list_transl = []
    for value in market_id_list:
        temp = get_market(value, data_markets['markets'])
        market_id_list_transl.append(temp)

    country_id_list_transl = []
    for value in country_id_list:
        temp = get_country(value, data_countries['countries'])
        country_id_list_transl.append(temp)

    try:
        os.mkdir(current_wd + "/data")
    except OSError:
        print("Folder already exists")

    pd.DataFrame(
        {'Name': names_list, 'Ticker': ticker_list, 'Sector': sector_id_list_transl, 'Market': market_id_list_transl,
         'Country': country_id_list_transl}).to_csv(path_or_buf=current_wd + "/data/Tickers.csv", sep=",",
                                                    index=False, decimal=".", encoding="utf-8")
    return names_list, url_name_list, instrument_list, ticker_list, sector_id_list, market_id_list, country_id_list, \
           ins_id_list


def download_all_data(read_tickers, ticker_list, ins_id, apikey, current_wd):
    tickers = []
    i = 0
    for item in read_tickers['Ticker']:
        i = i + 1
        print('Reading item', i, ",", item)
        try:
            tempObject = CollectTickerData(item, ticker_list=ticker_list, insId_list=ins_id, apiKey=apikey)
            tickers.append(tempObject)
        except Exception:
            print(item, 'failed collection')
        try:
            os.mkdir(current_wd + "/data/" + item)
            print(item, 'folder created')
        except Exception:
            print(item, 'folder already exists')
        try:
            tempObject.priceData.to_csv(path_or_buf=current_wd + "/data/" + item + "/" + item + "price.csv", sep=",",
                                        header=True, index=False, decimal=".")
            print(item, 'price data created')
        except Exception:
            print(item, "couldn't write price data")
        try:
            tempObject.quarterData.to_csv(path_or_buf=current_wd + "/data/" + item + "/" + item + "Quarter.csv", sep=","
                                          , header=True, index=False, decimal=".")
            print(item, 'quarter data created')
        except Exception:
            print(item, "couldn't write quarter data")
        try:
            tempObject.yearData.to_csv(path_or_buf=current_wd + "/data/" + item + "/" + item + "Year.csv", sep=",",
                                       header=True, index=False, decimal=".")
            print(item, 'year data created')
        except Exception:
            print(item, "couldn't write year data")
