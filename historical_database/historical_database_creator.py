import pykx as kx


def create_or_update_database(csv_file_path, database_path, market_open, market_close):
    # Upload CSV file into trades table
    trades_table = kx.q.read.csv(csv_file_path, [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])

    # Filter trades by market hours
    filtered_trades_table = trades_table.select(
        where=(
                (kx.Column('timestamp') >= kx.q(market_open)) &
                (kx.Column('timestamp') <= kx.q(market_close))
        )
    )

    # Add the column date
    filtered_trades_table['date'] = filtered_trades_table['timestamp'].date

    db = kx.DB(path=database_path)
    db.create(filtered_trades_table, table_name='trade_data', partition='date')
