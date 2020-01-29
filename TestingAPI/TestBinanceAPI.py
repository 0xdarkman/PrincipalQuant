from binance.client import Client
api_key = "rOsVSRe409vOsHGnwpErHivGTsAqCHNxZoNnocvYnuhBCX1iAbBnTsiKSh5hBmyV"
api_secret = "d7zvWZBktLsFJVp8T5g6Q8koLQUPPr8GEwBu41Dfgame25r8L8zbtpuTuzE2gRAh"
client = Client( api_key , api_secret )

# get market depth
depth = client.get_order_book(symbol='ETHUSDT')

# place a test market buy order, to place an actual order use the create_order function
# order = client.create_order(
#     symbol='ETHUSDT',
#     side=Client.SIDE_SELL,
#     type=Client.ORDER_TYPE_MARKET,
#     quantity=0.057)

# get all symbol prices
prices = client.get_all_tickers()

# withdraw 100 ETH
# check docs for assumptions around withdrawals
# from binance.exceptions import BinanceAPIException, BinanceWithdrawException
# try:
#     result = client.withdraw(
#         asset='ETH',
#         address='<eth_address>',
#         amount=100)
# except BinanceAPIException as e:
#     print(e)
# except BinanceWithdrawException as e:
#     print(e)
# else:
#     print("Success")

# # fetch list of withdrawals
# withdraws = client.get_withdraw_history()

# # fetch list of ETH withdrawals
# eth_withdraws = client.get_withdraw_history(asset='ETH')

# get a deposit address for BTC
# address = client.get_deposit_address(asset='BTC')

# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

# from binance.websockets import BinanceSocketManager
# bm = BinanceSocketManager(client)
# bm.start_aggtrade_socket('BNBBTC', process_message)
# bm.start()

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2014", "1 Jan, 2020")

# fetch weekly klines since it listed
klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")
