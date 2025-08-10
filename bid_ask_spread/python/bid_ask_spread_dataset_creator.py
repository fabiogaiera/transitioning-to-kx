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
    # Upload CSV files into kdb+ tables

    trades = kx.q.read.csv(csv_file_path_1,
                           [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])

    quotes = kx.q.read.csv(csv_file_path_2,
                           [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom, kx.FloatAtom, kx.LongAtom])

    filtered_trades = trades.select(
        where=(
                (kx.Column('timestamp') >= kx.q(market_open)) &
                (kx.Column('timestamp') <= kx.q(market_close))
        )
    )

    filtered_quotes = quotes.select(
        where=(
                (kx.Column('timestamp') >= kx.q(market_open)) &
                (kx.Column('timestamp') <= kx.q(market_close))
        )
    )

    # Key the quotes table
    filtered_quotes_keyed = kx.q.xkey(['sym', 'timestamp'], filtered_quotes)

    # As-Of Join between trades and quotes tables
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'timestamp']), filtered_trades, filtered_quotes_keyed)

    # Clean dataset here

    # Calculate mid_price
    taq_table = taq_table.update(
        kx.Column('mid_price', value=((kx.Column('bid_price') + kx.Column('ask_price')) / 2)))

    # Calculate Effective bid_ask_spread (Percentage Form)
    taq_table = taq_table.update(
        kx.Column('bid_ask_spread',
                  value=((2 * abs(kx.Column('price') - kx.Column('mid_price'))) / kx.Column('mid_price')) * 100)
    )

    # Convert to pandas DataFrame
    return taq_table.pd()
