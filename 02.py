nomeProprietario = 'Andre Guilherme Pereira Caetano' #Nome do proprietario
print(f"Boas-vindas o Sorveteria do {nomeProprietario}") #Mensagem de boas vindas
print('-' * 37 + "Cardápio" + '-' * 38)
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |         R$ 6,00        |      R$ 7,00       |       R$ 8,00       |')
print('|      2      |         R$ 10,00       |      R$ 12,00      |       R$ 14,00      |')
print('|      3      |         R$ 14,00       |      R$ 17,00      |       R$ 20,00      |')
print('-' * 83)

while True:
    while True:
        sabor = input("Entre com o sabor desejado (tr/es/pr): ").lower()
        if sabor == "tr" or sabor == "es" or sabor == "pr":
            break
        else:
            print("Sabor inválido. Tente novamente\n")
            continue

    while True:
        numeroBolas = input("Entre com o numero de bolas de sorvete desejado (1/2/3): ")
        if numeroBolas == '1' or numeroBolas == '2' or numeroBolas == '3':
            break
        else:
            print("Número de bolas de sorvete inválido. Tente novamente \n")
            print(f"Entre com o sabor desejado (tr/es/pr): {sabor}")
            continue

#sabor TR
    if sabor == 'tr' and numeroBolas == '1':
        valor = 6
    elif sabor == 'tr' and numeroBolas == '2':
        valor = 10
    elif sabor == 'tr' and numeroBolas == '3':
        valor = 14
    if sabor == 'tr':
        if numeroBolas == '1':
            valor 
    elif sabor == 'pr':
    else:


#Saabor PR
    if sabor == 'pr' and numeroBolas == '1':
        valor = 7
    elif sabor == 'pr' and numeroBolas == '2':
        valor = 12
    elif sabor == 'pr' and numeroBolas == '2':