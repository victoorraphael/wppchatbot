import os.path

nome = input('nome:')
arquivo = '{}.txt'.format(nome)

caminho = '/home/raphael/Google Drive/The Bots/wppchatbot/'

verifica = caminho+arquivo

check = os.path.exists(verifica)

if check:
    cria = open (arquivo, 'a')
    print('Bom te ver de volta!')
    cria.write('novo')
    cria.close()
else:
    print('Novo')
    cria = open (arquivo, 'a')
    cria.write('novo')
    cria.close()

