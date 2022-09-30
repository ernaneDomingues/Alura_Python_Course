import re


class ExtractorURL:
    def __init__(self, url):
        self.url = self.clear_url(url)
        self.url_validation()

    def clear_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def url_validation(self):
        if not self.url:
            raise ValueError("Empty URL")
        standard_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = standard_url.match(self.url)
        if not match:
            raise ValueError('Invalid URL')


    def get_url_base(self):
        return self.url[:self.url.find('?')]

    def get_url_parameters(self):
        return self.url[self.url.find('?') + 1:]

    def get_value_parameter(self, query_parameter):
        ampersand_index = self.get_url_parameters().find('&', (
                    self.get_url_parameters().find(query_parameter) + len(query_parameter) + 1))
        if ampersand_index == -1:
            return self.get_url_parameters()[
                   self.get_url_parameters().find(query_parameter) + len(query_parameter) + 1:]
        else:
            return self.get_url_parameters()[
                   self.get_url_parameters().find(query_parameter) + len(query_parameter) + 1:ampersand_index]

    def get_currency_coverter(self, currency_value):
        source_currency = self.get_value_parameter('sourcerCurrency')
        target_currency = self.get_value_parameter('targetCurrency')
        currency_quantity = self.get_value_parameter('value')
        return f'The value converted from {currency_quantity} {source_currency} to {target_currency} is ${int(currency_quantity)/currency_value}.'


    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

extractor_url = ExtractorURL('https://bytebank.com/cambio?sourceCurrency=BRL&targetCurrency=USD&value=100')
print(extractor_url.get_currency_coverter(5.4))

