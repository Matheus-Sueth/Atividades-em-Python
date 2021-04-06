"""

1.01 Faça um programa que receba como entrada um inteiro N e três listas de tamanho N: **produto**, **estoque** e **pedido**. A lista **produto** é formada por strings e as listas **estoque** e **pedido** são formadas por inteiros. Considere que os elementos numa mesma porsição i das três listas estão relacionadas. Seu programa deve retornar uma listagem na tela dos produtos que não têm estoque suficiente para o pedido e a respectiva quantidade que está faltando.
#Obersevação: Os elementos de cada lista devem ser digitados pelo usuário na mesma linha e separados por vírgula.
Por exemplo:

Entrada: 
3 
banana, tomate, cenoura 
26, 30, 47 
20, 34, 50

Saída:
tomate 4
cenoura 3

"""

prod = est = ped = []
valor = int(input('Digite o tamanho da lista: '))
while (len(prod) < valor):
  prod = input().split(",")
while (len(est) < valor):
  est = input().split(",")
while (len(ped) < valor):
  ped = input().split(",")

lista = []
i = 0

while (i < valor):
  if (est[i] < ped[i]):
    print(str(prod[i]) + ' ' + str(int(ped[i]) - int(est[i])))
  i += 1
