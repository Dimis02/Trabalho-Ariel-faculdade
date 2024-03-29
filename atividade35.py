def inverter_numero(numero):
    numero_str = str(numero)
    numero_invertido_str = numero_str[::-1]
    numero_invertido = int(numero_invertido_str)
    return numero_invertido

def main():
    numero = int(input("Digite um número inteiro de três dígitos (entre 100 e 999): "))

    if 100 <= numero <= 999:
        numero_invertido = inverter_numero(numero)
        print("Número Gerado:", numero_invertido)
    else:
        print("Por favor, insira um número inteiro de três dígitos entre 100 e 999.")

if __name__ == "__main__":
    main()
