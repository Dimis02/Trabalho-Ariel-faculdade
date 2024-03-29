#Sabendo que a média de aprovação é 7, e a formula para cálculo da média consiste em a primeira avaliação com peso 1 e a segunda 
#avaliação com peso 2, sendo divido por 3, realize o cálculo de quanto deve ser a nota da segunda avaliação para que o resultado seja a 
#aprovação. Elabore a fórmula para o cálculo e a representação do algoritmo para o mesmo. 

N1 = int(input("Digite a nota da primeira avaliação: "))

MEDIA = 7

N2 = ((MEDIA * 3) - N1) / 2

print("O valor que você deve ter na segunda avaliação para ser aprovado é:",N2)
