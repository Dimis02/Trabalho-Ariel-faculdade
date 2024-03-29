def imprimir_digitos(numero):
    print(numero // 1000)
    print((numero % 1000) // 100)
    print((numero % 100) // 10)
    print(numero % 10)

def main():
    numero = int(input("Digite um número inteiro de quatro dígitos (entre 1000 e 9999): "))

    if 1000 <= numero <= 9999:
        imprimir_digitos(numero)
    else:
        print("Por favor, insira um número inteiro de quatro dígitos entre 1000 e 9999.")

if __name__ == "__main__":
    main()
