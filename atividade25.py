import math

def calcular_volume_cilindro(raio, altura):
    pi = math.pi
    volume = pi * raio**2 * altura
    return volume

def main():
    raio = float(input("Digite o raio do cilindro: "))
    altura = float(input("Digite a altura do cilindro: "))
    
    volume = calcular_volume_cilindro(raio, altura)
    print("O volume do cilindro é:", volume)

if __name__ == "__main__":
    main()
