#Login e Senha - Básico
n1 = input("Qual seu nome? ")
print ("Olá, {}, entre em sua conta de administrador: ".format(n1))
L1 = str(input("Digite seu Login: "))
L2 = int(input("Digite sua senha: "))
if L1 == "Admin" and L2 == 2020:
    print("Seja Bem Vindo, {}.".format(n1))
else:
    print("Login ou senha incorreta")
