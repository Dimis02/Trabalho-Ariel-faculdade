import math

def converter_graus_para_radianos(angulo_graus):
    angulo_radianos = angulo_graus * math.pi / 180
    return angulo_radianos

angulo_graus = float(input("Digite o ângulo em graus: "))

angulo_radianos = converter_graus_para_radianos(angulo_graus)

print("O ângulo em radianos é:", angulo_radianos)
