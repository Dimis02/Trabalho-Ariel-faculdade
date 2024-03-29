#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao 
#custo de fábrica. Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos de 45%, prepare um algoritmo para ler o custo de 
#fábrica do carro e imprimir o custo ao consumidor. 

Usuario = int(input("Custo de fabrica do carro: "))
Custo = Usuario * 0.12
Imposto = Usuario * 0.45
Valor_final = Usuario * Custo + Imposto 
print("Volor final do carro é: ", Valor_final )