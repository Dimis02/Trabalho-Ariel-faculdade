def converter_velocidade(metros_por_segundo):
    km_por_hora = metros_por_segundo * 3.6
    return km_por_hora

metros_por_segundo = float(input("Digite a velocidade em m/s: "))

km_por_hora = converter_velocidade(metros_por_segundo)

print("A velocidade em km/h é:", km_por_hora)