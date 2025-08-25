from historical_database.query_engine import run_query
from historical_database.historical_database_creator import create_or_update_database

if __name__ == "__main__":
    #    if len(sys.argv) != 4:
    #        print("Incorrect parameters")
    #        sys.exit(1)

    # Path to the CSV file
    trades_data = "/home/fabio/data/2025.04.09_AAPL_trades.csv"
    database_path = "/home/fabio/db"

    # Daylight Saving Time (DST) for Eastern Time (ET) in the U.S. as we're analyzing the IBM ticker.
    # Timestamp data type in q
    market_open = '2025.04.09D13:30:00.000000000'
    market_close = '2025.04.09D20:00:00.000000000'

    # create_or_update_database(trades_data, database_path, market_open, market_close)
    run_query(database_path)
