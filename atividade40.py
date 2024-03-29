def calcular_ganhadores_investimento(investimento1, investimento2, investimento3, premio):
    total_investido = investimento1 + investimento2 + investimento3
    proporcao1 = investimento1 / total_investido
    proporcao2 = investimento2 / total_investido
    proporcao3 = investimento3 / total_investido
    ganho1 = proporcao1 * premio
    ganho2 = proporcao2 * premio
    ganho3 = proporcao3 * premio
    return ganho1, ganho2, ganho3

def main():
    investimento1 = float(input("Digite o valor investido pelo primeiro apostador: "))
    investimento2 = float(input("Digite o valor investido pelo segundo apostador: "))
    investimento3 = float(input("Digite o valor investido pelo terceiro apostador: "))
    premio = float(input("Digite o valor total do prêmio: "))
    
    ganho1, ganho2, ganho3 = calcular_ganhadores_investimento(investimento1, investimento2, investimento3, premio)
    
    print("O primeiro apostador ganharia R$", ganho1)
    print("O segundo apostador ganharia R$", ganho2)
    print("O terceiro apostador ganharia R$", ganho3)

if __name__ == "__main__":
    main()
