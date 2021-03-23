from django.core.exceptions import ValidationError
from bicpf import BrazilianCpfValidationTests

def validat(value):
	cpf=BrazilianCpfValidationTests()
	cpf(value)
	for test in cpf.tests:
		raise ValidationError(cpf,GetMessage(test), test)
		pass
	pass
		
cpf1=string(input("digite o cpf que deseja consultar:"))

if (validat(cpf1)):
    print("sucesso")
	