nomeProprietario = 'Andre Guilherme Pereira Caetano' #Nome do proprietario
print(f"Boas-vindas o Sorveteria do {nomeProprietario}") #Mensagem de boas vindas
print('-' * 37 + "Cardápio" + '-' * 38)
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |         R$ 6,00        |      R$ 7,00       |       R$ 8,00       |')
print('|      2      |         R$ 11,00       |      R$ 13,00      |       R$ 15,00      |')
print('|      3      |         R$ 15,00       |      R$ 18,00      |       R$ 21,00      |')
print('-' * 83)

total = 0 #Acumula os valores que o cliente vai pagar
while True:
    while True:
        sabor = input("Entre com o sabor desejado (tr/es/pr): ").lower() #lower() possinilita entra com letra maíusculas ou minúsculas
        if sabor == "tr" or sabor == "es" or sabor == "pr": #Verifica se os sabores são validos
            break #Se sim vai continuar o programa
        else:
            print("Sabor inválido. Tente novamente\n")
            continue #Se não vai voltar e perguntar novamente

    while True:
        numeroBolas = input("Entre com o numero de bolas de sorvete desejado (1/2/3): ")
        if numeroBolas == '1' or numeroBolas == '2' or numeroBolas == '3': #Verifica se as quantidade de bolas são validos
            break #Se sim vai continuar o programa
        else:
            print("Número de bolas de sorvete inválido. Tente novamente \n")
            print(f"Entre com o sabor desejado (tr/es/pr): {sabor}")
            continue #Se não vai voltar e perguntar novamente

    if sabor == 'tr': #sabor Tradicional
        if numeroBolas == '1': #Se for 1 bola o valor vai ser 6 reais
            valor = 6
        elif numeroBolas == '2':#Se for 2 bola o valor vai ser 10 reais
            valor = 11
        else: #Se for 3 bola o valor vai ser 14 reais
            valor = 15
    elif sabor == 'pr': #Sabor Premium
        if numeroBolas == '1': #Se for 1 bola o valor vai ser 7 reais
            valor = 7
        elif numeroBolas == '2':#Se for 2 bola o valor vai ser 12 reais
            valor = 13
        else: #Se for 3 bola o valor vai ser 17 reais
            valor = 18
    else: # Sabor Especial
        if numeroBolas == '1': #Se for 1 bola o valor vai ser 8 reais
            valor = 8
        elif numeroBolas == '2':#Se for 2 bola o valor vai ser 14 reais
            valor = 15
        else: #Se for 3 bola o valor vai ser 20 reais
            valor = 21

    total += valor #Vai calcular o total que o cliente vai pagar

    if numeroBolas == '1': #Verifica se o cliente escolheu 1 bolas
        print(f"Você pediu {numeroBolas} bola de sorvete no sabor {sabor}: R$ {valor:.2f}")
        #Se sim vai imprimir a mensagem com "bola"
    else:
        print(f"Você pediu {numeroBolas} bolas de sorvete no sabor {sabor}: R$ {valor:.2f}")
        #Se não vai imprimir a mensagem com "bolas"


    desejaMaisSorvete = input('Deseja mais algunm sorvete (s/digite outra tecla)?: ').lower() ##lower() possinilita entra com letra maíusculas ou minúsculas
    print() #Pular linha
    if desejaMaisSorvete == 's':
        continue
    else:
        print(f'O valor total a ser pago: R${total:.2f} ')
        break
