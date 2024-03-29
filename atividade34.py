def converter_maiuscula_para_minuscula(letra_maiuscula):
    if ord('A') <= ord(letra_maiuscula) <= ord('Z'):
        codigo_minuscula = ord(letra_maiuscula) + 32
        letra_minuscula = chr(codigo_minuscula)
        return letra_minuscula
    else:
        return "Por favor, insira uma letra maiúscula válida."

def main():
    letra_maiuscula = input("Digite uma letra maiúscula: ")
    letra_minuscula = converter_maiuscula_para_minuscula(letra_maiuscula)
    print("A letra minúscula correspondente é:", letra_minuscula)

if __name__ == "__main__":
    main()
