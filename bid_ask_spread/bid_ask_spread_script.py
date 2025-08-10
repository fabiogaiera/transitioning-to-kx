# bid_ask_spread_script.py

import sys

from bid_ask_spread.bid_ask_spread_density_plot_creator import create_density_plot
from bid_ask_spread.python.bid_ask_spread_df_creator import retrieve_bid_ask_spread_df

"""
Usage in Linux / Mac:
python -m bid_ask_spread.bid_ask_spread_script /path/to/file/trades.csv /path/to/file/quotes.csv

Usage in Windows: 
python -m bid_ask_spread.bid_ask_spread_script C:/path/to/file/trades.csv C:/path/to/file/quotes.csv
"""

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect parameters")
        sys.exit(1)

    # Daylight Saving Time (DST) for Eastern Time (ET) in the U.S. as we're analyzing the IBM ticker.
    market_open = '2025.06.16D13:30:00.000000000'
    market_close = '2025.06.16D20:00:00.000000000'

    bid_ask_spread_df = retrieve_bid_ask_spread_df(sys.argv[1], sys.argv[2], market_open, market_close)
    create_density_plot(bid_ask_spread_df)
