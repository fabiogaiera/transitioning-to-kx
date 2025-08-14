# 📊 Transitioning to KX: Creating an Intraday Trading Volume Histogram

This post is a continuation of my previous article: 

[🚀 Transitioning to KX: Exploring a Series of Use Cases](https://www.linkedin.com/pulse/transitioning-kx-products-exploring-series-use-cases-fabio-gaiera-rfi2f)

## Getting Comfortable with a New Stack

Even if it might seem trivial, it's worth emphasizing: migrating to a new technology can be frustrating.

At first, you're likely to be excited by the advanced capabilities the technology offers—and tempted to jump straight
into the complex stuff. But in my experience, the smoothest (and most rewarding) transition happens when you start with
the basics and build up gradually.

## What You'll Learn

In this use case, I’ll walk you through key concepts and operations using kdb+ and PyKX, including:

- 📂 Uploading a CSV file (Trades Tick Data) into an in-memory kdb+ table
- 🔍 Performing date-based queries
- 🔄 Casting data types (e.g., from timestamp to date) — something you'll do frequently
- 📊 Grouping and aggregating data using `xbar`
- 🐍 Seamless integration with your existing Python code — because, let’s be honest, you probably have a lot of it!

## Prerequisites

Before we dive in, make sure:

- ✅ kdb+ and PyKX are installed and working
- ✅ You have some example CSV tick data ready (you can use sample data from my repository)


## Let’s Build: Intraday Trading Volume Histogram

Now that you're set up, you're ready to build your Intraday Trading Volume Histogram step by step.

### Step 1: Create the DataFrame with PyKX

```python
# trades_dataframe_creator.py

import pykx as kx

"""
CSV format example for trades:
timestamp,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_dataframe(csv_file_path, date, market_open, market_close):
    trades = kx.q.read.csv(csv_file_path, [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])

    intraday_trades = trades.select(
        where=((kx.Column('timestamp').cast('date')) == kx.q(date))
    )

    filtered_intraday_trades = intraday_trades.select(
        where=((kx.Column('timestamp') >= kx.q(market_open)) &
               (kx.Column('timestamp') <= kx.q(market_close)))
    )

    aggregation = filtered_intraday_trades.select(
        kx.Column('trades_count', value=kx.Column('i').count()),
        by=kx.Column('time', value=kx.Column('timestamp').minute.xbar(60))
    )

    return aggregation.pd()
```

### Step 2: Build the Histogram with Matplotlib

```python
# volumes_histogram_creator.py

import matplotlib.pyplot as plt


def create_histogram(df):
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title("Intraday Analysis")
    df.plot(kind='bar', ax=ax)
    ax.set_title("Intraday Trading Volume Histogram", fontsize=14)
    ax.set_xlabel("Hour", fontsize=12)
    ax.set_ylabel("Total Size", fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    plt.show()
```

### Step 3: The Main Script

```python
import sys

from intraday_trading_volume.python.trades_dataset_creator import create_dataset
from intraday_trading_volume.volumes_histogram_creator import create_histogram

"""
Usage in Linux / Mac:
python -m intraday_trading_volume.intraday_trading_volume_script /path/to/file/trades.csv 2025-06-06

Usage in Windows: 
python -m intraday_trading_volume.intraday_trading_volume_script C:/path/to/file/trades.csv 2025-06-06
"""

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect parameters")
        sys.exit(1)

    # Path to the CSV file
    trades_data = sys.argv[1]

    # Daylight Saving Time (DST) for Eastern Time (ET) in the U.S. as we're analyzing the IBM ticker.
    # Timestamp data type in q
    market_open = '2025.06.06D13:30:00.000000000'
    market_close = '2025.06.06D20:00:00.000000000'

    trades_dataset = create_dataset(trades_data, market_open, market_close)
    create_histogram(trades_dataset)
```


## GitHub Repository

Here's the link to the GitHub repository: [Intraday Trading Volume](https://github.com/fabiogaiera/transitioning-to-kx/tree/master/intraday_trading_volume)


## Potential Enhancements

- In real-world scenarios, kdb+ tables are partitioned. This allows for optimal performance when storing/retrieving
  data.
- Consider building a `kdb+tick` architecture when creating a real-time and historical tick data solution.


## Further Readings

- [Database Creation and Management](https://code.kx.com/pykx/3.1/examples/db-management.html)
- [Example: Real-Time Streaming using PyKX](https://code.kx.com/pykx/3.1/examples/streaming/index.html)


**Glad you made it to the end—hope you enjoyed it.**
