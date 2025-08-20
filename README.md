# Transitioning to KX: Exploring a Series of Use Cases

While migrating tick data to kdb+, one of the more straightforward aspects is handling raw trade and quote
data. This is because such data can often be re-sourced from market data providers. Therefore, the main focus during
migration lies in rethinking the architecture of the data analytics platform itself.

By shifting to the kdb+ times series database, teams can take full advantage of its performance and expressiveness,
among other powerful features. This transition also enables seamless integration with existing Python-based analytics
platforms through PyKX, resulting in a more flexible and scalable architecture.

**Environment Setup**

Clone repository: `git clone https://github.com/fabiogaiera/transitioning-to-kx-products.git`

Create Virtual Environment: `python -m venv .venv`

Activate Virtual Environment (Linux / Mac): `source .venv/bin/activate`

Activate Virtual Environment (Windows):`.venv\Scripts\activate`

Install Libraries: 

`pip install requests`   
`pip install matplotlib`   
`pip install seaborn`  
`pip install plotly`  

When using a Linux distro check whether **Tkinter** has been installed:

```bash
python -c "import tkinter; tkinter._test()"
```

If test isn't successful, execute

```bash
sudo apt-get install python3-tk  
```

For kdb+ and PyKX installation, check [KX.com](https://kx.com)

**Alpaca Trading API Documentation (Required in case you want to download market data)**

Historical trades (single symbol): [Stock Trades](https://docs.alpaca.markets/reference/stocktradesingle-1)  
Historical quotes (single symbol): [Stock Quotes](https://docs.alpaca.markets/reference/stockquotesingle-1)

**KX Documentation**

Database and Programming Language: [kdb+ and q](https://code.kx.com/q)

Python interface library: [PyKX](https://code.kx.com/pykx)
