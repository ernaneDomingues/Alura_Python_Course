url = 'https://bytebank.com/cambio?sourceCurrency=real&targetCurrency=dolar&value=100'

url = url.replace(' ', '')
if len(url) == 0:
    raise ValueError('Empty URL')

url_base = url[:url.find('?')]
url_parameters = url[url.find('?') + 1:]

query_source_currency = 'sourceCurrency'
query_target_currency = 'targetCurrency'
query_value = 'value'

source_currency = url_parameters[url_parameters.find(query_source_currency)+len(query_source_currency)+1:url_parameters.find('&', url_parameters.find(query_source_currency))]
target_currency = url_parameters[url_parameters.find(query_target_currency)+len(query_target_currency)+1:url_parameters.find('&', url_parameters.find(query_target_currency))]
value = url_parameters[url_parameters.find(query_value)+len(query_value)+1:]

print(f'moeda de origem: {source_currency}')
print(f'moeda destino: {target_currency}')
print(f'valor a ser convertido: {value}')