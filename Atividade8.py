#Calcule a média de um aluno na disciplina de ED. Para isso solicite o nome do aluno, a nota da prova e a nota qualitativa. Sabe-se que a nota 
#da prova tem peso 2 e a nota qualitativa peso 1. Mostre a média como resultado.

Nome_do_aluno = (input("Digite seu nome: "))
Nota_da_Prova = int(input("Digite sua nota da Prova: "))
Nota_Qualitativa = int(input("Digite sua nota da Qualitativa: "))

Media = (Nota_Qualitativa + (Nota_da_Prova*2)) / 3

print (f"Sua nota é: {Media}")
