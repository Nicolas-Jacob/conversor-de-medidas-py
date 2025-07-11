def converter_medidas():
    print("\n====== CONVERSOR DE MEDIDAS ======")
    print("Escolha o tipo de medida")
    print("1.Comprimento")
    print("2.Massa")
    print("3.Temperatura")

    try:
        tipo_medida = int(input("Digite o tipo de medida a ser convertida: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        return

    if tipo_medida == 1:
        print("\n1.Metros para Quilômetros")
        print("2.Quilômetros para Milhas")
        try:
            conversao_comprimento = int(input("\nEscolha a conversão a ser feita: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            return
        if conversao_comprimento == 1:
            try:
                metros = float(input("\nDigite quantos metros serão convertidos em Km: "))
                print(f"{metros:.2f} metros são equivalentes à {metros / 1000:.2f} Km")
            except ValueError:
                print("Valor inválido! Digite um número.")
        elif conversao_comprimento == 2:
            try:
                km = float(input("\nDigite quantos quilômetros serão convertidos em Milhas: "))
                print(f"{km:.2f} km são equivalentes à {km * 0.621:.2f} Milhas")
            except ValueError:
                print("Valor inválido! Digite um número.")
        else:
            print("Digite uma opção válida!")

    elif tipo_medida == 2:
        print("\n1.Gramas para Quilogramas")
        print("2.Quilogramas para libras")
        try:
            conversao_massa = int(input("\nDigite a conversão de massas a ser realizada: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            return

        if conversao_massa == 1:
            try:
                gramas = float(input("\nDigite quantas Gramas serão convertidas em Quilogramas: "))
                print(f"{gramas:.2f} gramas são equivalentes à {gramas / 1000:.2f} KG")
            except ValueError:
                print("Valor inválido! Digite um número.")
        elif conversao_massa == 2:
            try:
                kg = float(input("\nDigite quantos Quilogramas serão convertidas em Libras: "))
                print(f"{kg:.2f} Quilogramas são equivalentes à {kg * 2.20462:.2f} Libras")
            except ValueError:
                print("Valor inválido! Digite um número.")
        else:
            print("Digite uma opção válida!")

    elif tipo_medida == 3:
        print("\n1.Fahrenheit")
        print("2.Kelvin")
        try:
            conversao_temperatura = int(input("Digite a conversão a ser feita: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            return

        if conversao_temperatura == 1:
            try:
                celsius = float(input("\nDigite quantos Graus Celsius serão convertidos em Fahrenheit: "))
                print(f"{celsius}ºC são equivalentes à {(celsius * 1.8) + 32}ºF")
            except ValueError:
                print("Valor inválido! Digite um número.")
        elif conversao_temperatura == 2:
            try:
                celsius = float(input("\nDigite quantos Graus Celsius serão convertidos em Kelvin: "))
                print(f"{celsius}ºC são equivalentes à {celsius + 273.15:.2f}K")
            except ValueError:
                print("Valor inválido! Digite um número.")
        else:
            print("\nDigite uma opção válida!")
    else:
        print("\nDigite uma opção válida!")
