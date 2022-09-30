import re


address = 'Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120'

standard = re.compile('[0-9]{5}[-]?[0-9]{3}')

cep_search = standard.search(address)
if cep_search:
    cep = cep_search.group()
    print(cep)