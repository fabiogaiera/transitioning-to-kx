# candlestick_chart_script.py

import sys

from candlestick_chart.candlestick_chart_creator import create_candlestick_chart
from candlestick_chart.python.ohlcv_dataset_creator import create_dataframe

"""
Usage in Linux / Mac:
python -m candlestick_chart.candlestick_chart_script /path/to/file/trades.csv

Usage in Windows: 
python -m candlestick_chart.candlestick_chart_script C:/path/to/file/trades.csv
"""

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Incorrect parameters")
        sys.exit(1)

    # Path to the CSV file
    trades_data = sys.argv[1]

    # Daylight Saving Time (DST) for Eastern Time (ET) in the U.S. as we're analyzing the IBM ticker.
    # Timespan data type in q
    market_open_timespan = '13:30:00.000000000'
    market_close_timespan = '20:00:00.000000000'

    trades_data_frame = create_dataframe(trades_data, market_open_timespan, market_close_timespan)
    create_candlestick_chart(trades_data_frame)
