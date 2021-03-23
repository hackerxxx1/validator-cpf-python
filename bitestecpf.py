import pytest
from bicpf import BrazilianCpfValidationTests


def testp(): #teste padrao de cpf para testar se esta no modo certo

    cpf=BrazilianCpfValidationTests()

    casos=[
        '123.456.789-09',
        '12345678909',
    ]

    for caso in casos:
        cpf(caso)
        assert not cpf.tests


def testd(): #teste digitos corretos

    cpf=BrazilianCpfValidationTests()

    casos=[
        '123.456.789-19',
        '12345678919',
    ]

    for caso in casos:
        cpf(caso)
        assert 'checkdigits' in cpf.tests

def testlen(): #teste tamanho correto

    cpf=BrazilianCpfValidationTests()

    casos=[
        '1234',
        '123456789012',
    ]

    for caso in casos:
        cpf(caso)
        assert 'length' in cpf.tests

def testdln(): #teste letra numero ou digitos corretos

    cpf=BrazilianCpfValidationTests()

    casos=[
        'ABCD5678901',
        '1234567ABCD',
    ]

    for caso in casos:
        cpf(caso)
        assert 'digits' in cpf.tests

def testfor(): #teste de formatação do cpf 

    cpf=BrazilianCpfValidationTests()

    casos=[
        '123456789-01',
        '123.456.78901',
        '123.456.789.01',
    ]

    for caso in casos:
        cpf(caso)
        assert 'charformat' in cpf.tests