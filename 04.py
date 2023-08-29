lista_colaboradores = [] #Lista vazia

def cadastrar_colaborador(id): #Função para cadastrar um colaborador
    #Solicita as informações do colaborador
    nome = input('Por favor entre com o nome: ')
    setor = input('Por favor entre com o setor: ')
    pagamento = float(input('Por favor entre com o pagamento (R$): '))

    colaborador = {"id":id, "nome":nome, "setor":setor, "pagamento":pagamento} #Pega as informações e é colocado dentro de uma biblioteca de nome colaborador
    lista_colaboradores.append(colaborador) #Adiciona o colaborador a lista

def consultar_colaboradores(): #Função para consultar um colaboradores
   while True:
       try:
           print('*' * 80)
           print('-' * 25, ' MENU CONSULTAR COLABORADOR ', '-' * 25)
           print('Escolha a opção desejada:')
           print('1-Consultar Todas os Colaborador')
           print('2-Consultar Colaborador por id')
           print('3-Consultar Colaborador(es) por setor')
           print('4-Retornar')
           opcao = int(input('>>'))

           if opcao == 1:
               # Consultar todos os colaboradores
               print('-' * 20)
               for colaborador in lista_colaboradores:  # Percorre todos os colaboradores dentro da lista de colaboradores
                   print(f'id : {colaborador["id"]}')  # Imprime o ID do colaborador
                   print(f'nome : {colaborador["nome"]}')  # Imprime o NOME do colaborador
                   print(f'setor : {colaborador["setor"]}')  # Imprime o SETOR do colaborador
                   print(f'pagamento : {colaborador["pagamento"]}')  # Imprime o PAGAMENTO do colaborador
               print('-' * 20)
           elif opcao == 2:
               # Consultar por id
               id_consultado = int(input('Digite o id do colaborador: '))
               print('-' * 20)
               for colaborador in lista_colaboradores:  # Percorre todos os colaboradores dentro da lista de colaboradores
                   if colaborador["id"] == id_consultado:  # Compara se o ID CONSULTADO existe dentro da lista
                       print(f'id : {colaborador["id"]}')  # Imprime o ID do colaborador
                       print(f'nome : {colaborador["nome"]}')  # Imprime o NOME do colaborador
                       print(f'setor : {colaborador["setor"]}')  # Imprime o SETOR do colaborador
                       print(f'pagamento : {colaborador["pagamento"]}')  # Imprime o PAGAMENTO do colaborador
                   else:  # Se não vai imprimir a mensagem
                       print('Colaborador não encontrado.')
               print('-' * 20)
           elif opcao == 3:
               # Consultar por Setor
               setor_consultado = input('Digite o setor do(s) colaborador(es): ')
               print('-' * 20)
               for colaborador in lista_colaboradores:  #Percorre todos os colaboradores dentro da lista de colaboradores
                   if colaborador["setor"] == setor_consultado:  #Compara se o SETOR CONSULTADO existe dentro da lista
                       print(f'id : {colaborador["id"]}')  #Imprime o ID do colaborador
                       print(f'nome : {colaborador["nome"]}')  # Imprime o NOME do colaborador
                       print(f'setor : {colaborador["setor"]}')  # Imprime o SETOR do colaborador
                       print(f'pagamento : {colaborador["pagamento"]}')  # Imprime o PAGAMENTO do colaborador
                       print('-' * 20)
           elif opcao == 4:
               # Retornar ao menu principal
               break
           else:
               print('Opção inválida.\n')
               continue
       except ValueError:
           print('Opção inválida.\n')

def remover_colaborador():
    print('*' * 80)
    print('-' * 26, ' MENU REMOVER COLABORADOR ', '-' * 26)
    id_remover = int(input('Digite o id do colaborador a ser removido: '))
    for colaborador in lista_colaboradores:  #Percorre todos os colaboradores dentro da lista de colaboradores
        if colaborador["id"] == id_remover:  #Compara se o ID existe dentro da lista
            lista_colaboradores.remove(colaborador)  #Remove o ID da lista

def main():
    id_global = 0 #Retem o ID anterior
    nomeEmpresa = 'Andre Guilherme Pereira Caetano'
    print(f'Bem-vindo ao Controle de Colaboradores do {nomeEmpresa}')
    while True:
        while True:
            try:
                print('*' * 80)
                print('-' * 31, ' MENU PRINCIPAL ', '-' * 31)
                print('Escolha a opção desejado:')
                print('1-Cadastrar colaborador')
                print('2-Consultar Colaborador(es)')
                print('3-Remover Colaborador')
                print('4-Sair')
                opcaoMenuPrincipal = int(input('>>'))
                if opcaoMenuPrincipal == 1 or opcaoMenuPrincipal == 2 or opcaoMenuPrincipal == 3 or opcaoMenuPrincipal == 4: #Verifica se a opção é valida
                    break
                else:
                    print('Opção inválida.\n')
                    continue

            except ValueError: #Verifica se é um número
                print('Opção inválida.\n')


        if opcaoMenuPrincipal == 1:  #Cadastrar Colaboradores
            id_global += 1 #Soma mais um ID no ID anterior e cria o novo ID
            print('*' * 80)
            print('-' * 25, ' MENU CADASTRAR COLABORADOR ', '-' * 25)
            print(f'id do colaborador {id_global}') #Imprime o ID do colaborador
            cadastrar_colaborador(id_global)
        elif opcaoMenuPrincipal == 2:  #Consultar Colaborador(es)
            consultar_colaboradores()
        elif opcaoMenuPrincipal == 3: #Remover Colaborador
            remover_colaborador()
        elif opcaoMenuPrincipal == 4: #Sir do sistema
            break
main()
