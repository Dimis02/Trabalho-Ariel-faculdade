def calcular_quantia_ganhadores(total, percentual):
    quantia = total * percentual / 100
    return quantia

def main():
    total = 780000.00
    
    quantia_primeiro_ganhador = calcular_quantia_ganhadores(total, 46)
    quantia_segundo_ganhador = calcular_quantia_ganhadores(total, 32)
    quantia_terceiro_ganhador = total - quantia_primeiro_ganhador - quantia_segundo_ganhador
    
    print("Quantia ganha pelo primeiro ganhador:", quantia_primeiro_ganhador)
    print("Quantia ganha pelo segundo ganhador:", quantia_segundo_ganhador)
    print("Quantia ganha pelo terceiro ganhador:", quantia_terceiro_ganhador)

if __name__ == "__main__":
    main()
