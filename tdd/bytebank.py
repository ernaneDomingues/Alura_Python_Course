from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_sobrenome = nome_completo.split(' ')
        return nome_sobrenome[-1]

    def _verifica_se_e_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._verifica_se_e_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        # valor = self._salario * 0.1
        if self._salario > 1000:
            raise Exception('O funcionário não tem direito a bônus')
        return self._salario * 0.1

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'