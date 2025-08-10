class URLComposer:

    def __init__(self, base_url, start_date, end_date):
        self.url = "{}?start={}&end={}&limit=1000".format(base_url, start_date, end_date)

    def get_string_url(self):
        return self.url

    def get_string_url_with_next_page_token(self, next_page_token):
        return "{}&page_token={}".format(self.url, next_page_token)
