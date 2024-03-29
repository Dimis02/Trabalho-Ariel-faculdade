def calcular_ano_nascimento(idade, ano_atual):
    ano_nascimento = ano_atual - idade
    return ano_nascimento

def main():
    idade = int(input("Digite sua idade: "))
    ano_atual = int(input("Digite o ano atual: "))
    
    ano_nascimento = calcular_ano_nascimento(idade, ano_atual)
    
    print("Você nasceu aproximadamente no ano:", ano_nascimento)

if __name__ == "__main__":
    main()
