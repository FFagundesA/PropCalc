elif operacao == "operações entre raízes":
numero_de_raizes = int(input("\nDigite quantas raízes você quer usar: "))
total_de_raizes = list()
n_da_raiz = 1
for x in range(1, numero_de_raizes + 1):
    indice_n = int(input(f"\nDigite o índice da raíz {n_da_raiz}: "))
    numero_n = float(input(f"\nDigite o número da raíz {n_da_raiz}: "))
    raiz_n = (numero_n ** (1 / indice_n))
    total_de_raizes.append(raiz_n)
    n_da_raiz = n_da_raiz + 1
print(f"\nAs raízes que você escolheu são: {total_de_raizes}.")




elif operacao == "raíz":
i = 0
indice = float(input("\nDigite o índice da raíz: "))

for x in lista_de_numeros:
    if lista_de_numeros[i] > 0:
        raiz = (lista_de_numeros[i]) ** (1 / indice)
        print(f"A raíz de índice {indice} do número {lista_de_numeros[i]} é {raiz}.")

    if lista_de_numeros[i] < 0 and (indice / 2) != (indice // 2):
        raiz = -(((lista_de_numeros[i]) * -1) ** (1 / indice))
        print(f"A raíz de índice {indice} do número {lista_de_numeros[i]} é {raiz}.")

    if lista_de_numeros[i] < 0 and (indice / 2) == (indice // 2):
        print(f"A raíz de índice {indice} do número {lista_de_numeros[i]} é imaginária.")

    i = i + 1

##

divisores = list()
numeros = list()
pergunta = int(input("Quantos números você quer usar? "))
n = 1

while len(numeros) < pergunta:
    nn = int(input(f"Digite o número {n}: "))
    numeros.append(nn)
    n = n + 1

print(f"Os números que você escolheu foram: {numeros}")

while True:
    pergunta2 = input("Deseja alterar algum número? (s ou n) ")

    while pergunta2 != "s" and pergunta2 != "n":
        pergunta2 = input("As possíveis respostas são 's' e 'n'. Digite novamente: ")

    if pergunta2 == "s":
        pergunta3 = int(input("Qual posição da sequência (1, 2, 3..) você quer alterar? "))
        antigo_n = numeros[pergunta3 - 1]
        i = numeros.index(numeros[pergunta3 - 1])
        novo_n = int(input(f"Qual núero você quer colocar no lugar do {antigo_n}? "))
        numeros.remove(antigo_n)
        numeros.insert(i, novo_n)
    print(f"Os novos números são: {numeros}")

    if pergunta2 == "n":
        break

for x in numeros:
    for y in range(1, x + 1):
        if x / y == x // y:
            divisores.append(y)