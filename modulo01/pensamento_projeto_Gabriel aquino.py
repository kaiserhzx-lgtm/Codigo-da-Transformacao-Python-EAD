'''
Um bloco de comentarios
>PO (como dono negocio) preciso de um sistema de vendas de hamburguer para que eu possa vender e lucrar

>QA (como cliente) preciso de um sistema facil de compras para que eu possa comprar de forma prattica

>TECH (como programador) quero um sistema que eu possa implementar funcionalidades basicas para que eu possa atender o cliente de forma pratica 


>DEV (como programador) quero um sistema facil e pratico de comprass para minha hamburgueria para implementar funcionalidades a interface do sistema 


>UX (como designer de experiencia do usuario) quero um sistema pratico e facil para que o cliente possa comprar de forma pratica e facil


>IA (como inteligencia artificial) quero um sistema de vendas de hamburguer para que o cliente possa comprar de forma pratica e rapida

'''

#
while True:

    print('-' * 48 + '\n')
    print('bem vindo ao sistema de vendas de hamburguer\n')
    print('1 - cadastrar produto')     
    print('2 - listar produto') 
    print('3 - realizar venda')
    print('0 - sair')   
    print('\n---------------------------------------------\n')

    opção = input('digite a opção desejada: ')

    if opção == '1':


        print(' cadastrando produto...\n')
        nome_produto = input('digite o nome do produto: ')
        preço_produto = float(input('digite o preço do produto: '))
        validade_produto = input('digite a validade do produto: ')
        descrição_produto = input('digite a descrição do produto: ')
        print(f'produto {nome_produto} cadastrado com sucesso!\n')  

    if opção == '2':
        print('listar produtos...\n')
