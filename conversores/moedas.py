def converter_moedas():
    print("\n====== CONVERSOR DE MOEDAS ======")
    print("Escolha a moeda que será convertida através do Real")
    print("1.Dólar")
    print("2.Euro")
    print("3.Peso Argentino")

    try:
        moeda = int(input("Digite a moeda a ser convertida: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        return

    if moeda == 1:
        try:
            reais = float(input("\nDigite quantos reais serão convertidos em Dólar: "))
            print(f'{reais:.2f}R$ são equivalentes à {reais * 5.67:.2f} Dólares')
        except ValueError:
            print("Valor inválido! Digite um número.")
    elif moeda == 2:
        try:
            reais = float(input("\nDigite quantos reais serão convertidos em Euro: "))
            print(f'{reais:.2f}R$ são equivalentes à {reais * 6.46:.2f} Euros')
        except ValueError:
            print("Valor inválido! Digite um número.")
    elif moeda == 3:
        try:
            reais = float(input("\nDigite quantos reais serão convertidos em Peso Argentino: "))
            print(f'{reais:.2f}R$ são equivalentes à {reais * 0.0050:.2f} Pesos Argentinos')
        except ValueError:
            print("Valor inválido! Digite um número.")
    else:
        print("\nDigite uma opção válida!")
