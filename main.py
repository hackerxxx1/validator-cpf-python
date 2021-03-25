def validat(value):
#Validação dos CPFs inválidos conhecidos de acordo com o algoritmo de criação do cpf
    if (value[0]==value[1]) and (value[1]==value[2]) and (value[2]==value[3]) and (value[3]==value[4]) and (value[4]==value[5]) and (value[5]==value[6]) and (value[6]==value[7]) and (value[7]==value[8]) and (value[8]==value[9]) and (value[9]==value[10]):
         print("cpf invalido")
    else:
        soma1=int(value[0])*10+int(value[1])*9+int(value[2])*8+int(value[3])*7+int(value[4])*6+int(value[5])*5+int(value[6])*4+int(value[7])*3+int(value[8])*2
        resto1 = (soma1*10) % 11
        if (resto1==10):
            resto1=0
            pass
        soma2 = int(value[0])*11+int(value[1])*10+int(value[2])*9+int(value[3])*8+int(value[4])*7+int(value[5])*6+int(value[6])*5+int(value[7])*4+int(value[8])*3+int(value[9])*2
        resto2 = (soma2*10) % 11
        if (resto2==10):
            resto2=0
            pass
        if (resto1==int(value[9])) and (resto2==int(value[10])): 
            print("cpf valido")
        else:
            print("cpf invalido")
            pass
        pass
    pass
#Começo do programa em si    
print("para sair digite exit")
cpf1=input("digite o cpf que deseja consultar:")
while (cpf1.upper() != "EXIT"):
    cpf=''.join(char for char in cpf1 if char not in "--.")
    if cpf.isdigit() and len(cpf)==11:
        validat(cpf)
        aux=input("deseja continuar?(sim/nao)")
        if aux.upper() =="NAO" or aux.upper() == "EXIT":
        	cpf1="exit"
        	pass
        elif aux.upper() == "SIM":
            cpf1=input("digite o cpf que deseja consultar:")
        else:
            print("nao foi possivel entender o comando")
            cpf1="exit"
    else:
        print("syntax error: cpf invalido ou escrito errado")
        print("tente novamente")
        cpf1=input("digite o cpf que deseja consultar:")
        pass
    pass    
	