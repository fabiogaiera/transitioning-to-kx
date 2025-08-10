def adjust_datetime(expression):
    expression = expression.replace('Z', '').replace('-', '.').replace('T', 'D')
    if len(expression) < 29:
        expression = expression.ljust(29, '0')
    return expression


def fetch_csv_rows_from_quotes_dict(parsed_data_as_dict):

    symbol = parsed_data_as_dict['symbol']
    quotes = parsed_data_as_dict['quotes']
    lst = []

    for elem in quotes:
        # Adjusting datetime for kdb+ type conversion on a later stage
        datetime = adjust_datetime(elem['t'])
        nested_list = [datetime, symbol, elem['bp'], elem['bs'], elem['ap'], elem['as']]
        lst.append(nested_list)

    return lst


def fetch_csv_rows_from_trades_dict(parsed_data_as_dict):

    symbol = parsed_data_as_dict['symbol']
    trades = parsed_data_as_dict['trades']
    lst = []

    for elem in trades:
        # Adjusting datetime for kdb+ type conversion on a later stage
        datetime = adjust_datetime(elem['t'])
        nested_list = [datetime, symbol, elem['p'], elem['s']]
        lst.append(nested_list)

    return lst
