import wppbot
import time
bot = wppbot.wppbot('Robot')


def saudacao():
    print('Olá, digite seu nome: ')
    nome = input()
    while(True):
        print('{}, digite o numero referente a opção desejada:'.format(nome))
        print('\n')
        print('(1) - Novo pedido')              
        print('(2) - Alteração de pedido')
        print('(3) - Mais opções')
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
    """Realiza todo o tratamento de um novo pedido"""

    global tamanho

    # Tratamento de decisoes no pedido
    while(True):
        print('Qual o tamanho da sua pizza?\n'
              '(1).  PEQUENA\n'
              '(2).  MÉDIA\n'
              '(3).  GRANDE')

        option = input()
        if option.isnumeric():
            option = int(option)
            if option == 1:
                return um_sabor(option)

            elif option == 2:
                opt_sabor = input(
                    'Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores\n')
                if opt_sabor == 1:
                    return um_sabor(option)
                else:
                    return dois_sabores(option)

            elif option == 3:
                opt_sabor = input('Deseja sua pizza com quantos sabores?\n'
                                  '(1) 1 Sabor\n'
                                  '(2) 2 Sabores\n'
                                  '(3) 3 Sabores\n')
                if option == 1:
                    return um_sabor(option)
                elif option == 2:
                    return dois_sabores(option)
                elif option == 3:
                    return tres_sabores()
        elif option.isalpha():
            option = option.upper()
            if option == 'PEQUENA':
                return um_sabor(option)

            elif option == 'MEDIA':
                opt_sabor = input(
                    'Deseja sua pizza com quantos sabores?\n(1) 1 Sabor\n(2) 2 Sabores\n')
                if opt_sabor == 1:
                    return um_sabor(option)
                else:
                    return dois_sabores(option)

            elif option == 'GRANDE':
                opt_sabor = input('Deseja sua pizza com quantos sabores?\n'
                                  '(1) 1 Sabor\n'
                                  '(2) 2 Sabores\n'
                                  '(3) 3 Sabores\n')


def alteracao_pedido():
    global tamanho
    global sabores
    print('O que você deseja alterar?\nDigite o numero referente a opção desejada')

    print('(1) - Alterar tamanho')
    print('(2) - Alterar sabores')
    print('(3) - Alterar extras')
    op = input()
    if(op == '1'):
        return alterar_tamanho()
    elif(op == '2'):
        return alterar_sabores(tamanho)
    elif(op == '3'):
        return alterar_extras()
    else:
        print('Essa opção não existe')
        alteracao_pedido()


def alterar_tamanho():
    global tamanho
    print('Para qual tamanho deseja alterar? Digite a opção desejada:')
    print('1 - Pequena\n2 - Média\n3 - Grande')
    op = input()
    if(op == '1'):
        tamanho = 'Pequena'
        return
    elif(op == '2'):
        tamanho = 'Media'
        return
    elif(op == '3'):
        tamanho = 'Grande'
        return
    else:
        print('Essa opção não existe')
        alterar_tamanho()


def alterar_sabores(tamanho):
    global menu
    global sabores
    if tamanho == 'Pequena':
        show_cardapio()
        print('Escolha o numero referente a novo sabor:')
        while(True):
            sabor = input()
            escolha = int(sabor)
            if escolha in menu:
                sabores[0] = sabor
                return
            else:
                print(
                    'Essa opção não está dentro das opções do menu. Escolha novamente:')
    elif tamanho == 'Media':
        if len(sabores) == 1:
            show_cardapio()
            print('Escolha o numero referente a novo sabor:')
            while(True):
                sabor = input()
                escolha = int(sabor)
                if escolha in menu:
                    sabores[0] = sabor
                    return
                else:
                    print(
                        'Essa opção não está dentro das opções do menu. Escolha novamente:')
        elif len(sabores) == 2:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois = int(sabores[1])
            print('(1) - {} '.format(menu[saborum]))
            print('(2) - {} '.format(menu[sabordois]))
            print('(3) - Os dois sabores')
            op = input()
            if(op == '1'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                i = 0
                while(i < 2):
                    show_cardapio()
                    print('Escolha seu {}º novo sabor'.format(i+1))

                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i += 1
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            else:
                print('Opção invalida')
                alterar_sabores(tamanho)
    elif tamanho == 'Grande':
        if len(sabores) == 1:
            print('Escolha o numero referente a novo sabor:')
            show_cardapio()
            while(True):
                sabor = input()
                escolha = int(sabor)
                if escolha in menu:
                    sabores.pop(0)
                    sabores.insert(0, sabor)
                    return
                else:
                    print(
                        'Essa opção não está dentro das opções do menu. Escolha novamente:')

        elif len(sabores) == 2:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois = int(sabores[1])
            print('(1) - {} '.format(menu[saborum]))
            print('(2) - {} '.format(menu[sabordois]))
            print('(3) - OS DOIS SABORES')
            op = input()
            if(op == '1'):
                show_cardapio()
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
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                i = 0
                while(i < 2):
                    show_cardapio()
                    print('Escolha seu {}º novo sabor'.format(i+1))

                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i += 1

                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')

            else:
                print('Opção invalida')
                alterar_sabores(tamanho)
        elif len(sabores) == 3:
            print('Você quer alterar qual sabor:')
            saborum = int(sabores[0])
            sabordois = int(sabores[1])
            sabortres = int(sabores[2])
            print('(1) - {} '.format(menu[saborum]))
            print('(2) - {} '.format(menu[sabordois]))
            print('(3) - {} '.format(menu[sabortres]))
            print('(4) - OS TRÊS SABORES')
            op = input()
            if(op == '1'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[0] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '2'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[1] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '3'):
                show_cardapio()
                print('Escolha seu novo sabor')
                while(True):
                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[2] = sabor
                        return
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')
            elif(op == '4'):
                i = 0
                while(i < 3):
                    show_cardapio()
                    print('Escolha seu {}º novo sabor'.format(i+1))

                    sabor = input()
                    escolha = int(sabor)
                    if escolha in menu:
                        sabores[i] = sabor
                        i += 1
                    else:
                        print(
                            'Essa opção não está dentro das opções do menu. Escolha novamente:')

            else:
                print('Opção invalida')
                alterar_sabores(tamanho)


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


def alterar_extras():
    return


def show_cardapio():
    """Mostra o cardapio do estabelecimento, arquivado em um .txt"""
    cardapio = open('cardapio.txt', 'r')
    for item in cardapio:
        print(item)
    cardapio.close()


def um_sabor(option):
    """Escolha do sabor para apenas um sabor"""

    global tamanho

    if option == 1 or option == 'PEQUENA':
        tamanho = 'Pequena'
    elif option == 2 or option == 'MEDIA':
        tamanho = 'Media'
    elif option == 3 or option == 'GRANDE':
        tamanho = 'Grande'
    show_cardapio()
    while (True):
        sabor_0 = input('Insira o numero referente ao sabor desejado:\n')
        if sabor_0.isnumeric():
            escolha = int(sabor_0)
            if escolha in menu:
                sabores.append(sabor_0)
                break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
    return more_options()


def dois_sabores(option):
    """Escolha do sabor para duas opcoes"""

    global tamanho
    global sabores
    if option == 2:
        tamanho = 'Media'
    elif option == 3:
        tamanho = 'Grande'

    while (True):
        show_cardapio()
        sabor_1 = input(
            'Insira o numero referente ao primeiro sabor desejado:\n')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_1.isnumeric():
            escolha = int(sabor_1)
            if escolha in menu:
                sabores.append(sabor_1)
                break
            sabor_2 = input(
                'Insira o numero referente ao segundo sabor desejado:\n')
            # Validando se o valor do sabor_2 eh um numero para poder adicionar ao pedido
            if sabor_2.isnumeric():
                escolha = int(sabor_2)
                if escolha in menu:
                    sabores.append(sabor_2)
                    break
            else:
                print('Ops! Digite apenas o número referente ao sabor:\n')
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
        # Condicao de parada do loop
        # if len(sabores) == 2:
        #     more_options()
        #     return sabores
    return more_options()


def tres_sabores():
    """Escolha dos sabores para tres opcoes"""

    global tamanho
    tamanho = 'Grande'
    global sabores
    show_cardapio()
    while (True):
        sabor_1 = input(
            'Insira o numero referente ao primeiro sabor desejado:\n')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_1.isnumeric():
            escolha = int(sabor_1)
            if escolha in menu:
                sabores.append(sabor_1)
                break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
    while (True):
        sabor_2 = input(
            'Insira o numero referente ao segundo sabor desejado:\n')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_2.isnumeric():
            escolha = int(sabor_2)
            if escolha in menu:
                sabores.append(sabor_2)
                break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
    while (True):
        sabor_3 = input(
            'Insira o numero referente ao terceiro sabor desejado:\n')
        # Validando se o valor do sabor_1 eh um numero para poder ser adicionado ao pedido
        if sabor_3.isnumeric():
            escolha = int(sabor_3)
            if escolha in menu:
                sabores.append(sabor_3)
                break
        else:
            print('Ops! Digite apenas o número referente ao sabor:\n')
    return more_options()


def more_options():
    global borders
    global refrigerante
    global borda
    global refri
    opt_border = int(input('Deseja adicionar borda?\n(1) SIM\n(2) NÃO\n'))
    if opt_border == 1:
        print('Escolha o recheio da borda:')
        for i in range(len(borders)):
            print(i, borders[i])
        b = int(input())
        if b >= 0 and b < len(borders):
            borda = borders[b]
        else:
            print('Essa opção de borda não existe')
    more_add = int(
        input('Deseja adicionar alguma bebida ao seu pedido?\n(1) SIM\n(2) NÃO\n'))
    if more_add == 1:
        print('Escolha o seu refrigerante:')
        for i in range(len(refrigerante)):
            print(i, refrigerante[i])
        r = int(input())
        if r >= 0 and r < len(borders):
            refri = refrigerante[r]
        else:
            print('Essa opção de borda não existe')
    return total_pedido()


def total_pedido():
    global tamanho
    global sabores
    global borders
    global borda
    global refrigerante
    global refri
    global menu
    print('Por favor, confirme seu pedido:')
    print('Pizza tamanho: {}'.format(tamanho))
    print('Sabores:')
    for i in sabores:
        j = int(i)
        print('{} '.format(menu[j]))
    if(borda != ''):
        print('Borda:')
        print(borda)
    if(refri != ''):
        print('refri:')
        print(refri)
    print('Valor total: R$ {}'.format(
        valor_total(tamanho, sabores, borda, refri)))
    answer = int(input('O seu pedido está correto?\n(1) SIM\n(2) NÃO\n'))
    if answer == 1:
        return payment()
    else:
        return alteracao_pedido()


def valor_total(tamanho, sabores, borda, refri):
    vl_total = 0.0
    if(tamanho == 'Pequena'):
        vl_total += 15.00
    elif (tamanho == 'Media'):
        vl_total += 20.00
    elif (tamanho == 'Grande'):
        vl_total += 25.00
    if(borda != ''):
        vl_total += 1
    if(refri != ''):
        vl_total += 7.00
    return vl_total


def payment():

    opt_payment = int(
        input('Qual a forma de pagamento:\n(1) Dinheiro\n(2) Cartão\n'))
    if opt_payment == 1:
        pay_back = input('Deseja troco?\n(1) SIM\n(2) NÃO\n')
        if pay_back == '1':
            print('Para quanto deseja o troco?')
            client_money = float(input())
            print('O troco será: R${}'.format(client_money -
                                              (valor_total(tamanho, sabores, borda, refri))))
            print('Agradecemos sua preferência!')
    else:
        print('O motoboy levará a máquineta para o pagamento no ato da entrega!')
        print('Agradecemos sua preferência!')


menu = {
    1: "AMERICANA",
    2: "APRESUNTADA",
    3: "CROCANTE",
    4: "MILHO",
    5: "MUSSARELA",
    6: "TRADICIONAL",
    7: "ALHO E ÓLEO",
    8: "BACON",
    9: "CALABRESA",
    10: "ESCAROLA",
    11: "FRANGO",
    12: "FRANGO C/ CATUPIRY",
    13: "FRAN-MILHO",
    14: "MARGUERITA",
    15: "MEXICANA",
    16: "NAPOLITANA",
    17: "PAULISTA",
    18: "PORTUGUESA",
    19: "TOSCANA",
    20: "ALICHE"
}
tamanho = ''
sabores = []
borda = ''
refri = ''
borders = ['Catupiry', 'Cheddar', 'Calabresa', 'Queijo', 'Nutela']
refrigerante = ['Coca-cola', 'Fanta', 'Sprite', 'Kuat', 'Guaraná Antartica']

bot.inicia()
i = 0
while(True):
    texto = bot.escuta()
    print(texto)
    if(texto == 'Fala bot!'):
        bot.responde()
        print("Entrei aqui")
    time.sleep(10)
# saudacao()
