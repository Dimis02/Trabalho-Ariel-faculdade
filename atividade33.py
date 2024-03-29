import math

def calcular_numero_degraus(altura_degrau, altura_desejada):
    numero_degraus = altura_desejada / altura_degrau
    numero_degraus = math.ceil(numero_degraus) 
    return numero_degraus

def main():
    altura_degrau = float(input("Digite a altura do degrau da escada em metros: "))
    altura_desejada = float(input("Digite a altura que deseja alcançar em metros: "))
    
    numero_degraus = calcular_numero_degraus(altura_degrau, altura_desejada)
    print("Você precisará subir", numero_degraus, "degraus para alcançar a altura desejada.")

if __name__ == "__main__":
    main()
