def calcular_desconto(valor_total):
    return valor_total * 0.10

def calcular_valor_parcelas(valor_total, num_parcelas):
    return valor_total / num_parcelas

def calcular_comissao_vista(valor_total):
    return valor_total * 0.05

def calcular_comissao_parcelada(valor_total):
    return valor_total * 0.05

def main():
    valor_total = float(input("Digite o valor total da venda: "))
    
    total_com_desconto = valor_total - calcular_desconto(valor_total)
    
    valor_parcela = calcular_valor_parcelas(valor_total, 3)
    
    comissao_vista = calcular_comissao_vista(total_com_desconto)
    
    comissao_parcelada = calcular_comissao_parcelada(valor_total)
    
    print("a. Total a pagar com desconto de 10%: R$", total_com_desconto)
    print("b. Valor de cada parcela (3x sem juros): R$", valor_parcela)
    print("c. Comissão do vendedor (venda à vista): R$", comissao_vista)
    print("d. Comissão do vendedor (venda parcelada): R$", comissao_parcelada)

if __name__ == "__main__":
    main()
