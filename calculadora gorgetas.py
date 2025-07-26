#1 Boas Vindas
boas_vindas = 'Seja bem vindo(a) calculadora de gorgetas!'
print (boas_vindas)

#2 Perguntar o valor da conta
valor_conta = input('qual foi o valor total?')

#3 Perguntar a porcentagem da gorgeta
porc_gorgeta = input('Qual a porcentagem de gorgetas que você poderia oferecer?')

#4 Conversão 
valor_conta_num = float(valor_conta)
porc_gorgeta_num = int(porc_gorgeta)

#5 Cálculo da gorgeta
valor_gorgeta = valor_conta_num * (porc_gorgeta_num/100)

#6 Conta Final
valor_final = valor_conta_num + valor_gorgeta

#7 Resultados
print (f'O valor da gorgeta é de {valor_gorgeta:.2f}')
print (f'O valor final a pagar é de R$ {valor_final: .2f}')