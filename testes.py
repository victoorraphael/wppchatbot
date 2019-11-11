import re

texto = '#Olá, como está?'

if(not(re.match(r'^#', texto))):
    print('1')
else:
    print('2')