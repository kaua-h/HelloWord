print("Bem Vindo!!!")
trim1 = float(input("Digite a nota do aluno do 1 trimestre: "))
trim2 = float(input("Digite a nota do aluno do 2 trimestre: "))
trim3 = float(input("Digite a nota do aluno do 3 trimestre: "))
soma = trim1 + trim2 + trim3
média = soma / 3
print("A média do aluno é {:.1f}".format(média))