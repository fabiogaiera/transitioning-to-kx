# 🕯 Transitioning to KX: Building OHLCV Datasets & Candlestick Charts ️

This post is a continuation of my previous write-ups: 

[🚀 Transitioning to KX: Exploring a Series of Use Cases](https://www.linkedin.com/pulse/transitioning-kx-products-exploring-series-use-cases-fabio-gaiera-rfi2f)  
[📊 Transitioning to KX: Creating an Intraday Trading Volume Histogram](https://www.linkedin.com/pulse/transitioning-kx-products-creating-intraday-trading-volume-gaiera-c1lxf)  

Today, we’re diving into something simple yet incredibly powerful in the world of trading data: **OHLCV datasets**.

Yes—**Open, High, Low, Close, Volume**. Basic, right? But don’t be fooled. These little columns unlock a ton of
possibilities, from technical analysis to full-blown algorithmic strategy development.

## 🧩 Why OHLCV Matters (More Than You Think)

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

## ✅ What You Need Before We Start

- ✅ kdb+ and PyKX installed and working
- ✅ A sample CSV file with tick data (You can grab one from my GitHub repo if needed)

## 🛠️ Time to Build!

In this walkthrough, I’ll show you how to construct OHLCV datasets and candlestick charts using **PyKX** and **Plotly**.

### 📊 OHLCV Dataset Creation

Here's what we’ll cover:

- 📂 Upload a CSV file (tick-by-tick trade data) into an in-memory kdb+ table
- 🧱 Add auxiliary columns to help with dataset construction (This will feel familiar if you’ve used the `pandas`
  library)
- 🔍 Query the data (something we covered in a previous post)
- 📊 Group and aggregate using built-in operators like `first`, `max`, `min`, and `last`
- 🧬 Integrate everything with your existing Python codebase (Transform KX data types into a pandas DataFrame — a
  game-changer if you're coming from a Python-heavy stack!)

Translated to code:

```python
# Import necessary libraries
import pykx as kx


# CSV format example:
# timestamp,sym,price,size
# 2025.05.05D08:00:00.009039359,IBM,244.56,10
# 2025.05.05D08:00:00.156501572,IBM,243,8
# 2025.05.05D08:00:00.156579644,IBM,244.03,6

def create_dataframe(csv_file_path, market_open_timespan, market_close_timespan):
    # Upload a CSV file into a kdb+ table
    trades = kx.q.read.csv(csv_file_path, [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])

    # Add a 'date' column
    trades['date'] = trades['timestamp'].date

    # Set an index
    trades.set_index('date')

    # Add 'market_open' and 'market_close' columns
    trades['market_open'] = trades['date'] + kx.q(market_open_timespan)
    trades['market_close'] = trades['date'] + kx.q(market_close_timespan)

    # Select trades executed during market hours
    market_hours_trades = trades.select(
        where=(
                (kx.Column('timestamp') >= kx.Column('market_open')) &
                (kx.Column('timestamp') <= kx.Column('market_close'))
        )
    )

    # Aggregate data by date
    aggregated_data = market_hours_trades.select(
        columns={
            'open': kx.Column('price').first(),
            'high': kx.Column('price').max(),
            'low': kx.Column('price').min(),
            'close': kx.Column('price').last(),
            'volume': kx.Column('size').sum(),
        },
        by=kx.Column('date')
    )

    # Transform to a pandas.DataFrame instance
    return aggregated_data.pd()
```

### 🕯️ Candlestick Chart Creation

In this section, we’ll code the candlestick chart using the Plotly library: 

```python
# candlestick_chart_script.py

import plotly.graph_objects as go


def create_candlestick_chart(df):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df.index.date,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            showlegend=False
        )
    ])

    fig.update_layout(
        title={
            'text': 'Candlestick Chart',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Black')
        },
        xaxis=dict(
            title=dict(text='Date', font=dict(size=16)),
            tickfont=dict(size=12),
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.3)',
            gridwidth=1,
            rangeslider=dict(visible=False)
        ),
        yaxis=dict(
            title=dict(text='Price', font=dict(size=16)),
            tickfont=dict(size=12),
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.3)',
            gridwidth=1,
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Arial", size=12),
        margin=dict(l=50, r=50, t=80, b=50),
    )

    fig.update_xaxes(type='category')
    fig.update_yaxes(tickprefix="$")

    fig.show()
```

### 🐍 Python Script to Generate the Chart

```python
import sys

from candlestick_chart.python.ohlcv_dataset_creator import create_dataset
from candlestick_chart.candlestick_chart_creator import create_candlestick_chart

# Usage on Linux / macOS:
# python -m candlestick_chart.candlestick_chart_script /path/to/file/trades.csv

# Usage on Windows:
# python -m candlestick_chart.candlestick_chart_script C:/path/to/file/trades.csv

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Incorrect parameters")
        sys.exit(1)

    # Path to the CSV file
    trades_data = sys.argv[1]

    # Daylight Saving Time (DST) for Eastern Time (ET) in the U.S., since we’re analyzing the IBM ticker
    market_open_timespan = '13:30:00.000000000'
    market_close_timespan = '20:00:00.000000000'

    trades_data_frame = create_dataset(trades_data, market_open_timespan, market_close_timespan)
    create_candlestick_chart(trades_data_frame)
```

## GitHub Repository

Here’s the link to the GitHub repository: [Candlestick Chart](https://github.com/fabiogaiera/transitioning-to-kx/tree/master/candlestick_chart)

If you prefer using kdb+/q instead of the PyKX library, I’ve created a dedicated package called `q`, which contains
kdb+/q expressions invoked via `kx.q("kdb+/q code here")`.

Thanks for reading! Your feedback is much appreciated.