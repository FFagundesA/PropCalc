print("Bem vindo à Calculadora Humanizada!")
pergunta = input("\nQual serviço você quer usar? (calculadora, par ou impar, primo ou nao, raiz, potencia, divisores, "
                 "equação do segundo grau (eq2)) ")

while pergunta != "calculadora" and pergunta != "par ou impar" and pergunta != "primo ou nao" and pergunta != "raiz" and pergunta != "potencia" and pergunta != "divisores" and pergunta != "eq2":
    pergunta = input("cara, ou vc ta tentando burlar o sistema ou vc escreveu errado, digita de novo: ")

if pergunta == "calculadora":
    numeros = int(input("\nQuantos números você quer usar no cálculo? "))

    while numeros < 0:
        numeros = int(
            input("Cara kkkk na moral, para de tentar burlar o sistema e coloca logo quantos números você quer usar: "))
    if numeros == 0:
        print("Ah é, então tá, já que você quer usar 0 números..entendo que você não quer fazer nenhum cálculo..então "
              "tchau!")
        exit("Toma Essa!")

    lista_de_numeros = list()
    n = 1

    for x in range(1, numeros + 1):
        a = float(input(f"\nDigite o número {n}: "))
        lista_de_numeros.append(a)
        n = n + 1

    print(f"\nOs números que você escolheu são: {lista_de_numeros}.")

    possivel_mais = ""

    while True:
        pergunta2 = input(f"\nDeseja alterar {possivel_mais} algum número de sua sequência? (s ou n) ")

        while pergunta2 != "s" and pergunta2 != "n":
            pergunta2 = input("\nAs possíveis respostas são 's' ou 'n', favor digitar novamente: ")

        if pergunta2 == "s":
            n = int(input("\nQual dos números você gostaria de alterar? (1, 2 ...) "))
            lista_de_numeros.remove(lista_de_numeros[n - 1])
            novo_n = int(input(f"\nQual número você gostaria de pôr no lugar do número {n}? "))
            lista_de_numeros.insert(n - 1, novo_n)
            print(f"\nOs números que você escolheu são: {lista_de_numeros}.")
            possivel_mais = "mais"

        if pergunta2 == "n":
            break

    operacao = input("\nQual operação você quer efetuar? (soma, sub, mut, div, div int, media) ")

    if operacao == "soma":
        print(f"A soma é {sum(lista_de_numeros)}.")
    elif operacao == "sub":
        for x in range(1, len(lista_de_numeros)):
            n0 = lista_de_numeros[0]
            n1 = lista_de_numeros[1]
            sub = (n0 - n1)
            lista_de_numeros.remove(n0)
            lista_de_numeros.remove(n1)
            lista_de_numeros.insert(0, sub)
        print(f"A diferença é {sub}.")
    elif operacao == "mut":
        for x in range(1, len(lista_de_numeros)):
            n0 = lista_de_numeros[0]
            n1 = lista_de_numeros[1]
            mut = (n0 * n1)
            lista_de_numeros.remove(n0)
            lista_de_numeros.remove(n1)
            lista_de_numeros.insert(0, mut)
        print(f"A mutiplicação é {mut}.")
    elif operacao == "div":
        for x in range(1, len(lista_de_numeros)):
            n0 = lista_de_numeros[0]
            n1 = lista_de_numeros[1]
            div = (n0 / n1)
            lista_de_numeros.remove(n0)
            lista_de_numeros.remove(n1)
            lista_de_numeros.insert(0, div)
        print(f"A divisão é {div}.")
    elif operacao == "div int":
        for x in range(1, len(lista_de_numeros)):
            n0 = lista_de_numeros[0]
            n1 = lista_de_numeros[1]
            div_int = (n0 // n1)
            lista_de_numeros.remove(n0)
            lista_de_numeros.remove(n1)
            lista_de_numeros.insert(0, div_int)
        print(f"A divisão inteira é {div_int}.")
    elif operacao == "media":
        media = (sum(lista_de_numeros)) / len(lista_de_numeros)
        print(f"A média dos números é: {media}")

if pergunta == "raiz":
    numero_de_raizes = int(input("\nDigite quantas raízes você quer usar: "))
    total_de_raizes = list()
    n_da_raiz = 1
    for x in range(1, numero_de_raizes + 1):
        indice_n = int(input(f"\nDigite o índice da raíz {n_da_raiz}: "))
        numero_n = float(input(f"Digite o número da raíz {n_da_raiz}: "))
        if numero_n >= 0:
            raiz_n = (numero_n ** (1 / indice_n))
        elif indice_n / 2 != indice_n // 2 and numero_n < 0:
            raiz_n = -((numero_n * -1) ** (1 / indice_n))
        elif indice_n / 2 == indice_n // 2 and numero_n < 0:
            raiz_n = f"A raíz de índice {indice_n} do número {numero_n} é imaginária."
        total_de_raizes.append(raiz_n)
        n_da_raiz = n_da_raiz + 1
    print(f"\nOs resultados das raízes são, respectivamente: {total_de_raizes}.")

if pergunta == "potencia":
    qnts_potencias = int(input("\nQuantos números você quer usar? "))
    total_potencias = list()
    numero_da_potencia = 1
    for x in range(1, qnts_potencias + 1):
        numero = float(input(f"\nDigite o número da potência {numero_da_potencia}: "))
        expoente = float(input(f"Digite o expoente da potência {numero_da_potencia}: "))
        resultado = (numero ** expoente)
        total_potencias.append(resultado)
        numero_da_potencia = numero_da_potencia + 1
    print(f"\nOs resultados são, respectivamente: {total_potencias}.")

if pergunta == "par ou impar":
    qnts_numeros = int(input("Quantos números você quer usar? "))
    total_numeros = list()
    n = 1
    for x in range(1, qnts_numeros + 1):
        numero_n = float(input(f"Digite o número {n}: "))
        total_numeros.append(numero_n)
        n = n + 1

    print(f"\nOs números que você escolheu são: {total_numeros}.")
    possivel_mais = ""

    while True:
        pergunta = input(f"Deseja alterar {possivel_mais} algum número? (s ou n) ")

        while pergunta != "s" and pergunta != "n":
            pergunta = input("As possíveis respostas são apenas 's' ou 'n'. Digite novamente: ")

        if pergunta == "s":
            n_a_alterar = float(input("\nQual número você gostaria de alterar? (Digite o número): "))

            while n_a_alterar not in total_numeros:
                n_a_alterar = float(input("O número que você escolheu não está presente na lista, digite um que esteja "
                                          "para fazer a substituição: "))

            i = total_numeros.index(n_a_alterar)
            total_numeros.remove(n_a_alterar)
            novo_n = float(input("\nDigite o novo número: "))
            total_numeros.insert(i, novo_n)
            possivel_mais = "mais"

        if pergunta == "n":
            break

    print(f"\nOs números que você escolheu são: {total_numeros}")

    pares = list()
    impares = list()

    for x in total_numeros:
        if x / 2 == x // 2:
            pares.append(x)
        else:
            impares.append(x)

    print(f"Os pares são: {pares}\nOs Ímpares são: {impares}")
    print(f"\nNúmero de pares: {len(pares)}\nNúmero de Ímpares: {len(impares)}")

if pergunta == "primo ou nao":
    lista = list()
    ask = int(input("\nQuantos números você quer usar? "))
    vez = 1

    for x in range(1, (ask + 1)):
        ask2 = int(input(f"\nDigite o número {vez}: "))
        lista.append(ask2)
        vez = vez + 1

    print(f"\nOs numeros que você escolheu são: {lista}")

    ask3 = input("\nDeseja alterar algum número? (s ou n) ")

    while ask3 != "s" and ask3 != "n":
        ask3 = input("\ncara na moral para de tentar burlar plmds...'s' ou 'n'? ")

    if ask3 == "s":
        qnts_alter = int(input("\nQuantos números você quer alterar? "))

        while qnts_alter > len(lista):
            qnts_alter = int(input("A lista não tem essa quantidade de números para alterar, digite novamente: "))

        for x in range(1, (qnts_alter + 1)):
            alter = int(input("\nQual número você quer alterar? "))

            while alter not in lista:
                alter = int(input("\nO número que você escolheu não está na lsita, digite novamente: "))

            lugar = lista.index(alter)
            novo = int(input(f"\nQual número entrará no lugar do {alter}? "))
            lista.insert(lugar, novo)
            lista.remove(alter)

    print(f"\nOs números que você escolheu são: {lista}")

    primos = list()
    n_primos = list()
    possivel_p = list()

    for x in lista:
        if x == 1 or x == 2:
            primos.append(x)
        else:
            for y in range(2, x):
                if x / y == x // y:
                    n_primos.append(x)
                    break
                else:
                    possivel_p.append(x)
            if x not in n_primos and x in possivel_p:
                primos.append(x)

    print(f"\nOs primos são: {primos}\nOs não primos são: {n_primos}")

if pergunta == "divisores":
    divisores = list()
    numero = list()
    pergunta1 = int(input("Qual número você quer? "))
    numero.append(pergunta1)

    while True:
        pergunta2 = input("Você deseja alterar o número? ('s' ou 'n') ")

        while pergunta2 != 's' and pergunta2 != 'n':
            pergunta2 = input("As possíveis respostas são 's' ou 'n', digite novamente: ")

        if pergunta2 == 'n':
            break

        if pergunta2 == 's':
            nn = int(input(f"Qual número você quer colocar no lugar do {pergunta1}? "))
            numero.remove(pergunta1)
            numero.append(nn)

        print(f"O número agora é {numero}")

    for x in numero:
        for y in range(1, x + 1):
            if x / y == x // y:
                divisores.append(y)

    print(f"Os divisores do número {numero[0]} são: {divisores}.")

if pergunta == "eq2":
    A, B, C = float(input("Digite o valore de A: ")), float(input("Digite o valore de B: ")), float(input("Digite o "
                                                                                                          "valore"
                                                                                                    "de C: "))
    while True:
        ask4 = input(f"Os valores que você escolheu para A, B e C, respectivamente foram: {A, B, C}. Deseja alterar "
                     f"algum? ('s'"
                     f"ou 'n') ")
        while ask4 != "s" and ask4 != "n":
            ask4 = input("As possíveis respostas são 's' ou 'n'. Digite novamente: ")

        if ask4 == "s":
            ask5 = (input("Qual letra você deseja alterar? (A, B ou C) "))

            while ask5 != "A" and ask5 != "B" and ask5 != "C":
                ask5 = input(
                    "Cara na moral, ou vc escreveu um minúsculo ou vc tá tentando burlar o sistema. Digita dnv: ")

            if ask5 == "A":
                A = float(input("Qual será o novo valor de A? "))

            if ask5 == "B":
                B = float(input("Qual será o novo valor de B? "))

            if ask5 == "C":
                C = float(input("Qual será o novo valor de C? "))

        if ask4 == "n":
            break

    delta = ((B ** 2) - (4 * A * C))
    raiz1 = (((-B) + (delta ** (1 / 2))) / (2 * A))
    raiz2 = (((-B) - (delta ** (1 / 2))) / (2 * A))

    if delta < 0:
        print("As raízes da equação são complexas.")

    if delta == 0:
        print(f"As raízes da equação são respectivamente: {raiz1, raiz2}.\nP.S Elas são iguais pq "
              f"o delta da 0.")

    if delta > 0 and (A + B + C) != 0:
        print(f"As raízes da equação são respectivamente: {raiz1, raiz2}.")

    if delta > 0 and A + B + C == 0:
        print(f"As raízes da equação são respectivamente: {raiz1, raiz2}.\nP.S Essa equação foi "
              f"resolvida pelo maçete do 'O CASO'!")

final = input("\nVocê deseja continuar usando o programa? (s ou n) ")

while final != "s" and final != "n":
    final = input("\nAs possíveis respostas são apenas 's' ou 'n', digite novamente: ")

if final == "n":
    print("\nObrigado pela sua preferência!")
    exit("Feito por Felipe Fagundes de Azevedo")

if final == "s":
    while True:
        print("Bem vindo à Calculadora Humanizada!")
        pergunta = input(
            "\nQual serviço você quer usar? (calculadora, par ou impar, primo ou nao, raiz, potencia, divisores, "
            "equação do segundo grau (eq2)) ")

        while pergunta != "calculadora" and pergunta != "par ou impar" and pergunta != "primo ou nao" and pergunta != "raiz" and pergunta != "potencia" and pergunta != "divisores" and pergunta != "eq2":
            pergunta = input("cara, ou vc ta tentando burlar o sistema ou vc escreveu errado, digita de novo: ")

        if pergunta == "calculadora":
            numeros = int(input("\nQuantos números você quer usar no cálculo? "))

            while numeros < 0:
                numeros = int(
                    input(
                        "Cara kkkk na moral, para de tentar burlar o sistema e coloca logo quantos números você quer "
                        "usar: "))
            if numeros == 0:
                print(
                    "Ah é, então tá, já que você quer usar 0 números..entendo que você não quer fazer nenhum "
                    "cálculo..então"
                    "tchau!")
                exit("Toma Essa!")

            lista_de_numeros = list()
            n = 1

            for x in range(1, numeros + 1):
                a = float(input(f"\nDigite o número {n}: "))
                lista_de_numeros.append(a)
                n = n + 1

            print(f"\nOs números que você escolheu são: {lista_de_numeros}.")

            possivel_mais = ""

            while True:
                pergunta2 = input(f"\nDeseja alterar {possivel_mais} algum número de sua sequência? (s ou n) ")

                while pergunta2 != "s" and pergunta2 != "n":
                    pergunta2 = input("\nAs possíveis respostas são 's' ou 'n', favor digitar novamente: ")

                if pergunta2 == "s":
                    n = int(input("\nQual dos números você gostaria de alterar? (1, 2 ...) "))
                    lista_de_numeros.remove(lista_de_numeros[n - 1])
                    novo_n = int(input(f"\nQual número você gostaria de pôr no lugar do número {n}? "))
                    lista_de_numeros.insert(n - 1, novo_n)
                    print(f"\nOs números que você escolheu são: {lista_de_numeros}.")
                    possivel_mais = "mais"

                if pergunta2 == "n":
                    break

            operacao = input("\nQual operação você quer efetuar? (soma, sub, mut, div, div int, media) ")

            if operacao == "soma":
                print(f"A soma é {sum(lista_de_numeros)}.")
            elif operacao == "sub":
                for x in range(1, len(lista_de_numeros)):
                    n0 = lista_de_numeros[0]
                    n1 = lista_de_numeros[1]
                    sub = (n0 - n1)
                    lista_de_numeros.remove(n0)
                    lista_de_numeros.remove(n1)
                    lista_de_numeros.insert(0, sub)
                print(f"A diferença é {sub}.")
            elif operacao == "mut":
                for x in range(1, len(lista_de_numeros)):
                    n0 = lista_de_numeros[0]
                    n1 = lista_de_numeros[1]
                    mut = (n0 * n1)
                    lista_de_numeros.remove(n0)
                    lista_de_numeros.remove(n1)
                    lista_de_numeros.insert(0, mut)
                print(f"A mutiplicação é {mut}.")
            elif operacao == "div":
                for x in range(1, len(lista_de_numeros)):
                    n0 = lista_de_numeros[0]
                    n1 = lista_de_numeros[1]
                    div = (n0 / n1)
                    lista_de_numeros.remove(n0)
                    lista_de_numeros.remove(n1)
                    lista_de_numeros.insert(0, div)
                print(f"A divisão é {div}.")
            elif operacao == "div int":
                for x in range(1, len(lista_de_numeros)):
                    n0 = lista_de_numeros[0]
                    n1 = lista_de_numeros[1]
                    div_int = (n0 // n1)
                    lista_de_numeros.remove(n0)
                    lista_de_numeros.remove(n1)
                    lista_de_numeros.insert(0, div_int)
                print(f"A divisão inteira é {div_int}.")
            elif operacao == "media":
                media = (sum(lista_de_numeros)) / len(lista_de_numeros)
                print(f"A média dos números é: {media}")

        if pergunta == "raiz":
            numero_de_raizes = int(input("\nDigite quantas raízes você quer usar: "))
            total_de_raizes = list()
            n_da_raiz = 1
            for x in range(1, numero_de_raizes + 1):
                indice_n = int(input(f"\nDigite o índice da raíz {n_da_raiz}: "))
                numero_n = float(input(f"Digite o número da raíz {n_da_raiz}: "))
                if numero_n >= 0:
                    raiz_n = (numero_n ** (1 / indice_n))
                elif indice_n / 2 != indice_n // 2 and numero_n < 0:
                    raiz_n = -((numero_n * -1) ** (1 / indice_n))
                elif indice_n / 2 == indice_n // 2 and numero_n < 0:
                    raiz_n = f"A raíz de índice {indice_n} do número {numero_n} é imaginária."
                total_de_raizes.append(raiz_n)
                n_da_raiz = n_da_raiz + 1
            print(f"\nOs resultados das raízes são, respectivamente: {total_de_raizes}.")

        if pergunta == "potencia":
            qnts_potencias = int(input("\nQuantos números você quer usar? "))
            total_potencias = list()
            numero_da_potencia = 1
            for x in range(1, qnts_potencias + 1):
                numero = float(input(f"\nDigite o número da potência {numero_da_potencia}: "))
                expoente = float(input(f"Digite o expoente da potência {numero_da_potencia}: "))
                resultado = (numero ** expoente)
                total_potencias.append(resultado)
                numero_da_potencia = numero_da_potencia + 1
            print(f"\nOs resultados são, respectivamente: {total_potencias}.")

        if pergunta == "par ou impar":
            qnts_numeros = int(input("Quantos números você quer usar? "))
            total_numeros = list()
            n = 1
            for x in range(1, qnts_numeros + 1):
                numero_n = float(input(f"Digite o número {n}: "))
                total_numeros.append(numero_n)
                n = n + 1

            print(f"\nOs números que você escolheu são: {total_numeros}.")
            possivel_mais = ""

            while True:
                pergunta = input(f"Deseja alterar {possivel_mais} algum número? (s ou n) ")

                while pergunta != "s" and pergunta != "n":
                    pergunta = input("As possíveis respostas são apenas 's' ou 'n'. Digite novamente: ")

                if pergunta == "s":
                    n_a_alterar = float(input("\nQual número você gostaria de alterar? (Digite o número): "))

                    while n_a_alterar not in total_numeros:
                        n_a_alterar = float(
                            input("O número que você escolheu não está presente na lista, digite um que esteja "
                                  "para fazer a substituição: "))

                    i = total_numeros.index(n_a_alterar)
                    total_numeros.remove(n_a_alterar)
                    novo_n = float(input("\nDigite o novo número: "))
                    total_numeros.insert(i, novo_n)
                    possivel_mais = "mais"

                if pergunta == "n":
                    break

            print(f"\nOs números que você escolheu são: {total_numeros}")

            pares = list()
            impares = list()

            for x in total_numeros:
                if x / 2 == x // 2:
                    pares.append(x)
                else:
                    impares.append(x)

            print(f"Os pares são: {pares}\nOs Ímpares são: {impares}")
            print(f"\nNúmero de pares: {len(pares)}\nNúmero de Ímpares: {len(impares)}")

        if pergunta == "primo ou nao":
            lista = list()
            ask = int(input("\nQuantos números você quer usar? "))
            vez = 1

            for x in range(1, (ask + 1)):
                ask2 = int(input(f"\nDigite o número {vez}: "))
                lista.append(ask2)
                vez = vez + 1

            print(f"\nOs numeros que você escolheu são: {lista}")

            ask3 = input("\nDeseja alterar algum número? (s ou n) ")

            while ask3 != "s" and ask3 != "n":
                ask3 = input("\ncara na moral para de tentar burlar plmds...'s' ou 'n'? ")

            if ask3 == "s":
                qnts_alter = int(input("\nQuantos números você quer alterar? "))

                while qnts_alter > len(lista):
                    qnts_alter = int(
                        input("A lista não tem essa quantidade de números para alterar, digite novamente: "))

                for x in range(1, (qnts_alter + 1)):
                    alter = int(input("\nQual número você quer alterar? "))

                    while alter not in lista:
                        alter = int(input("\nO número que você escolheu não está na lsita, digite novamente: "))

                    lugar = lista.index(alter)
                    novo = int(input(f"\nQual número entrará no lugar do {alter}? "))
                    lista.insert(lugar, novo)
                    lista.remove(alter)

            print(f"\nOs números que você escolheu são: {lista}")

            primos = list()
            n_primos = list()
            possivel_p = list()

            for x in lista:
                if x == 1 or x == 2:
                    primos.append(x)
                else:
                    for y in range(2, x):
                        if x / y == x // y:
                            n_primos.append(x)
                            break
                        else:
                            possivel_p.append(x)
                    if x not in n_primos and x in possivel_p:
                        primos.append(x)

            print(f"\nOs primos são: {primos}\nOs não primos são: {n_primos}")

        if pergunta == "divisores":
            divisores = list()
            numero = list()
            pergunta1 = int(input("Qual número você quer? "))
            numero.append(pergunta1)

            while True:
                pergunta2 = input("Você deseja alterar o número? ('s' ou 'n') ")

                while pergunta2 != 's' and pergunta2 != 'n':
                    pergunta2 = input("As possíveis respostas são 's' ou 'n', digite novamente: ")

                if pergunta2 == 'n':
                    break

                if pergunta2 == 's':
                    nn = int(input(f"Qual número você quer colocar no lugar do {pergunta1}? "))
                    numero.remove(pergunta1)
                    numero.append(nn)

                print(f"O número agora é {numero}")

            for x in numero:
                for y in range(1, x + 1):
                    if x / y == x // y:
                        divisores.append(y)

            print(f"Os divisores do número {numero[0]} são: {divisores}.")

        if pergunta == "eq2":
            A, B, C = float(input("Digite o valore de A: ")), float(input("Digite o valore de B: ")), float(
                input("Digite o valore "
                      "de C: "))
            while True:
                ask4 = input(
                    f"Os valores que você escolheu para A, B e C, respectivamente foram: {A, B, C}. Deseja alterar "
                    f"algum? ('s'"
                    f"ou 'n') ")
                while ask4 != "s" and ask4 != "n":
                    ask4 = input("As possíveis respostas são 's' ou 'n'. Digite novamente: ")

                if ask4 == "s":
                    ask5 = (input("Qual letra você deseja alterar? (A, B ou C) "))

                    while ask5 != "A" and ask5 != "B" and ask5 != "C":
                        ask5 = input(
                            "Cara na moral, ou vc escreveu um minúsculo ou vc tá tentando burlar o sistema. Digita "
                            "dnv: ")

                    if ask5 == "A":
                        A = float(input("Qual será o novo valor de A? "))

                    if ask5 == "B":
                        B = float(input("Qual será o novo valor de B? "))

                    if ask5 == "C":
                        C = float(input("Qual será o novo valor de C? "))

                if ask4 == "n":
                    break

            delta = ((B ** 2) - (4 * A * C))
            raiz1 = (((-B) + (delta ** (1 / 2))) / (2 * A))
            raiz2 = (((-B) - (delta ** (1 / 2))) / (2 * A))

            if delta < 0:
                print("As raízes da equação são complexas.")

            if delta == 0:
                print(f"As raízes da equação são respectivamente: {raiz1, raiz2}.\nP.S Elas são iguais pq "
                      f"o delta da 0.")

            if delta > 0 and A + B + C != 0:
                print(f"As raízes da equação são respectivamente: {raiz1, raiz2}.")

            if delta > 0 and A + B + C == 0:
                print(f"As raízes da equação são respectivamente: {raiz1, raiz2}.\nP.S Essa equação foi "
                      f"resolvida pelo maçete do 'O CASO'!")

        final = input("\nVocê deseja continuar usando o programa? (s ou n) ")

        while final != "s" and final != "n":
            final = input("\nAs possíveis respostas são apenas 's' ou 'n', digite novamente: ")

        if final == "n":
            print("\nObrigado pela sua preferência!")
            exit("Feito por Felipe Fagundes de Azevedo")
