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
    trades = kx.q.read.csv(csv_file_path, [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])

    # Add the column date
    trades['date'] = trades['timestamp'].date

    # Set an index
    trades.set_index('date')

    # Add the columns market_open and market_close
    trades['market_open'] = trades['date'] + kx.q(market_open_timespan)
    trades['market_close'] = trades['date'] + kx.q(market_close_timespan)

    # Select trades done during market hours
    market_hours_trades = trades.select(

        where=(
                (kx.Column('timestamp') >= kx.Column('market_open')) &
                (kx.Column('timestamp') <= kx.Column('market_close'))
        )
    )

    # Aggregate data by date
    aggregated_data = market_hours_trades.select(

        columns={

            'open': kx.Column('price').first(),
            'high': kx.Column('price').max(),
            'low': kx.Column('price').min(),
            'close': kx.Column('price').last(),
            'volume': kx.Column('size').sum(),
        },

        by=kx.Column('date')

    )

    # Transform to a pandas.DataFrame instance
    return aggregated_data.pd()
