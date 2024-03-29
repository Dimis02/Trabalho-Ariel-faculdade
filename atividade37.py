def converter_segundos_para_horas_minutos_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = (segundos % 3600) % 60
    return horas, minutos, segundos_restantes

def main():
    segundos = int(input("Digite um valor inteiro em segundos: "))
    
    horas, minutos, segundos_restantes = converter_segundos_para_horas_minutos_segundos(segundos)
    
    print("Horas:", horas)
    print("Minutos:", minutos)
    print("Segundos:", segundos_restantes)

if __name__ == "__main__":
    main()
