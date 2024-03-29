#Sabendo que a média de aprovação é 7, e a formula para cálculo da média consiste em a primeira avaliação com peso 1 e a segunda 
#avaliação com peso 2, sendo divido por 3, realize o cálculo de quanto deve ser a nota da primeira avaliação para que o resultado seja a 
#aprovação. Elabore a fórmula para o cálculo e a representação do algoritmo para o mesmo. 
#a. MEDIA = (N1 + (N2 * 2)) / 3 

media_aprovacao = 7

nota2 = float(input("Informe a nota 2 do aluno: "))

nota1 = (3 * media_aprovacao) - (nota2 * 2)

print(f"O aluno deve tirar {nota1:} na nota 1 para ser aprovado.")
