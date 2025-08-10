loadcsvandsavetable:{[csvpath1;csvpath2;marketopen;marketclose]

    // Load CSV into a table
    trades: ("PSFJ";enlist ",") 0: `$csvpath1;
    quotes: ("PSFJFJ";enlist ",") 0: `$csvpath2;

    // Filter by date
    trades: select from trades where timestamp within (marketopen;marketclose);
    quotes: select from quotes where timestamp within (marketopen;marketclose);

    //Key the table
    quotes: `sym`timestamp xkey quotes;

    // As-Of Join
    taq: aj[`sym`timestamp;trades;quotes];

    // Arithmetics to obtain bid-ask spread
    taq: update mid_price: (bid_price + ask_price) % 2 from taq;
    taq: update bid_ask_spread: 2 * (abs(price - mid_price) % mid_price) * 100 from taq;

    show taq
    //save table here

 }


loadcsvandsavetable["/home/fabio/data/IBM_trades.csv";"/home/fabio/data/IBM_quotes.csv";2025.06.16D13:30:00.000000000; 2025.06.16D20:00:00.000000000]