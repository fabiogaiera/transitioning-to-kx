# bid_ask_spread_dataset_creator.py

import pykx as kx

from bid_ask_spread.benchmark_util import log_execution_time

"""
CSV format example for trades
timestamp,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""

"""
CSV format example for quotes
timestamp,sym,bid_price,bid_size,ask_price,ask_size
2025.05.23D08:00:00.001037561,IBM,257.03,2,260.91,1
2025.05.23D08:00:00.001062570,IBM,257.03,2,259.77,1
2025.05.23D08:00:00.009487606,IBM,257.03,2,259.49,1
2025.05.23D08:00:00.017576775,IBM,257.03,2,259.41,1
"""


@log_execution_time
def create_dataset(csv_file_path_1, csv_file_path_2, market_open, market_close):
    # Upload CSV file into trades table
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path_1}"')
    # Upload CSV file into quotes table
    kx.q(f'quotes: ("PSFJFJ";enlist ",") 0: `$":{csv_file_path_2}"')

    # Filter trades by market hours
    kx.q(f'trades: select from trades where timestamp within({market_open};{market_close})')
    # Filter quotes by market hours
    kx.q(f'quotes: select from quotes where timestamp within({market_open};{market_close})')

    # Order the quotes by timestamp and apply grouped to sym
    kx.q('quotes: update `g#sym from `timestamp xasc quotes')
    # As-Of Join between trades and quotes tables
    kx.q('taq: aj[`sym`timestamp;trades;quotes]')

    # Calculate mid_price
    kx.q('taq: update mid_price: (bid_price + ask_price) % 2 from taq')
    # Calculate Effective bid_ask_spread (Percentage Form)
    taq_table = kx.q('update bid_ask_spread: 2 * (abs(price - mid_price) % mid_price) * 100 from taq')

    # Convert to pandas DataFrame
    return taq_table.pd()
