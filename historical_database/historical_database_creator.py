from datetime import date

import pykx as kx

db = kx.DB(path='/home/fabio/db')

N = 1000000
trades = kx.Table(data={
    'date': kx.random.random(N, [date(2020, 1, 1), date(2020, 1, 2)]),
    'sym': kx.random.random(N, ['AAPL', 'GOOG', 'MSFT']),
    'price': kx.random.random(N, 10.0),
    'size': kx.random.random(N, 1000)
})

db.create(trades, 'trade_data', 'date')
