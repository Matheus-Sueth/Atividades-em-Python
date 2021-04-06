a = []
print('Digite o grau do polinômio: (1/2/3)')
poten = grau = int(input(' '))
i = 0
while (i <= grau):
  a.append(float(input('Digite o ' + str(i+1) + '°coeficiente: ')))
  print(str(a[i]))
  if (i == grau):
    x = float(input('Digite o valor da variável: '))
  i+=1
if (grau == 1):
  print(str(a[0]) + " * " + str(x) + " + " + str(a[1]))
  f = a[0]*(x**(poten)) + a[1]
elif (grau == 2):
  f = a[0]*(x**poten) + a[1]*(x**(poten-1)) + a[2]
elif (grau == 3):
  f = a[0]*(x**poten) + a[1]*(x**poten-2 ) + a[2]*(x**(poten-1)) + a[3]
print(str(f))
