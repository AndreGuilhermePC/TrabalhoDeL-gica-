nome_dono = 'Andre Guilherme Pereira Caetano' #nome do dono
print(f'Bem-vindo a Loja do {nome_dono}') #Mensagens de boas vindas

valor_unidade = float(input('Entre com o valor do produto: ')) #entrada do valor da unidade
quantidade_unidade = int(input('Entre com a quantidade do produto: ')) #entrada da quantidade de unidades

valor_total_sem_desconto = valor_unidade * quantidade_unidade #calcula o valor total sem desconto

if quantidade_unidade < 200:
    porcentagem_desconto = 0  # Se quantidade for menor que 200 o desconto será de 0%
elif ((quantidade_unidade >= 200) and (quantidade_unidade < 1000)):
    porcentagem_desconto = 5 #Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%
elif((quantidade_unidade >= 1000) and (quantidade_unidade < 2000)):
    porcentagem_desconto = 10 # Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%
else:
    porcentagem_desconto = 15 #Se quantidade for igual ou maior que 2000 o desconto será de 15%%

valor_total_com_desconto = valor - (valor * porcentagem_desconto / 100) #Calcula o valor com desconto

print(f'O valor SEM desconto: R$ {valor_total_sem_desconto:.2f}') #Imprime o valoe sem desconto
print(f'O valor COM desconto: R$ {valor_total_com_desconto:.2f}') #Imprime o valoe com desconto
