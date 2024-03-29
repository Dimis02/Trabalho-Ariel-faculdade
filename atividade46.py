def calcular_nota_segunda_avaliacao(media_aprovacao, nota_primeira_avaliacao):
    nota_segunda_avaliacao = (3 * media_aprovacao - nota_primeira_avaliacao) / 2
    return nota_segunda_avaliacao

def main():
    media_aprovacao = 7
    nota_primeira_avaliacao = float(input("Digite a nota obtida na primeira avaliação: "))
    
    nota_segunda_avaliacao = calcular_nota_segunda_avaliacao(media_aprovacao, nota_primeira_avaliacao)
    
    print("Para ser aprovado com média", media_aprovacao, "é necessário obter pelo menos", nota_segunda_avaliacao, "na segunda avaliação.")

if __name__ == "__main__":
    main()
