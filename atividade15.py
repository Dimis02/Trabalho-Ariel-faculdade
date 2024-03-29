def calcular_volume_piscina(largura, comprimento, profundidade):
    volume = largura * comprimento * profundidade
    return volume

largura = float(input("Digite a largura da piscina em metros: "))
comprimento = float(input("Digite o comprimento da piscina em metros: "))
profundidade = float(input("Digite a profundidade da piscina em metros: "))

volume_piscina = calcular_volume_piscina(largura, comprimento, profundidade)

print("O volume da piscina é:", volume_piscina, "m³")
