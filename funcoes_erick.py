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
    global tamanho
    global cardapio
    global sabores
    print('O que você deseja alterar?\nDigite o numero referente a opção desejada')
    
    print('1 - Alterar tamanho')
    print('2 - Alterar sabores')
    print('3 - Alterar extras')
    op = input()
    if(op == '1'):
        return alterar_tamanho()
    elif(op == '2'):
        return alterar_sabores(tamanho,cardapio)
    elif(op == '3'):
        return alterar_extras()
    else:
        print('Essa opção não existe')
        alteracao_pedido()

def alterar_tamanho():
    global tamanho
    print('Para qual tamanho deseja alterar? Digite a opção desejada:')
    print('1 - P\n2 - M\n3 - G')
    op = input()
    if(op == '1'):
        tamanho = 'P'
        return
    elif(op == '2'):
        tamanho = 'M'
        return
    elif(op == '3'):
        tamanho = 'G'
        return
    else:
        print('Essa opção não existe')
        alterar_tamanho()


def alterar_sabores(tamanho, cardapio):
    global menu
    global sabores
    if tamanho == 'P':
        print(cardapio)
        print('Escolha o numero referente a novo sabor:')
        while(True):    
            sabor = input()
            escolha = int(sabor)
            if escolha in menu:
                sabores[0] = sabor
                return
            else:
                print('Essa opção não está dentro das opções do menu. Escolha novamente:')
    elif tamanho == 'M':
        if len(sabores)==1:
            print(cardapio)
            print('Escolha o numero referente a novo sabor:')
            while(True):    
                sabor = input()
                escolha = int(sabor)
                if escolha in menu:
                    sabores[0] = sabor
                    return
                else:
                    print('Essa opção não está dentro das opções do menu. Escolha novamente:')
        elif len(sabores)==2:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois =  int(sabores[1])
            print('1 - {} '.format(menu[saborum]))
            print('2 - {} '.format(menu[sabordois]))
            print('3 - Os dois sabores')
            op = input()
            if(op == '1'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:                
                        sabores[0] = sabor
                        return
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                i = 0
                while(i<2):
                    print(cardapio)
                    print('Escolha seu {}º novo sabor'.format(i+1))
                    
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i+=1   
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            else:
                print('Opção invalida')
                alterar_sabores(tamanho,cardapio)
    elif tamanho == 'G':
        if len(sabores)==1:
            print('Escolha o numero referente a novo sabor:')
            print(cardapio)
            while(True):
                sabor = input()
                escolha = int(sabor)
                if escolha in menu:
                    sabores.pop(0)
                    sabores.insert(0,sabor)
                    return
                else:
                    print('Essa opção não está dentro das opções do menu. Escolha novamente:')            
        
        elif len(sabores)==2:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois =  int(sabores[1])
            print('1 - {} '.format(menu[saborum]))
            print('2 - {} '.format(menu[sabordois]))
            print('3 - OS DOIS SABORES')
            op = input()
            if(op == '1'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        # sabores.pop(0)
                        # sabores.insert(0,sabor)
                        return
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                i = 0
                while(i<2):
                    print(cardapio)
                    print('Escolha seu {}º novo sabor'.format(i+1))
                    
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i+=1
                        
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
                        
            else:
                print('Opção invalida')
                alterar_sabores(tamanho,cardapio)
        elif len(sabores)==3:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois =  int(sabores[1])
            sabortres =  int(sabores[2])
            print('1 - {} '.format(menu[saborum]))
            print('2 - {} '.format(menu[sabordois]))
            print('3 - {} '.format(menu[sabortres]))
            print('4 - OS TRÊS SABORES')
            op = input()
            if(op == '1'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):    
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        return
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                print(cardapio)
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[2] = sabor
                        return    
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '4'):
                i=0
                while(i<3):
                    print(cardapio)
                    print('Escolha seu {}º novo sabor'.format(i+1))
                    
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i+=1
                    else:
                        print('Essa opção não está dentro das opções do menu. Escolha novamente:')

            else:
                print('Opção invalida')
                alterar_sabores(tamanho,cardapio)

def mais_opcoes():
    print('Essa é a opção mais opções')
def alterar_extras():
    return

cardapio = ('NOSSAS OPÇÕES DE SABORES\n\n'
                '01. AMERICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, BACON, CALABRESA, OVOS E CEBOLA\n'
                '02. APRESUNTADA\n'
                'MOLHO DE TOMATE, PRESUNTO E MUSSARELA\n'
                '03. CROCANTE\n'
                'MOLHO DE TOMATE, MUSSARELA (2 CAMADAS), CATUPIRY, BATATA PALHA (DEPOIS DE ASSADA)\n'
                '04. MILHO\n'
                'MOLHO DE TOMATE, MUSSARELA E MILHO\n'
                '05. MUSSARELA\n'
                'MOLHO DE TOMATE E MUSSARELA (2 CAMADAS)\n'
                '06. TRADICIONAL\n'
                'MOLHO DE TOMATE, PRESUNTO, TOMATES E MUSSARELA\n'
                '10. ALHO E OLEO\n'
                'MOLHO DE TOMATE, MUSSARELA, ALHO E AZEITE DE OLIVA\n'
                '11. BACON\n'
                'MOLHO DE TOMATE, MUSSARELA E BACON\n'
                '12. CALABRESA\n'
                'MOLHO DE TOMATE, MUSSARELA E CALABRESA\n'
                '13. ESCAROLA\n'
                'MOLHO DE TOMATE, ESCAROLA (REFOGADA), BACON, ALHO (OPCIONAL) E MUSSARELA\n'
                '14. FRANGO\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO E REFOGADO\n'
                '15. FRANGO C/ CATUPIRY\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO AO MOLHO DE CATUPIRY\n'
                '16. FRAN-MILHO\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO AO MOLHO E MILHO\n'
                '18. MARGUERITA\n'
                'MOLHO DE TOMATE, TOMATES, PARMESAO, MANJERICAO, AZEITE DE OLIVA E MUSSARELA\n'
                '19. MEXICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA RALADA, PIMENTAO VERDE E PIMENTA-CALABRESA\n'
                '20. NAPOLITANA\n'
                'MOLHO DE TOMATE, TOMATES, PROVOLONE E MUSSARELA\n'
                '21. PAULISTA\n'
                'MOLHO DE TOMATE, MUSSARELA, MILHO, ERVILHA, PALMITO E AZEITONAS\n'
                '22. PORTUGUESA\n'
                'MOLHO DE TOMATE, PRESUNTO, MUSSARELA, OVOS, CEBOLA E AZEITONAS\n'
                '23. TOSCANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA E OVOS\n'
                '30. ALICHE\n'
                'MOLHO DE TOMATE, MUSSARELA, ALICHE E TOMATES\n')

menu = {
    1:"AMERICANA",
    2:"APRESUNTADA",
    3:"CROCANTE",
    4:"MILHO",
    5:"MUSSARELA",
    6:"TRADICIONAL",
    10:"ALHO E ÓLEO",
    11:"BACON",
    12:"CALABRESA",
    13:"ESCAROLA",
    14:"FRANGO",
    15:"FRANGO C/ CATUPIRY",
    16:"FRAN-MILHO",
    18:"MARGUERITA",
    19:"MEXICANA",
    20:"NAPOLITANA",
    21:"PAULISTA",
    22:"PORTUGUESA",
    23:"TOSCANA",
    30:"ALICHE"
}


tamanho = ''
recheio_um = ''
recheio_dois = ''
recheio_tres = ''
border = ''
refri = ''
sabores = []

sabores.insert(0,'1')
sabores.insert(1,'2')
sabores.insert(1,'3')

#recheio_um = menu[5]
#print(menu[1])
#print(recheio_um)
#print(sabores[0])
# print('Tamanho é : {}'.format(tamanho))
# alterar_tamanho()
# print('Tamanho é : {}'.format(tamanho))
tamanho = 'G'
print(sabores)
saudacao()
print(tamanho)
print(sabores)