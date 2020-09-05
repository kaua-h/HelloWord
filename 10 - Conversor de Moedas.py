real = float(input("Digite o valor desejado: "))
dolar = real / 5.45
euro = real / 6.39
print('Com R$ {:.2f} você pode comprar U$ - {:.2f} dólares e EUR$ - {:.2f} euros'.format(real, dolar, euro))