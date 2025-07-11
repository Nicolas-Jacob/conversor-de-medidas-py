from conversores.medidas import converter_medidas
from conversores.moedas import converter_moedas
from conversores.tempo import converter_tempo

def exibir_menu():
    print("\n====== CONVERSOR UNIVERSAL ======")
    print("1.Converter medidas")
    print("2.Converter moedas")
    print("3.Converter tempo")
    print("4.Sair")

def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("\nPor favor, digite apenas números!\n")
            continue 

        if opcao == 1:
            converter_medidas()
        elif opcao == 2:
            converter_moedas()
        elif opcao == 3:
            converter_tempo()
        elif opcao == 4:
            print("\nObrigado por usar o Conversor Universal! Até logo.")
            exit()
        else:
            print("\nDigite uma opção válida!\n")

if __name__ == "__main__":
    main()
