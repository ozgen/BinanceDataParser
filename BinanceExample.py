import json
from binance.client import Client
import BinanceHistoricDataParser
from DateUtil import date_to_milliseconds

symbol = "XRPBTC"
start = "1 Dec, 2017"
end = "1 Jan, 2018"
interval = Client.KLINE_INTERVAL_30MINUTE

klines = BinanceHistoricDataParser.get_historical_klines(symbol, interval, start, end)

# open a file with filename including symbol, interval and start and end converted to milliseconds
with open(
        "Binance_{}_{}_{}-{}.json".format(
            symbol,
            interval,
            date_to_milliseconds(start),
            date_to_milliseconds(end)
        ),
        'w'  # set file write mode
) as f:
    f.write(json.dumps(klines))

