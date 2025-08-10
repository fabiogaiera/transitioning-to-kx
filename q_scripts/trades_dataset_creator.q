
loadcsvandsavetable: {[csvpath;marketopen;marketclose]
    trades: ("PSFJ";enlist ",") 0: `$csvpath;
    trades: select from trades where timestamp within (marketopen;marketclose);
    tvolume: select tc: count i by time: 60 xbar timestamp.minute from trades;
    show tvolume
    //save table here
 }

loadcsvandsavetable["/home/fabio/data/IBM_trades.csv";2025.06.06D13:30:00.000000000; 2025.06.06D20:00:00.000000000]