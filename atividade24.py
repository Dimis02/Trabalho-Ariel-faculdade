import math

def calcular_hipotenusa(a, b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return hipotenusa

def main():
    a = float(input("Digite o valor do cateto a: "))
    b = float(input("Digite o valor do cateto b: "))
    
    hipotenusa = calcular_hipotenusa(a, b)
    print("O valor da hipotenusa é:", hipotenusa)

if __name__ == "__main__":
    main()
