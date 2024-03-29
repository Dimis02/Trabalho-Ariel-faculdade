def calcular_media(nota_prova, nota_qualitativa):
    peso_prova = 2
    peso_qualitativa = 1
    
    media = (nota_prova * peso_prova + nota_qualitativa * peso_qualitativa) / (peso_prova + peso_qualitativa)
    return media

def main():
    nome_aluno = input("Digite o nome do aluno: ")
    nota_prova = float(input("Digite a nota da prova: "))
    nota_qualitativa = float(input("Digite a nota qualitativa: "))
    
    media_aluno = calcular_media(nota_prova, nota_qualitativa)
    
    print("A média do aluno", nome_aluno, "na disciplina de Estrutura de Dados é:", media_aluno)

if __name__ == "__main__":
    main()
