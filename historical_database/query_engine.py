import pykx as kx


def run_query(database_path):
    db = kx.DB(path=database_path)
    trades = db.table.trade_data.select(

        columns={'close': kx.Column('price').last()},

        where=(
                (kx.Column('date') >= kx.q('2025.04.02')) &
                (kx.Column('date') <= kx.q('2025.04.09'))
        ),

        by=kx.Column('date')

    )
    print(trades)
