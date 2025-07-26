#1 Boas Vindas
boas_vindas = 'Seja bem vindo(a) para o Verificador de Idade para Votação'
print (boas_vindas)

#2 Perguntar a idade do usuário
idade_quest = input ('Qual a sua idade?')

#3 Conversão de valores 
idade_num = int(idade_quest)

#4 Definindo as idades e respondendo o usuário
if idade_num < 16 : print ('Não é permitido votar, desculpe')

elif idade_num >= 16 and idade_num <= 17 : print ('Seu voto é opcional')

elif idade_num >= 18 and idade_num <= 69 : print ('Seu voto é obrigatório')

else:  print ('Seu voto é opcional')
