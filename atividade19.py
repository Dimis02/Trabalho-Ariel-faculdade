def converter_para_dolar(valor_real, cotacao_dolar):
    valor_dolar = valor_real / cotacao_dolar
    return valor_dolar

valor_real = float(input("Digite o valor em real: "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))

valor_dolar = converter_para_dolar(valor_real, cotacao_dolar)

print("O valor correspondente em dólares é: $", valor_dolar)
