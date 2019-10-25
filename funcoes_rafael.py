def novo_pedido():
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
                '10. ALHO E ÓLEO\n'
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
                'MOLHO DE TOMATE, TOMATES, PARMESÃO, MANJERICÃO, AZEITE DE OLIVA E MUSSARELA\n'
                '19. MEXICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA RALADA, PIMENTÃO VERDE E PIMENTA-CALABRESA\n'
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
    global tamanho
    while(True):
        print('Qual o tamanho da sua pizza?\n'
              '1.  PEQUENA\n'
              '2.  MÉDIA\n'
              '3.  GRANDE')
        option = int(input())
        if option == 1:
            tamanho = 'Pequena'
            print(cardapio)
            while(True):
                sabores.append(int(input('Qual o sabor?')))
                #if sabor_um == type(int):
                #    break
                #else:
                #    return ('Opção invalida, tente novamente!\n'
                #            'ATENÇÃO! Digite apenas o número referente ao que deseja.\n')
                break
            break
        elif option == 2:
            tamanho = 'Média'
            print(cardapio)
            while(True):
                sabor_dois = int(input('Quantos sabores deseja:\n1. Um sabor\n2. Dois sabores'))
                if sabor_dois == 1:
                    sabores.append(int(input('Insira o sabor.')))
                    break
                elif sabor_dois == 2:
                    sabores.append(int(input('Insira o primeiro sabor.')))
                    sabores.append((int(input('Insira o segundo sabor.'))))
                    break
                else:
                    print('Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')

            break
        elif option == 3:
            tamanho = 'Grande'
            print(cardapio)
            while(True):
                sabor_tres = (int(input('Quantos sabores deseja:\n1. Um sabor\n2. Dois sabores\n3. Três sabores')))
                if sabor_tres == 1:
                    sabores.append(int(input('Insira o sabor.')))
                    break
                elif sabor_tres == 2:
                    sabores.append(int(input('Insira o primeiro sabor.')))
                    sabores.append(int(input('Insira o segundo sabor.')))
                    break
                elif sabor_tres == 3:
                    sabores.append(int(input('Insira o primeiro sabor.')))
                    sabores.append(int(input('Insira o segundo sabor.')))
                    sabores.append(int(input('Insira o terceiro sabor.')))
                    break
                else:
                    print(
                        'Opção invalida, tente novamente!\nATENÇÃO! Digite apenas o número referente ao que desejar.\n')
            break
        else:
            print('Opção invalida, tente novamente!\n'
                  'ATENÇÃO! Digite apenas o número referente ao que desejar.\n')
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
sabores = []
novo_pedido()
print('Os sabores escolhidos foram\n{}'.format(sabores))
print(tamanho)