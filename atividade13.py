def converter_distancia_quilometros_para_milhas(distancia_quilometros):
    distancia_milhas = distancia_quilometros / 1.61
    return distancia_milhas

distancia_quilometros = float(input("Digite a distância em quilômetros: "))

distancia_milhas = converter_distancia_quilometros_para_milhas(distancia_quilometros)

print("A distância em milhas é:", distancia_milhas)