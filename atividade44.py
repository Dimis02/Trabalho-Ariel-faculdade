def calcular_salario_vendedor(nome, num_carros_vendidos, valor_total_vendas):
    salario_fixo = 500.00
    comissao_por_carro = 50.00
    percentual_comissao = 0.05
    
    comissao_total_carros = num_carros_vendidos * comissao_por_carro
    comissao_total_vendas = valor_total_vendas * percentual_comissao
    salario_total = salario_fixo + comissao_total_carros + comissao_total_vendas
    return salario_total

def main():
    nome_vendedor = input("Digite o nome do vendedor: ")
    num_carros_vendidos = int(input("Digite o número de carros vendidos: "))
    valor_total_vendas = float(input("Digite o valor total das vendas: R$ "))
    
    salario_vendedor = calcular_salario_vendedor(nome_vendedor, num_carros_vendidos, valor_total_vendas)
    
    print("O salário total de", nome_vendedor, "no mês é R$ {:.2f}".format(salario_vendedor))

if __name__ == "__main__":
    main()
