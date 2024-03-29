def aplicar_desconto(valor_produto, percentual_desconto):
    valor_com_desconto = valor_produto * (1 - percentual_desconto / 100)
    return valor_com_desconto

def main():
    valor_produto = float(input("Digite o valor do produto: "))
    percentual_desconto = 12
    
    valor_com_desconto = aplicar_desconto(valor_produto, percentual_desconto)
    print("O valor do produto com desconto é:", valor_com_desconto)

if __name__ == "__main__":
    main()
