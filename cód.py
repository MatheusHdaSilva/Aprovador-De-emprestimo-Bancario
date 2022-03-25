casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o valor do salário?'))
tempo = int(input('Em quantos anos você pretende pagar?'))
s1 = (tempo * 12)
s2 = (casa / s1) 
s3 = (salario * 30 / 100)
if s2 >= s3:
	print('A parcela ficará em torno de {:.2f} e por exerder 30% do valor do salário que é {:.2f}, seu empréstimo não será aprovado...'.format(s2, s3))
else:
	print('\033[0;30;41m!!!PARABÉNS O SEU EMPRÉSTIMO FOI APROVADO!!!\033[m, a parcela da casa ficou em torno de {:.2f}, e não ultrapassa 30% do seu salário e será paga em {} anos'.format(s2, tempo))