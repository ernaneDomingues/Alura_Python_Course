import requests

class ZipCodeSearch:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_validation(cep):
            self.cep = cep
        else:
            raise ValueError('Invalid CEP!')

    def __str__(self):
        return self.cep_format()

    def cep_validation(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_format(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def zip_code_search(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        address = r.json()
        if r.status_code == 200:
            if 'erro' in address:
                return 'Invalid CEP!'
            else:
                return address
        elif r.status_code == 404:
            print('Not Found.')