import pykx as kx


def run_query(database_path):
    db = kx.DB(path=database_path)
    trades1 = db.table.trade_data.select(where= kx.Column('date') == kx.q('2025.04.02'))
    trades2 = db.table.trade_data.select(where= kx.Column('date') == kx.q('2025.04.03'))
    print(trades1)
    print(trades2)