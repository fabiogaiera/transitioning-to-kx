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
- 📊 Grouping and aggregating data using `xbar`
- 🐍 Seamless integration with your existing Python code — because, let’s be honest, you probably have a lot of it!

## Prerequisites

Before we dive in, make sure:

- ✅ kdb+ and PyKX are installed and working
- ✅ You have some example CSV tick data ready (you can use sample data from my repository)


## Let’s Build

Now that you're set up, you're ready to build your Intraday Trading Volume Histogram step by step.

### Step 1: Create the dataset with PyKX

See [trades_dataset_creator.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/intraday_trading_volume/trades_dataset_creator.py)

### Step 2: Build the histogram with Matplotlib

See [volumes_histogram_creator.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/intraday_trading_volume/volumes_histogram_creator.py)

### Step 3: The main script

See [intraday_trading_volume_script.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/intraday_trading_volume/intraday_trading_volume_script.py)

Here's the link to the GitHub repository for full reference: [intraday_trading_volume](https://github.com/fabiogaiera/transitioning-to-kx/tree/master/intraday_trading_volume)


## Potential Enhancements

- In real-world scenarios, kdb+ tables are partitioned. This allows for optimal performance when storing/retrieving
  data.
- Consider building a `kdb+tick` architecture when creating a real-time and historical tick data solution.

## Conclusion

Given a CSV file with tick data, there's no need to use PyKX to create a pandas DataFrame, 
as the CSV can be directly converted using pandas.

The purpose here is to demonstrate how to integrate different formats and technologies. 
The real power of kdb+ can be leveraged, for example, in high-frequency trading.

## Further Readings

- [count](https://code.kx.com/pykx/3.1/api/pykx-execution/q.html#count)
- [xbar](https://code.kx.com/pykx/3.1/api/pykx-q-data/wrappers.html#pykx.wrappers.Table.xbar)
- [.pd()](https://code.kx.com/pykx/3.1/api/pykx-q-data/wrappers.html)

**Glad you made it to the end—hope you enjoyed it.**
