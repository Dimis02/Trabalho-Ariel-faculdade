#O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que 
#leia a quantidade de cada item que você consumiu e calcule a conta final. 
# a. Hambúrguer................. R$ 3,00 
# b. Cheeseburger.............. R$ 2,50 
# c. Fritas............................ R$ 2,50 
# d. Refrigerante ................. R$ 1,00 
# e. Milkshake..................... R$ 3,00 

H = int(input("Quantidade de Hambúrger é: "))
C = int(input("Quantidade de Cheeseburger é: "))
F = int(input("Quantidade de Fritas é: "))
R = int(input("Quantidade de Refrigerante é: "))
M = int(input("Quantidade de Milkshake é: "))
somatotal = (H * 3.00) + (C * 2.50) + (F * 2.50) + (R * 1.00) + (M * 3.00)
print(f'Valor total da conta é: ', {somatotal})