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

    trades = trades.update(
        kx.Column('return', value=(kx.Column('close').divide(kx.Column('close').prev()) - 1))
    )

    print(trades)

    # kx.q['trades'] = trades
    # kx.q('trades: update return: (close % (prev close)) - 1 from trades')
    # kx.q('show trades')
