def converter_tempo():
    print("\n====== CONVERSOR DE TEMPO ======")
    print("1.Horas para Minutos")
    print("2.Minutos para Segundos")
    print("3.Dias para Horas")
    print("4.Semanas para Dias")

    try:
        tempo = int(input("Digite o tempo a ser convertido: "))
    except ValueError:
        print("\nPor favor, digite um número válido!")
        return

    if tempo == 1:
        try:
            horas = float(input("\nDigite quantas Horas serão convertidas em Minutos: "))
            print(f"{horas:.2f} horas são equivalentes à {horas * 60:.2f} Minutos")
        except ValueError:
            print("Valor inválido! Digite um número.")
    elif tempo == 2:
        try:
            minutos = float(input("\nDigite quantos Minutos serão convertidos em Segundos: "))
            print(f"{minutos:.2f} Minutos são equivalentes à {minutos * 60:.2f} Segundos")
        except ValueError:
            print("Valor inválido! Digite um número.")
    elif tempo == 3:
        try:
            dias = float(input("\nDigite quantos Dias serão convertidos para Horas: "))
            print(f"{dias:.2f} Dias são equivalentes à {dias * 24:.2f} Horas")
        except ValueError:
            print("Valor inválido! Digite um número.")
    elif tempo == 4:
        try:
            semanas = float(input("\nDigite quantas Semanas serão convertidas em Dias: "))
            print(f"{semanas:.2f} Semanas são equivalentes à {semanas * 7:.2f} Dias")
        except ValueError:
            print("Valor inválido! Digite um número.")
    else:
        print("Digite uma opção válida!")
