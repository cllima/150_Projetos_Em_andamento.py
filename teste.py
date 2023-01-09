from datetime import datetime
import calendar
print(f"\033[;1m{'*'*10}Desfio 41 - Dividir idades por categorias{'*'*10}\033[0;m")
nascimento = input("Digite a sua idade (dd/mm/aaaa): ")
dia = int(nascimento[0:2])
mes = int(nascimento[3:5])
ano = int(nascimento[6:10])
## Verifica se a pessoa ja nasceu e se a data é possivel
if dia > 31 or mes > 12 or (ano > datetime.now().year or (ano == datetime.now().year
and mes > datetime.now().month) or (ano == datetime.now().year and mes == datetime.now().month and dia > datetime.now().day)):
    print("\033[1;31mInforme uma data correta!")
## Verifica se o mês tem a quantidade de dias certo
if dia > (calendar.monthrange(ano,mes)[1]):
    print(f"O Mês {mes} do ano {ano} não tem {dia} dias e sim {calendar.monthrange(ano,mes)[1]} dias\n\033[1;31mInforme uma data correta!")
## Calcula a sua idade em dia, mes e anos.
idade_ano = datetime.now().year - ano
idade_mes = datetime.now().month - mes
idade_dia = datetime.now().day - dia
if idade_dia < 0:
    idade_mes = idade_mes - 1
    idade_dia = calendar.monthrange(ano,mes)[1] + idade_dia
if idade_mes < 0:
    idade_ano = idade_ano - 1
    idade_mes = 12 + idade_mes
if idade_ano < 9 or (idade_ano == 9 and idade_dia == 0 and idade_mes == 0):
    print("Mirim!!")
elif idade_ano < 14 or (idade_ano == 14 and idade_dia == 0 and idade_mes == 0):
    print("Infantil!!")
elif idade_ano < 19 or (idade_ano == 19 and idade_dia == 0 and idade_mes == 0):
    print("Júnior!!")
elif idade_ano < 20 or (idade_ano == 20 and idade_dia == 0 and idade_dia == 0):
    print("Sênior!!")
else:
    print("Master!!")