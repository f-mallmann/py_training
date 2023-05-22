#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:#
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".#

print('Responda as seguintes perguntas com S/sim ou N/não : ')
positivo = 0

telefone = input('Telefonou para vitima ?')
if telefone.upper() == "S":
    positivo = positivo + 1

local = input('Esteve no local do crime ?')
if local.upper() ==  "S":
    positivo = positivo + 1

residencia = input('Mora perto da vitima ?')
if residencia.upper() == "S":
    positivo = positivo + 1

divida = input('Devia algo para vitima ?')
if divida.upper() ==  "S":
    positivo = positivo + 1

trabalho = input('Ja trabalhou com a vitima ?')
if trabalho.upper() == "S":
    positivo = positivo + 1

print('Classificação do Suspeito :')                
if positivo < 2:
    print("Inocente")
elif positivo == 2:
    print("Suspeita")
elif positivo < 5:
    print("Cúmplice")
else:
    print("Assassino")
          
               