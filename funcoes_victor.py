def saudacao():
    print('Olá, digite seu nome: ')
    nome = input()
    while(True):
        print('{}, digite o numero referente a opção desejada:'.format(nome))
        print('\n')
        print('1 - Novo pedido')
        print('2 - Alteração de pedido')
        print('3 - Mais opções')
        op = int(input())
        if(op == 1):
            return novo_pedido()
        elif(op == 2):
            return alteracao_pedido()
        elif (op == 3):
            return mais_opcoes()
        else:
            print('Essa opção não existe')

def novo_pedido():
    print('Essa é a opção novo pedido')

def alteracao_pedido():
    print('Essa é a opção alteração pedido')

def mais_opcoes(option):
    borders = ['Catupiry', 'Cheddar', 'Calabresa', 'Queijo', 'Nutela']
    refrigerante = ['Coca-cola', 'Fanta', 'Sprite', 'Kuat', 'Guaraná Antartica']
    if option == 1:
        opt_border = int(input('Deseja adicionar borda?\n(1) SIM\n(2) NÃO'))
        if opt_border == 1:
            print('Escolha o recheio da borda:')
            for i in range(len(borders)):
                print(i,borders[i])
            add_border = int(input())
        more_add = int(input('Deseja adicionar alguma bebida ao seu pedido?\n(1) SIM\n(2) NÃO'))
        if more_add == 1:
            print('Escolha o seu refrigerante:')
            for i in range(len(refrigerante)):
                print(i, refrigerante[i])
            add_refri = int(input())
        return(total_pedido)
    else:
        return(total_pedido)

def total_pedido(total):
    print('Por favor, confirme seu pedido:')
    for i in total:
        print(i)
    answer = int(input('O seu pedido está correto?\n(1) SIM\n(2) NÃO'))
    if answer == 1:
        return(payment)
    else:
        return(alteracao_pedido)

def payment():
    opt_payment = int(input('Qual a forma de pagamento:\n(1) Dinheiro\n(2) Cartão'))
    if opt_payment == 1:
        pay_back = input('Deseja troco?\n(1) SIM\n(2) NÃO')
        if pay_back == 1:
            print('Para quanto deseja o troco?')
            client_money = int(input())
            return(client_money - total_pedido)
    else:
        print('O motoboy levará a máquineta para o pagamento no ato da entrega!')
        print('Agradecemos sua preferência!')

#Vai receber todas as informações do pedido
total = list()