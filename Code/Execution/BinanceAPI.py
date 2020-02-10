
from binance.client import Client
from Execution.InterfaceAPI import API
from datetime import datetime

class BinanceAPI (API):

    def __init__(self):
        api_key = "rOsVSRe409vOsHGnwpErHivGTsAqCHNxZoNnocvYnuhBCX1iAbBnTsiKSh5hBmyV"
        api_secret = "d7zvWZBktLsFJVp8T5g6Q8koLQUPPr8GEwBu41Dfgame25r8L8zbtpuTuzE2gRAh"
        self.client = Client( api_key , api_secret )
        
        self.allowedTickers = [
            "BTCUSDT",
            "ETHUSDT",
            "BTCETH"
        ]
    
    def check_allowed_ticker(self,ticker):
        return ticker in self.allowedTickers

    def create_order(self,ticker,quantity,side,orderType,price=0):
        
        sideAPI = Client.SIDE_SELL if side == "SELL" else Client.SIDE_BUY if side == "BUY" else None
        typeAPI = Client.ORDER_TYPE_MARKET if orderType == "MARKET" else Client.ORDER_TYPE_LIMIT if orderType == "LIMIT" else None

        if sideAPI == None: raise Exception ("Side not allowed")
        if typeAPI == None: raise Exception ("Type not allowed")

        order = self.client.create_order(
            symbol=ticker,
            side=sideAPI,
            type=typeAPI,
            quantity=quantity)
        
        return True

    def get_all_tickers_prices(self):
        return self.client.get_all_tickers()

    def get_order_book(self,symbol):
        # get market depth
        return self.client.get_order_book(symbol=symbol)

    def get_historical_data(self,symbol,interval,startDate,endDate):

        startDate = startDate.strftime("%d %b, %Y")
        endDate = endDate.strftime("%d %b, %Y")
             
        if interval == '15':
            APIInterval = Client.KLINE_INTERVAL_15MINUTE

        return self.client.get_historical_klines(symbol, APIInterval , startDate, endDate )
