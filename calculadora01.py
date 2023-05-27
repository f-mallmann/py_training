while True:
    x = input('Digite um numero :')
    operador = input('Digite um operador matematico ( + , - , * ou / )')
    y = input('Digite o segundo numero :')
    
    numeros_validos = None #flag
    x_float = 0
    y_float = 0

    try:
        x_float = float(x)
        y_float = float(y)
        numeros_validos = True          #flag ok --- segue para verificar operadores . 

    except:
        numeros_validos = None          #flag nok --- volta para o inicio .
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são inválidos. ')
        continue 
    
    #verifica se operador esta no range permitido    
    operadores_permitidos = '+-/*'      
    if operador not in operadores_permitidos:
        print('Operador inválido. ')
        continue
    
    #verifica se foi digitado mais de 1 operador 
    if len(operador) > 1  :              
        print('Digite apenas um operador. ')
        continue
    # realizando as operações     
    print('Realizando sua conta, confira o resultado : ')
    if operador == '+' : 
        print(f'{x_float}+{y_float}=',x_float + y_float)
    elif operador == '-':
       print(f'{x_float}-{y_float}=',x_float - y_float) 
    elif operador == '/':
        print(f'{x_float}/{y_float}=',x_float / y_float)
    elif operador == '*':
        print(f'{x_float}*{y_float}=',x_float * y_float)        

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break    

            
        




   