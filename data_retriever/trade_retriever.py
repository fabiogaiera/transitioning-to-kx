import csv
import logging
import sys
from pathlib import Path

from data_retriever.alpaca_rest_client.api_client import get_response
from data_retriever.alpaca_rest_client.dict_parser import fetch_csv_rows_from_trades_dict

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def retrieve_trades_data(symbol, start_date, end_date, destination_folder):
    file_name = "{}_trades.csv".format(symbol)
    full_path = Path(destination_folder) / file_name
    str_full_path = str(full_path)
    base_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/trades"

    with open(str_full_path, 'w', newline='') as file:

        writer = csv.writer(file)
        first_row = ["timestamp", "sym", "price", "size"]
        writer.writerow(first_row)

        next_page_token = None
        first_iteration = True

        while next_page_token or first_iteration:

            if first_iteration:

                parsed_data, next_page_token = get_response(base_url, start_date, end_date)
                rows = fetch_csv_rows_from_trades_dict(parsed_data)
                writer.writerows(rows)
                next_page_token = parsed_data['next_page_token']
                first_iteration = False

            else:

                parsed_data, next_page_token = get_response(base_url, start_date, end_date, next_page_token)
                rows = fetch_csv_rows_from_trades_dict(parsed_data)
                writer.writerows(rows)
                next_page_token = parsed_data['next_page_token']

            logging.info(f"Next Page Token: {next_page_token}")


"""

To use this script, you must setup both environment variables in your OS:
API-KEY
API-SECRET
See https://alpaca.markets to get an API key and its corresponding secret

"""

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python -m data_retriever.trade_retriever <symbol> <yyyy-MM-dd> <yyyy-MM-dd> </path/to/folder>")
        sys.exit(1)
    retrieve_trades_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
