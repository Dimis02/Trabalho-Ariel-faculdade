def calcular_media(num1, num2, num3, num4):
    media = (num1 + num2 + num3 + num4) / 4
    return media

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

resultado_media = calcular_media(numero1, numero2, numero3, numero4)

print("A média dos quatro números é:", resultado_media)
