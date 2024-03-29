def calcular_salario_receber(salario_base):
    gratificacao = salario_base * 0.05
    imposto = salario_base * 0.07
    salario_receber = salario_base + gratificacao - imposto
    return salario_receber

def main():
    salario_base = float(input("Digite o salário-base do funcionário: "))
    
    salario_receber = calcular_salario_receber(salario_base)
    print("O salário a receber é R$ {:.2f}".format(salario_receber))

if __name__ == "__main__":
    main()
