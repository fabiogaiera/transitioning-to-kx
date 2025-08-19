# 🕯 Transitioning to KX: Building OHLCV Datasets and Candlestick Charts ️

This post is a continuation of my previous write-ups: 

[🚀 Transitioning to KX: Exploring a Series of Use Cases](https://www.linkedin.com/pulse/transitioning-kx-products-exploring-series-use-cases-fabio-gaiera-rfi2f)  
[📊 Transitioning to KX: Creating an Intraday Trading Volume Histogram](https://www.linkedin.com/pulse/transitioning-kx-products-creating-intraday-trading-volume-gaiera-c1lxf)  

Today, we’re diving into something simple yet incredibly powerful in the world of trading data: **OHLCV datasets**.

Yes—**Open, High, Low, Close, Volume**. Basic, right? But don’t be fooled. These little columns unlock a ton of
possibilities, from technical analysis to full-blown algorithmic strategy development.

## 🧩 Why OHLCV matters (more than you think)

OHLCV datasets play a critical role across many different use cases. Here's just a taste:

### 1. 📉 Technical Analysis

- **Chart Pattern Recognition**: Spot patterns like head and shoulders, double tops/bottoms, flags, and wedges.
- **Indicator Calculations**: Feed your favorite indicators like RSI, MACD, Bollinger Bands, and moving averages.
- **Candlestick Analysis**: Use candlestick formations to infer potential reversals or trend continuations.

### 2. 🤖 Algorithmic Trading / Strategy Development

- **Signal Generation**: Create entry/exit signals based on OHLC price behavior.
- **Feature Engineering**: Use OHLCV-derived features in ML models to predict price moves or classify market states.
- **Execution Logic**: Set stop-loss or take-profit levels using highs and lows.

### 3. 🔬 Market Microstructure Analysis

- **Liquidity Assessment**: Analyze market depth and impact using price and volume data.
- **Price Discovery**: Understand how the market digests information over specific time intervals.

### 4. 📊 Portfolio Optimization

- **Risk Modeling**: Measure drawdowns, daily ranges, and asset-specific volatility.
- **Correlation Analysis**: Use closing prices to build correlation matrices and design diversified portfolios.

### 5. 📈 Performance Analytics

- **Return Calculations**: Derive daily or monthly returns from closing prices.
- **Volatility Clustering**: Identify shifts in market volatility and periods of stress.
- **Sharpe/Sortino Ratios**: Compute performance metrics using return and risk data.

### 6. 🛡️ Risk Management Testing

- **Backtesting**: Simulate different risk models like fixed fractional, Kelly criterion, or volatility-adjusted sizing.
- **Strategy Evaluation**: Observe how stop-loss, take-profit, or drawdown rules perform over time.

And honestly, that’s just scratching the surface.

## ✅ What you need before we start

- ✅ kdb+ and PyKX installed and working
- ✅ A sample CSV file with tick data (You can grab one from my GitHub repo if needed)

## 🛠️ Time to build!

In this walkthrough, I’ll show you how to construct OHLCV datasets and candlestick charts using **PyKX** and **Plotly**.

### 📊 OHLCV Dataset Creation

Here's what we’ll cover:

- 📂 Upload a CSV file (tick-by-tick trade data) into an in-memory kdb+ table
- 🧱 Add auxiliary columns to help with dataset construction (This will feel familiar if you’ve used the pandas library)
- 🔍 Query the data (something we covered in a previous post)
- 📊 Group and aggregate using built-in operators like `first`, `max`, `min`, and `last` (this is new!)
- 🧬 Integrate everything with your existing Python codebase (Transform KX data types into a pandas DataFrame — a
  game-changer if you're coming from a Python-heavy stack!)

Translated to code: [ohlcv_dataset_creator.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/candlestick_chart/ohlcv_dataset_creator.py)


### 🕯️ Candlestick Chart Creation

In this section, we’ll code the candlestick chart using the Plotly library: [candlestick_chart_creator.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/candlestick_chart/candlestick_chart_creator.py)

### 🐍 Python script to generate the Chart

See [candlestick_chart_script.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/candlestick_chart/candlestick_chart_script.py)

### 💻 GitHub repository

Here’s the link to the repository for full reference: [candlestick_chart](https://github.com/fabiogaiera/transitioning-to-kx/tree/master/candlestick_chart)

## 📖 Further readings

- [first](https://code.kx.com/pykx/3.1/api/pykx-execution/q.html#first)
- [max](https://code.kx.com/pykx/3.1/api/pykx-execution/q.html#max)
- [min](https://code.kx.com/pykx/3.1/api/pykx-execution/q.html#min)
- [last](https://code.kx.com/pykx/3.1/api/pykx-execution/q.html#last)

Thanks for reading! Your feedback is much appreciated.