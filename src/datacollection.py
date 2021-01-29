"""Main file for the whole collection and uploading sequence."""
import requests
import os
from time import sleep
import logging

import pandas as pd

from typing import Tuple

from common import id_conv
from common import instrument_dictionary
from common import get_sector
from common import get_market
from common import get_country

logger = logging.getLogger(__name__)


class CollectTickerData:
    """Class process request into a pandas dataframe, for each ticker."""

    def __init__(self, ticker_name: str, ticker_list: list, ins_id: list, apikey: str):
        """Fetch all the data in initialization."""
        self.name = ticker_name

        sleep(0.5)  # Due to data api time constraint

        """Collect Price data """
        temp_price_data = requests.get(
            "https://apiservice.borsdata.se/v1/instruments/"
            + id_conv(ticker_list, ticker_name, ins_id)
            + "/stockprices?authKey="
            + apikey
        ).json()
        ticker_price_data = []
        try:
            for item in temp_price_data["stockPricesList"]:
                temp_price = [
                    item["d"],
                    item["c"],
                    item["o"],
                    item["h"],
                    item["l"],
                    item["v"],
                ]
                ticker_price_data.append(temp_price)

            ticker_price_data_frame = pd.DataFrame(
                data=ticker_price_data,
                columns=("Time", "Close", "Open", "High", "Low", "volume"),
            )
            self.priceData = ticker_price_data_frame

            logger.info(msg=str("Price data downloaded for stock " + ticker_name))

        except Exception:
            logger.error(
                msg=str("Couldn't download price data for stock " + ticker_name)
            )

        sleep(0.5)

        """ Year Data """
        temp_year = requests.get(
            "https://apiservice.borsdata.se/v1/instruments/"
            + id_conv(ticker_list, ticker_name, ins_id)
            + "/reports/year?authKey="
            + apikey
        ).json()

        year_data = []

        try:
            for item in temp_year["reports"]:
                year_temp = [
                    item["report_End_Date"],
                    item["revenues"],
                    item["gross_Income"],
                    item["operating_Income"],
                    item["profit_Before_Tax"],
                    item["profit_To_Equity_Holders"],
                    item["earnings_Per_Share"],
                    item["number_Of_Shares"],
                    item["dividend"],
                    item["intangible_Assets"],
                    item["tangible_Assets"],
                    item["financial_Assets"],
                    item["non_Current_Assets"],
                    item["cash_And_Equivalents"],
                    item["current_Assets"],
                    item["total_Assets"],
                    item["total_Equity"],
                    item["non_Current_Liabilities"],
                    item["current_Liabilities"],
                    item["total_Liabilities_And_Equity"],
                    item["net_Debt"],
                    item["cash_Flow_From_Operating_Activities"],
                    item["cash_Flow_From_Investing_Activities"],
                    item["cash_Flow_From_Financing_Activities"],
                    item["cash_Flow_For_The_Year"],
                    item["free_Cash_Flow"],
                    item["stock_Price_Average"],
                    item["stock_Price_High"],
                    item["stock_Price_Low"],
                ]
                year_data.append(year_temp)

            year_data_frame = pd.DataFrame(
                data=year_data,
                columns=(
                    "report_End_Date",
                    "revenues",
                    "gross_Income",
                    "operating_Income",
                    "profit_Before_Tax",
                    "profit_To_Equity_Holders",
                    "earnings_Per_Share",
                    "number_Of_Shares",
                    "dividend",
                    "intangible_Assets",
                    "tangible_Assets",
                    "financial_Assets",
                    "non_Current_Assets",
                    "cash_And_Equivalents",
                    "current_Assets",
                    "total_Assets",
                    "total_Equity",
                    "non_Current_Liabilities",
                    "current_Liabilities",
                    "total_Liabilities_And_Equity",
                    "net_Debt",
                    "cash_Flow_From_Operating_Activities",
                    "cash_Flow_From_Investing_Activities",
                    "cash_Flow_From_Financing_Activities",
                    "cash_Flow_For_The_Year",
                    "free_Cash_Flow",
                    "stock_Price_Average",
                    "stock_Price_High",
                    "stock_Price_Low",
                ),
            )

            self.yearData = year_data_frame

            logger.info(msg=str("Year data downloaded for stock " + ticker_name))

        except Exception:
            logger.error(
                msg=str("Couldn't download year data for stock " + ticker_name)
            )

        sleep(0.5)

        """Quarter data"""
        temp_quarter = requests.get(
            "https://apiservice.borsdata.se/v1/instruments/"
            + id_conv(ticker_list, ticker_name, ins_id)
            + "/reports/quarter?authKey="
            + apikey
        ).json()

        quarter_data = []

        try:
            for item in temp_quarter["reports"]:
                quarter_temp = [
                    item["report_End_Date"],
                    item["revenues"],
                    item["gross_Income"],
                    item["operating_Income"],
                    item["profit_Before_Tax"],
                    item["profit_To_Equity_Holders"],
                    item["earnings_Per_Share"],
                    item["number_Of_Shares"],
                    item["dividend"],
                    item["intangible_Assets"],
                    item["tangible_Assets"],
                    item["financial_Assets"],
                    item["non_Current_Assets"],
                    item["cash_And_Equivalents"],
                    item["current_Assets"],
                    item["total_Assets"],
                    item["total_Equity"],
                    item["non_Current_Liabilities"],
                    item["current_Liabilities"],
                    item["total_Liabilities_And_Equity"],
                    item["net_Debt"],
                    item["cash_Flow_From_Operating_Activities"],
                    item["cash_Flow_From_Investing_Activities"],
                    item["cash_Flow_From_Financing_Activities"],
                    item["cash_Flow_For_The_Year"],
                    item["free_Cash_Flow"],
                    item["stock_Price_Average"],
                    item["stock_Price_High"],
                    item["stock_Price_Low"],
                ]
                quarter_data.append(quarter_temp)

            quarter_data_frame = pd.DataFrame(
                data=quarter_data,
                columns=(
                    "report_End_Date",
                    "revenues",
                    "gross_Income",
                    "operating_Income",
                    "profit_Before_Tax",
                    "profit_To_Equity_Holders",
                    "earnings_Per_Share",
                    "number_Of_Shares",
                    "dividend",
                    "intangible_Assets",
                    "tangible_Assets",
                    "financial_Assets",
                    "non_Current_Assets",
                    "cash_And_Equivalents",
                    "current_Assets",
                    "total_Assets",
                    "total_Equity",
                    "non_Current_Liabilities",
                    "current_Liabilities",
                    "total_Liabilities_And_Equity",
                    "net_Debt",
                    "cash_Flow_From_Operating_Activities",
                    "cash_Flow_From_Investing_Activities",
                    "cash_Flow_From_Financing_Activities",
                    "cash_Flow_For_The_Year",
                    "free_Cash_Flow",
                    "stock_Price_Average",
                    "stock_Price_High",
                    "stock_Price_Low",
                ),
            )
            self.quarterData = quarter_data_frame

            logger.info(msg=str("Quarter data downloaded for stock " + ticker_name))

        except Exception:
            logger.error(
                msg=str("Couldn't download quarter data for stock " + ticker_name)
            )


def read_csv_from_disk(
    ticker_name: str, current_wd: str
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:  # Ticker, Sector or Market
    """Read downloaded data in to memory as data frames."""
    try:
        yearly = pd.read_csv(
            filepath_or_buffer=current_wd
            + "/data/"
            + ticker_name
            + "/"
            + ticker_name
            + "Year.csv"
        )
        yearly["report_End_Date"] = pd.to_datetime(
            yearly["report_End_Date"].str.replace("T", " "), format="%Y-%m-%d %H:%M:%S"
        )
        logger.info(msg=str("Read yearly data in to disk for " + ticker_name))

    except Exception:
        logger.error(msg=str("Couldn't read yearly data in to disk for " + ticker_name))

    try:
        quarterly = pd.read_csv(
            filepath_or_buffer=current_wd
            + "/data/"
            + ticker_name
            + "/"
            + ticker_name
            + "Quarter.csv"
        )
        quarterly["report_End_Date"] = pd.to_datetime(
            quarterly["report_End_Date"].str.replace("T", " "),
            format="%Y-%m-%d %H:%M:%S",
        )
        logger.info(msg=str("Read quarterly data in to disk for " + ticker_name))

    except Exception:
        logger.error(
            msg=str("Couldn't read quarterly data in to disk for " + ticker_name)
        )

    try:
        daily = pd.read_csv(
            filepath_or_buffer=current_wd
            + "/data/"
            + ticker_name
            + "/"
            + ticker_name
            + "price.csv"
        )
        daily["Time"] = pd.to_datetime(daily["Time"], format="%Y-%m-%d")
        logger.info(msg=str("Read daily data in to disk for " + ticker_name))

    except Exception:
        logger.error(msg=str("Couldn't read daily data in to disk for " + ticker_name))

    return yearly, quarterly, daily


def collect_ticker_metadata(
    apikey: str, current_wd: str
) -> Tuple[list, list, list, list, list, list, list, list]:
    """Function downloading meta-information of all tickers using api."""
    logger.info(msg="Start retrieving meta-data")

    request_instrument = requests.get(
        "https://apiservice.borsdata.se/v1/instruments?authKey=" + apikey
    )
    data_instruments = request_instrument.json()

    sleep(1)

    request_countries = requests.get(
        "https://apiservice.borsdata.se/v1/countries?authKey=" + apikey
    )
    data_countries = request_countries.json()

    sleep(1)

    request_markets = requests.get(
        "https://apiservice.borsdata.se/v1/markets?authKey=" + apikey
    )
    data_markets = request_markets.json()

    sleep(1)

    request_sectors = requests.get(
        "https://apiservice.borsdata.se/v1/sectors?authKey=" + apikey
    )
    data_sectors = request_sectors.json()

    sleep(1)

    (
        names_list,
        url_name_list,
        instrument_list,
        ticker_list,
        sector_id_list,
        market_id_list,
        country_id_list,
        ins_id_list,
    ) = instrument_dictionary(
        data_instruments
    )  # Fetch all ticker data

    sector_id_list_transl = []
    for value in sector_id_list:
        temp = get_sector(value, data_sectors["sectors"])
        sector_id_list_transl.append(temp)

    market_id_list_transl = []
    for value in market_id_list:
        temp = get_market(value, data_markets["markets"])
        market_id_list_transl.append(temp)

    country_id_list_transl = []
    for value in country_id_list:
        temp = get_country(value, data_countries["countries"])
        country_id_list_transl.append(temp)

    try:
        os.mkdir(current_wd + "/data")
    except OSError:
        logger.info(msg="Folder already exists")

    pd.DataFrame(
        {
            "Name": names_list,
            "Ticker": ticker_list,
            "Sector": sector_id_list_transl,
            "Market": market_id_list_transl,
            "Country": country_id_list_transl,
        }
    ).to_csv(
        path_or_buf=current_wd + "/data/Tickers.csv",
        sep=",",
        index=False,
        decimal=".",
        encoding="utf-8",
    )
    return (
        names_list,
        url_name_list,
        instrument_list,
        ticker_list,
        sector_id_list,
        market_id_list,
        country_id_list,
        ins_id_list,
    )


def download_all_data(
    read_tickers: pd.DataFrame,
    ticker_list: list,
    ins_id: list,
    apikey: str,
    current_wd: str,
) -> None:
    """Meta-function downloading all the yearly, daily and quarterly data using api."""
    tickers = []
    i = 0
    for item in read_tickers["Ticker"]:
        i += 1
        logger.info(msg="Reading item" + str(item))

        try:
            temp_object = CollectTickerData(
                item, ticker_list=ticker_list, ins_id=ins_id, apikey=apikey
            )
            tickers.append(temp_object)
            logger.info(msg=str(item + " successfull collection."))

        except Exception:
            logger.error(msg=str(item + " failed collection."))

        try:
            os.mkdir(current_wd + "/data/" + item)
            logger.info(msg=str(item + " folder created."))
        except Exception:
            logger.error(msg=str(item + " folder already exists."))

        try:
            temp_object.priceData.to_csv(
                path_or_buf=current_wd + "/data/" + item + "/" + item + "price.csv",
                sep=",",
                header=True,
                index=False,
                decimal=".",
            )
            logger.info(msg=str(item + " price data created."))

        except Exception:
            logger.error(msg=str(item + " couldn't write price data."))

        try:
            temp_object.quarterData.to_csv(
                path_or_buf=current_wd + "/data/" + item + "/" + item + "Quarter.csv",
                sep=",",
                header=True,
                index=False,
                decimal=".",
            )
            logger.info(msg=str(item + " quarter data created."))

        except Exception:
            logger.error(msg=str(item + " couldn't write quarter data."))

        try:
            temp_object.yearData.to_csv(
                path_or_buf=current_wd + "/data/" + item + "/" + item + "Year.csv",
                sep=",",
                header=True,
                index=False,
                decimal=".",
            )
            logger.info(msg=str(item + " year data created."))

        except Exception:
            logger.error(msg=str(item + " couldn't write year data."))
