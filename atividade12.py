def converter_distancia_milhas_para_quilometros(distancia_milhas):
    distancia_quilometros = 1.61 * distancia_milhas
    return distancia_quilometros

distancia_milhas = float(input("Digite a distância em milhas: "))

distancia_quilometros = converter_distancia_milhas_para_quilometros(distancia_milhas)

print("A distância em quilômetros é:", distancia_quilometros)
