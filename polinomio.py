"""
1.0 Faça um programa para avaliar equações polinomiais. O usuário deverá digitar numa linha o grau do polinômio, e na linha seguinte
os valores dos coeficientes em ordem decrescente e o valor da variável separados por espaço, lembrando que os coeficientes e valor da variável podem ser reais.
Por exemplo, para o caso f(x) = 2x² - 3x + 7 com x = 5, temos

Entrada: 
2 -
2 -3 7 5

Saída:
42.0
"""
a = []
print('Digite o grau do polinômio: (1/2/3)')
poten = grau = int(input(' '))
i = 0
while (i <= grau):
  a.append(float(input('Digite o ' + str(i+1) + '°coeficiente: ')))
  if (i == grau):
    x = float(input('Digite o valor da variável: '))
  i+=1
if (grau == 1):
  f = a[0]*(x**(poten)) + a[1]
elif (grau == 2):
  f = a[0]*(x**poten) + a[1]*(x**(poten-1)) + a[2]
elif (grau == 3):
  f = a[0]*(x**poten) + a[1]*(x**poten-2 ) + a[2]*(x**(poten-1)) + a[3]
print(str(f))
