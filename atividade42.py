def calcular_custo_consumidor(custo_fabrica):
    percentual_distribuidor = 0.12
    percentual_impostos = 0.45
    
    valor_distribuidor = custo_fabrica * percentual_distribuidor
    valor_impostos = custo_fabrica * percentual_impostos
    custo_consumidor = custo_fabrica + valor_distribuidor + valor_impostos
    return custo_consumidor

def main():
    custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
    
    custo_final = calcular_custo_consumidor(custo_fabrica)
    
    print("O custo ao consumidor do carro é R$ {:.2f}".format(custo_final))

if __name__ == "__main__":
    main()
