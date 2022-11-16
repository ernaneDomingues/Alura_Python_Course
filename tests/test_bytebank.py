from tdd.bytebank import Funcionario
import pytest
from pytest import mark
class TestClass:
    @mark.idade
    def test_quando_idade_recebe_07_07_2000_deve_retornar_22(self):
        entrada = '07/07/2000' #Given
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1212)
        resultado = funcionario_teste.idade() #When

        assert resultado == esperado #Then

    @mark.sobrenome
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '07/07/2000', 1212)
        resultado = lucas.sobrenome()

        assert resultado == esperado

    @mark.decrescimo_de_salario
    def test_quando_salario_100000_deve_ter_decrescimo_de_10_porcento_deve_retornar_90000(self):
        entrada = 100000
        entrada_diretor = 'Paulo Bragança'
        esperado = 90000


        funcionario_teste = Funcionario(entrada_diretor, '07/07/2000', entrada)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_calcula_bonus_do_funcionario_quando_salario_menor_de_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '07/07/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1001

            funcionario_teste = Funcionario('Teste', '07/07/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado