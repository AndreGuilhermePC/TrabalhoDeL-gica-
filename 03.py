nomeDoPetshop = 'Andre Guilherme Pereira Caetano'
print(f'Boas-vindas a petshop do {nomeDoPetshop}') #cabeçalho
def cachorro_peso(): #Função para informar o valor peso
    while True:
       try:
           peso = float(input("Entre com o peso do cachorro: "))
           if peso > 50: #Se for Maior 50 kg
               print('Não aceitamos cachorros tão grandes.')
               print('Por favor entre com o peso do cachorro novamente.\n')
               continue
           else: #Se for menor de 50 kg
               break
       except ValueError: #Se digitar valor não numérico
           print('Você digitou um valor não numérico.')
           print('Por favor entre com o peso do cachorro novamente.\n')

    if peso < 3: #Se o peso do cachorro for menor que 2kg
        valorPeso = 40 #Valor vai ser de R$ 40,00
    elif peso <= 10: #Se o peso do cachorro for maior que 3kg e menor ou igual a 10kg
        valorPeso = 50 #Valor vai ser de R$ 50,00
    elif peso <= 30: #Se o peso do cachorro for maior que 10kg e menor ou igual a 30kg
        valorPeso = 60 #Valor vai ser de R$ 60,00
    else: #Se o peso do cachorro for maior que 50kg
        valorPeso = 70 #Valor vai ser de R$ 70,00

    return valorPeso #Retorna o valor correspondente ao peso do cachorro

def cachorro_pelo(): #Função para calcular o multiplicador pelo
    while True:
        print('Entre com o pelo do cachorro') #Cabeçalho
        print('c - Pelo Curto')
        print('m - Pelo Médio')
        print('l - Pelo Longo')
        pelo = input('>>').lower() #lower() possinilita entra com letra maiúsculas ou minúsculas
        if pelo == 'c' or pelo == 'm' or pelo == 'l': #Verifica se "pelo" é "c", "m" ou "l"
            break #Se sim vai sair do loop
        else:
            continue #Se não vai continuar e vai perguntar novamente
    if pelo == 'c': #Se for o "pelo" for "c"
        return 1 #Múltiplo de 1.0
    elif pelo == 'm': #Se for o "pelo" for "m"
        return 1.5 #Múltiplo de 1.5
    else: #Se for o "pelo" for "l"
        return 2 #Múltiplo de 2

def cachorro_extra(): #Função para calcular o valor extra
    valorExtra = 0 #Sola o total
    while True:
        try:
            print('\nDeseja adicionar mais algum serviço?\n', #Cabeçalho
                  '1 - Corte de Unhas - R$ 10,00\n',
                  '2 - Escovar Dentes  - R$ 12,00\n',
                  '3 - Limpeza de Orelhas - R$ 15,00\n',
                  '0 - Não desejo mais nada')
            extra = int(input('>>')) #Atribui a resposta a variável "extra"
            if extra == 1: #Verifica se a variavel "extra" é igual a "1"
                valorExtra += 10 #Vai ser atribuído 10 na variavel "total" e somado ao valor já existente na variavel "valorExtra"
                continue #Repete o cabeçalho
            elif extra == 2: #Verifica se a variável "extra" é igual a "2"
                valorExtra += 12 #Vai ser atribuido 12 na variável "total" e somado ao valor já existente na variavel "valorExtra"
                continue #Repete o cabeçalho
            elif extra == 3: #Verifica se a variavel "extra" é igual a "3"
                valorExtra += 15 #Vai ser atribuido 15 na variavel "total" e somado ao valor já existente na variavel "valorExtra"
                continue #Repete o cabeçalho
            else: #Verifica se a variavel "extra" é igual a "0"
                break #Sai do loop
        except ValueError: #Se digitar valor não numérico
            print('Você digitou um valor não numérico.')
            print('Por favor entre com um valor numérico.\n')
    return valorExtra #retorna o totalExtra

def main(): #Função Main()
    totalBase = cachorro_peso() #Estância a função "cachorro_peso()" e atribuindo a variavel "base"
    print()
    totalMultiplicador = cachorro_pelo() #Estância a função "cachorro_pelo()" e atribuindo a variavel "multiplicador"
    totalExtra = cachorro_extra() #Estância a função "cachorro_extra()" e atribuindo a variavel "totalExtra"
    totalPagar = totalBase * totalMultiplicador + totalExtra #Calaculo do total que o cliente vai pagar
    print(f'Total a pagar(R$): {totalPagar:.2f} (peso: {totalBase} * pelo: {totalMultiplicador} + adicional(is): {totalExtra})') #Imprime o total a pagar informando valor do peso, valor do multiplo e os valores dos adicionais

main() #Executa a função "main()'
