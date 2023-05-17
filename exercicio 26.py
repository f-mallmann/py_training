"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
-Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
-Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
-Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""



combustivel = input("Digite A para álcool ou G para gasolina: ")
litros = float(input('Quantidade de litros abastecido :'))

valorgasolina = 2.50
valoralcool = 1.90
if combustivel == "a" or combustivel == "A":
    if litros <= 19:
        desconto = 0.057 
        desc = desconto * litros
        total =  (valoralcool - desconto) * litros
    else:
        if litros >= 20:
            desconto = 0.095 
            desc = desconto * litros
            total =  (valoralcool - desconto) * litros 
if combustivel == "g" or combustivel == "G":
    if litros <= 19:
        desconto = 0.10 
        desc = desconto * litros
        total = (valorgasolina - desconto) * litros
    else:
        if litros >= 20:
            desconto = 0.15 
            desc = desconto * litros
            total =  (valorgasolina - desconto) * litros
print(f'Valor total : R${total:.2f}')
print(f'Desconto =R$ {desc:.2f}')