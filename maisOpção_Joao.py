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

def mais_opcoes():
    print('Essa é a opção mais opções')


#saudacao()



def mais_opcoes():
    print('Mais Opções')
    print('\n')
    while(True):
        print('digite o numero referente a opção desejada:')
        print('\n')
        print('1 - Falar com Atendente Humana')
        print('2 - Voltar para as opções')
        op = int(input())
        if(op == 1):
            print('Essa opção - fala com a Atendente Humana')
            return saudacao()
        elif(op == 2):
            return saudacao()
        else:
            print('Essa opção não é válida')
            return mais_opcoes()
        

mais_opcoes()
