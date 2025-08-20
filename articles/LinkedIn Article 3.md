# 📊 Transitioning to KX: Creating a Bid-Ask Spread Chart

This post continues from my previous write-ups:

[🚀 Transitioning to KX: Exploring a Series of Use Cases](https://www.linkedin.com/pulse/transitioning-kx-products-exploring-series-use-cases-fabio-gaiera-rfi2f)  
[📊 Transitioning to KX: Creating an Intraday Trading Volume Histogram ](https://www.linkedin.com/pulse/transitioning-kx-products-creating-intraday-trading-volume-gaiera-c1lxf)  
[🕯 Transitioning to KX: Building OHLCV Datasets & Candlestick Charts ](https://www.linkedin.com/pulse/transitioning-kx-products-building-ohlcv-datasets-charts-fabio-gaiera-hozzf)  

Today, we’re diving into more complex queries and arithmetic operations in **kdb+**.  
Until now, we’ve focused on selections and simple aggregations within a single table. But what happens when we need to correlate data across **multiple tables**? If you're familiar with SQL, you might recall operators like `INNER JOIN`, `LEFT JOIN`,`RIGHT JOIN`, and so on. In the world of **Trades** and **Quotes** data, we introduce a particularly powerful concept: the **AS-OF JOIN** operator.

## 🔍 What is an AS-OF JOIN?

An **AS-OF JOIN** matches rows from two tables based on the closest **preceding (or equal)** timestamp — **not** an exact match.

### In simpler terms:

- For each row in the **left** table (e.g., `Trades`), it finds the most recent row in the **right** table (e.g., `Quotes`) with a timestamp **less than or equal to** the trade's timestamp.  
- Think of it as a “nearest earlier timestamp” join.

## 🧠 Why use AS-OF JOIN for Trades and Quotes?

- **Trades** occur at specific, discrete timestamps.  
- **Quotes** continuously update bid and ask prices at different timestamps.  
- To analyze market conditions at the time of a trade, we want to pair each trade with the **most recent quote**  
  available at or before that timestamp.  
- Because quotes update asynchronously, **exact timestamp matches are rare** — which is why AS-OF JOIN is essential.

## 🆚 How does it differ from a standard JOIN?

| Standard JOIN                  | AS-OF JOIN                              |
|-------------------------------|---------------------------------------|
| Requires exact timestamp match | Finds the most recent earlier timestamp |

## 🛠️ Where is the AS-OF JOIN operator available?

Most **RDBMS** and **NoSQL** systems do not offer native AS-OF JOIN functionality. However, **kdb+**, **ClickHouse**, and **QuestDB** provide built-in support for it.

## 🧪 Example: AS-OF JOIN between Trades and Quotes

### Trades (1 row)

| timestamp           | sym  | price  | size |
|---------------------|------|--------|------|
| 2025-08-07 10:00:06 | AAPL | 200.75 | 150  |

### Quotes (3 rows)

| timestamp           | sym  | bid_price | bid_size | ask_price | ask_size |
|---------------------|------|-----------|----------|-----------|----------|
| 2025-08-07 10:00:01 | AAPL | 200.40    | 300      | 200.60    | 250      |
| 2025-08-07 10:00:05 | AAPL | 200.65    | 320      | 200.85    | 270      |
| 2025-08-07 10:00:08 | AAPL | 200.90    | 310      | 201.10    | 290      |

### AS-OF JOIN Result (1 row)

We look for the quote with the **latest timestamp ≤ 2025-08-07 10:00:06**. That would be the quote at **10:00:05**.

| trade_timestamp     | sym  | trade_price | trade_size | quote_timestamp     | bid_price | bid_size | ask_price | ask_size |
|---------------------|------|-------------|------------|---------------------|-----------|----------|-----------|----------|
| 2025-08-07 10:00:06 | AAPL | 200.75      | 150        | 2025-08-07 10:00:05 | 200.65    | 320      | 200.85    | 270      |

## 🤔 How can I use the TAQ dataset?

Having created the TAQ (Trades And Quotes) dataset using the AS-OF JOIN, what's next? In this article, our aim is to calculate the bid-ask spread throughout a day.  
We won't enter into technical details of what the bid-ask spread is (there are several types of spreads), but briefly, I can tell you that Quant Traders care about the Bid-Ask spread since it has impacts on:

1. Trading costs  
2. Execution quality  
3. Strategy profitability

**🔼 High Bid-Ask Spread**

- The gap between bid and ask is large  
- Example: Bid = $10.00, Ask = $10.50 → Spread = $0.50

🔍 What it means:

- Low liquidity (fewer buyers and sellers)  
- Higher uncertainty or volatility  
- Wider price disagreement between participants  
- Common in illiquid stocks, after-hours trading, or during market stress

💥 Impact on trades:

- Higher trading cost (you pay more to buy / get less when selling)  
- Harder to enter/exit positions without price impact  
- Bad for high-frequency or short-term strategies  
- May require limit orders to avoid overpaying

**🔽 Low Bid-Ask Spread**

- The gap between bid and ask is small  
- Example: Bid = $10.00, Ask = $10.01 → Spread = $0.01

🔍 What it means:

- High liquidity  
- Tighter competition among buyers/sellers  
- Common in large-cap stocks, ETFs, and active markets

💥 Impact on trades:

- Lower trading cost  
- Easier to execute large or frequent trades  
- Ideal for algo trading, scalping, market making  
- Better price transparency and execution quality

**Too much financial theory so far? Time to get hands-on!**

## 🛠️ Time to build!

### 🔄 Building the TAQ dataset

The key part of this code is understanding how to implement the **AS-OF JOIN** to retrieve our TAQ table. Here are the steps:

- 📂 Upload CSV files (tick-by-tick trades and quotes data) into in-memory kdb+ tables  

- 🔍 Quant Traders are mostly interested in analyzing the bid-ask spread evolution during regular market hours, so we'll apply some filtering.  

- 🚀 Optimization is a key aspect when working with kdb+, that's why we care about it. One way to optimize is by using attributes. In our case, we apply the grouped attribute to a column.

- 🪄 This is where the magic happens: matching timestamps using the AS-OF JOIN operator.

```
taq_table = kx.q.aj(kx.SymbolVector(['sym', 'timestamp']), filtered_trades, filtered_quotes)
```
- 🧹 A bit of cleansing. There may be trades that don't match with any quotes.  

- 🔢 Once we obtain a clean TAQ dataset, we proceed with arithmetic operations to calculate the (effective) bid-ask spread

- 🧬 Integrate everything with your existing Python codebase (Transform KX data types into a pandas DataFrame — a
  game-changer if you're coming from a Python-heavy stack!)  

Translated to code: [bid_ask_spread_dataset_creator.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/bid_ask_spread/bid_ask_spread_dataset_creator.py)

### 📊 Building the Bid-Ask Spread Chart

Here is the code for the chart: [bid_ask_spread_chart_creator.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/bid_ask_spread/bid_ask_spread_chart_creator.py)

### 🐍 Python script to generate the Chart

See: [bid_ask_spread_script.py](https://github.com/fabiogaiera/transitioning-to-kx/blob/master/bid_ask_spread/bid_ask_spread_script.py)

### 📚 Further readings

- [As-of join kdb+ Documentation](https://code.kx.com/q/ref/aj/)  
- [Apply Attributes](https://code.kx.com/pykx/3.1/user-guide/advanced/attributes.html)
- [Bid-Ask Spread Wikipedia Article](https://en.wikipedia.org/wiki/Bid%E2%80%93ask_spread)

Grateful for your time and feedback — it helps me improve.