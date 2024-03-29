def calcular_custo_cercamento(comprimento, largura, preco_metro_tela):
    perimetro = 2 * (comprimento + largura)
    custo_total = perimetro * preco_metro_tela
    return custo_total

def main():
    comprimento = float(input("Digite o comprimento do terreno em metros: "))
    largura = float(input("Digite a largura do terreno em metros: "))
    preco_metro_tela = float(input("Digite o preço do metro de tela em reais: "))
    
    custo_cercamento = calcular_custo_cercamento(comprimento, largura, preco_metro_tela)
    
    print("O custo para cercar o terreno com tela é de R$", custo_cercamento)

if __name__ == "__main__":
    main()
