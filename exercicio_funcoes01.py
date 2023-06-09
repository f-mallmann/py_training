#função que multiplica argumentos não nomeados 
def multplicar (*args):
    total = 1 
    for numero in args:
        total *= numero 
    return total 

resultado1= multplicar(1,3)
print(resultado1)

#finção que mosyra se o numero é par ou impar 
def par_impar (numero):
    multiplo_2 = numero % 2 == 0 

    if multiplo_2:
        return f'{numero} é par. '
    return f'{numero} é impar. '


print(par_impar(resultado1))
  
