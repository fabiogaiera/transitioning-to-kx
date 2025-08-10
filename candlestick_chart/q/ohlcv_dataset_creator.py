# ohlcv_dataset_creator.py

# Import necessary libraries
import pykx as kx

"""
CSV format example
timestamp,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_dataframe(csv_file_path, market_open_timespan, market_close_timespan):
    # Upload a CSV file into a kdb+ table
    # P stands for timestamp
    # S stands for symbol
    # F stands for float
    # J stands for long
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path}"')

    # Add the column date
    kx.q(f'trades: update date: `date$timestamp from trades')

    # Add the columns mo and mc
    kx.q(f'trades: update mo: date + {market_open_timespan}, mc: date + {market_close_timespan} from trades')

    # Select trades done during market hours
    kx.q(f'trades: select from trades where timestamp within (mo; mc)')

    # Aggregate data by date
    aggregation = kx.q('select open: first price, high: max price, low: min price, close: last price, volume: sum size by date from trades')

    # Transform to a pandas.DataFrame instance
    return aggregation.pd()
