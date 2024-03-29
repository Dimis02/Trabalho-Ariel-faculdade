def calcular_salario_liquido(dias_trabalhados, valor_diario):
    salario_bruto = dias_trabalhados * valor_diario
    desconto_previdencia = salario_bruto * 0.11
    salario_apos_previdencia = salario_bruto - desconto_previdencia
    desconto_imposto_renda = salario_apos_previdencia * 0.08
    salario_liquido = salario_apos_previdencia - desconto_imposto_renda
    return salario_liquido

def main():
    valor_diario = 30.00
    dias_trabalhados = int(input("Digite o número de dias trabalhados pelo encanador: "))
    
    salario_liquido = calcular_salario_liquido(dias_trabalhados, valor_diario)
    print("A quantia líquida a ser paga ao encanador é R$", salario_liquido)

if __name__ == "__main__":
    main()
