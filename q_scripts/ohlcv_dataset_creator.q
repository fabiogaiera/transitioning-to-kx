
loadcsvandsavetable: {[csvpath;marketopen;marketclose]
    trades: ("PSFJ";enlist ",") 0: `$csvpath;
    trades: update date: `date$timestamp from trades;
    trades: update mo: date + marketopen, mc: date + marketclose from trades;
    trades: select from trades where timestamp within (mo; mc);
    aggregation: select open: first price, high: max price, low: min price, close: last price, volume: sum size by date from trades;
    show aggregation
    //save table here
 }

loadcsvandsavetable["/home/fabio/data/IBM_trades.csv";13:30:00.000000000; 20:00:00.000000000]