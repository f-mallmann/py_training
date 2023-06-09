#crie funções que duplicam, trilplicam e quadruplicam o numero recebido como parâmentro.

def multiplicar (multiplicador ):
    def multiplicado (numero) :
        return numero * multiplicador
    return multiplicado

mult_2 = multiplicar(2)
mult_3 = multiplicar(3)
mult_4 = multiplicar(4)

print(mult_2(3))
print(mult_3(3))
print(mult_4(3))
