"""

1.1 Lista de números positivos terminada por 0, imprimir seus quadrados

"""

lista = []
i = 0
n = int(input('Digite quantos números você vai digitar: '))
while (i < n):
  lista.append(int(input('Digite ' + str(i+1) + '° número: ')))
  i+=1
for m in lista:
  print(m**2)
