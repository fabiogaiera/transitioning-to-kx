# trades_dataframe_creator.py

# Import necessary libraries
import pykx as kx

"""
CSV format example
timestamp,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""

"""
Notice that there is a mix of naming convention variables: q variables and Python variables typically using _
"""


def create_dataset(csv_file_path, market_open, market_close):
    # Upload a CSV file into a kdb+ table
    # P stands for timestamp
    # S stands for symbol
    # F stands for float
    # J stands for long
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path}"')

    # Filter trades data considering only market hours
    kx.q(f'trades: select from trades where timestamp within {market_open} {market_close}')

    # Execute a qSQL query using xbar to bucket the minutes into hours
    trades_table = kx.q('select tc: count i by time: 60 xbar timestamp.minute from trades')

    # Transform to a pandas.DataFrame instance
    return trades_table.pd()
