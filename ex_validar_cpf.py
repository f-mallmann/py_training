#validar digito do CPF
cpf_usuario = input('Digite o seu CPF :') \
    .replace('.','')\
    .replace('-','')\
    .replace(' ','')  #se o usuario digitar o formato ___.___.___-__ a função replace retira . 
  
regressivo_1 = 10 
nove_digitos = cpf_usuario[:9]
#validando o 1º digito
resultado_digito_1 = 0 
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * regressivo_1
    regressivo_1 -= 1
digito_1 = ( resultado_digito_1 * 10) % 11 
digito_1 = digito_1 if digito_1 <= 9 else 0 

#validando o 2º digito   
regressivo_2 = 11 
dez_digitos = nove_digitos + str(digito_1)
resultado_digito_2 = 0 
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * regressivo_2
    regressivo_2 -= 1
digito_2 = ( resultado_digito_2 * 10) % 11 
digito_2 = digito_2 if digito_2 <= 9 else 0 

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado_pelo_calculo == cpf_usuario:
    print(f'{cpf_usuario} é valido ')
else :
    print('CPF inválido')    


