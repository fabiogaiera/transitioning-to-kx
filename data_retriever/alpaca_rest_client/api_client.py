import json
import os

import requests

from data_retriever.alpaca_rest_client.url_composer import URLComposer

headers = {

    "accept": "application/json",
    "APCA-API-KEY-ID": os.getenv("API_KEY"),
    "APCA-API-SECRET-KEY": os.getenv("API_SECRET")

}


def get_response(base_url, start_date, end_date, next_page_token=None):

    url_with_params = URLComposer(base_url, start_date, end_date)

    if next_page_token:

        response = requests.get(url_with_params.get_string_url_with_next_page_token(next_page_token), headers=headers)
        parsed_data = json.loads(response.text)
        next_page_token = parsed_data['next_page_token']

    else:

        response = requests.get(url_with_params.get_string_url(), headers=headers)
        parsed_data = json.loads(response.text)
        next_page_token = parsed_data['next_page_token']

    return parsed_data, next_page_token
