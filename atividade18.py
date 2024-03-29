def calcular_media_semestre(nota_g1, nota_g2):
    media_semestre = (nota_g1 + (nota_g2 * 2) / 3)
    return media_semestre

nota_g1 = float(input("Digite a nota de G1: "))
nota_g2 = float(input("Digite a nota de G2: "))

media_semestre = calcular_media_semestre(nota_g1, nota_g2)

if media_semestre >= 7.0:
    print("Parabéns! Você foi aprovado com média", media_semestre)
else:
    print("Infelizmente você não foi aprovado. Sua média foi", media_semestre)
