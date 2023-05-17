"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a 
quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""

x = int(input('Qual codigo do produto ? 1-MORANGO / 2 - MAÇÃ\n'))
y = float(input('Qual o peso do produto: '))

if x == 1:
    if y <= 5:
        valor =  y * 2.50
    else :
        valor = y * 2.20     
if x == 2:  
    if y <= 5:
        valor =  y * 1.80
    else :
        valor = y * 1.50
print(f'total R${valor:.2f}')

if y >= 8 or valor > 25.00:
    precototal= (valor / 100)*90 
    print(f'Total com desconto = R${precototal:.2f}')
