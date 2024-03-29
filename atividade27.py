def calcular_novo_salario(salario):
    aumento_percentual = 1.77
    novo_salario = salario * (1 + aumento_percentual / 100)
    return novo_salario

def main():
    salario = float(input("Digite o salário do funcionário: "))
    
    novo_salario = calcular_novo_salario(salario)
    print("O novo salário do funcionário é:", novo_salario)

if __name__ == "__main__":
    main()
