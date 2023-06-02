import os

lista= []
while True:
   
    print('Selecione uma opção :')
    opcao = input('[I]nserir - [A]pagar - [L]istar  - [S]air: ')

    if opcao == 'i':
        os.system('cls')
        produto = input ('Produto :')
        lista.append(produto)
    elif opcao == 'a':
        indice_str= input('Escolha o indice que voce quer apagar: ') 
        
        try :
            indice = int(indice_str)
            del lista[indice]
        
        except :
             print('Nao foi possivel apagara esse indice. ')
    
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0 :
            print('Nada para listar. ')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 's':
        print('Fim do programa.')
        break