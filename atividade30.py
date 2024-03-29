def calcular_valor_pago(hora_trabalho, horas_mes):
    salario_bruto = hora_trabalho * horas_mes
    valor_pago = salario_bruto * 1.10 
    return valor_pago

def main():
    hora_trabalho = float(input("Digite o valor da hora de trabalho em reais: "))
    horas_mes = float(input("Digite o número de horas trabalhadas no mês: "))
    
    valor_total_pago = calcular_valor_pago(hora_trabalho, horas_mes)
    print("O valor a ser pago ao funcionário é R$ {:.2f}".format(valor_total_pago))

if __name__ == "__main__":
    main()
