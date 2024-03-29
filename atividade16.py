def soma_quadrados(val1, val2, val3):
    soma = val1**2 + val2**2 + val3**2
    return soma

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

resultado = soma_quadrados(valor1, valor2, valor3)

print("A soma dos quadrados dos três números é:", resultado)
